import os
from typing import Optional
from src.user.domain.repository_interface import Repository
from src.user.domain.entities.entity import User
from supabase import create_client, Client
from dotenv import load_dotenv
from src.user.domain.password_hasher_interface import PasswordHasher
from src.user.domain.update_command import UpdateCommand


class PostgresRepository(Repository):
    def __init__(
        self, tablename: str, password_hasher: Optional[PasswordHasher]
    ) -> None:
        load_dotenv()
        supabase_url = os.environ.get("SUPABASE_URL")
        supabase_key = os.environ.get("SUPABASE_KEY")
        self._users_tablename = tablename
        self._supabase: Client = create_client(supabase_url, supabase_key)
        self._password_hasher = password_hasher

    def create(self, user: User) -> None:
        if self._password_hasher is None:
            raise Exception("Password Haser neded when creating a user")
        hashed_password = self._password_hasher.hash(user._password.get_value())
        user_to_insert = user.to_dict()
        user_to_insert["password"] = hashed_password
        self._supabase.table(self._users_tablename).insert(user_to_insert).execute()

    def find_by_id(self, id: str) -> Optional[User]:
        response = (
            self._supabase.table(self._users_tablename)
            .select("*")
            .eq("id", id)
            .execute()
        )

        if response and response.data and response.data[0] is not None:
            data = response.data[0]
            return User.unmarshall(data)

    def find_by_email(self, email: str) -> Optional[User]:
        response = (
            self._supabase.table(self._users_tablename)
            .select("*")
            .eq("email", email)
            .execute()
        )

        if response.data and response.data[0] != None:
            data = response.data[0]
            marshalled_user = User.unmarshall(data)

            return marshalled_user

    def update(self, user: User, command: UpdateCommand) -> Optional[User]:
        update_fields: dict = {}

        if command._username is not None:
            update_fields["username"] = command._username
        if command._refresh_token is not None:
            update_fields["refresh_token"] = command._refresh_token

        if not update_fields:
            return user

        response = (
            self._supabase.table(self._users_tablename)
            .update(update_fields)
            .eq("id", user._id)
            .execute()
        )

        if response and response.data and response.data[0] is not None:
            updated = response.data[0]
            return User.unmarshall(updated)

        return None

    def clear_database(self, username: str):
        # Supabase requiere un filtro en delete(); usamos uno que coincide con todas las filas
        self._supabase.table(self._users_tablename).delete().neq(
            "username", username
        ).execute()
