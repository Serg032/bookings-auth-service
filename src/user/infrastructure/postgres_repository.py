import os
from typing import Optional
from src.user.domain.public_user import PublicUser
from src.user.domain.repository_interface import Repository
from src.user.domain.entity import User
from supabase import create_client, Client
from dotenv import load_dotenv
from src.user.domain.password_hasher_interface import PasswordHasher


class PostgresRepository(Repository):
    def __init__(self, tablename: str, password_hasher: PasswordHasher) -> None:
        load_dotenv()
        supabase_url = os.environ.get("SUPABASE_URL")
        supabase_key = os.environ.get("SUPABASE_KEY")
        self._users_tablename = tablename
        self._supabase: Client = create_client(supabase_url, supabase_key)
        self._password_hasher = password_hasher

    def create(self, user: User) -> PublicUser:
        hashed_password = self._password_hasher.hash(user._password)
        user_to_insert = user.to_dict()
        user_to_insert["password"] = hashed_password
        result = (
            self._supabase.table(self._users_tablename).insert(user_to_insert).execute()
        )

        if result.data[0] is None:
            raise Exception("Something went wrong, there is no data to retreive")

        created_user = result.data[0]

        return PublicUser(created_user["id"], created_user["username"])

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
            

    def find_by_username(self, username: str) -> Optional[User]:
        response = (
            self._supabase.table(self._users_tablename)
            .select("*")
            .eq("username", username)
            .execute()
        )

        if response.data and response.data[0] != None:
            data = response.data[0]
            marshalled_user = User.unmarshall(data)

            return marshalled_user

    def clear_database(self, username: str):
        # Supabase requiere un filtro en delete(); usamos uno que coincide con todas las filas
        self._supabase.table(self._users_tablename).delete().neq(
            "username", username
        ).execute()
