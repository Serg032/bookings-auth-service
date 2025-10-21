from typing import Optional, Self


class User:
    def __init__(
        self,
        id: str,
        name: str,
        surname: str,
        email: str,
        password: str,
        refresh_token: Optional[str],
    ) -> None:
        self._id = id
        self._name = name
        self._surname = surname
        self._email = email
        self._password = password
        self._refresh_token = refresh_token

    def to_dict(self):
        return {
            "id": self._id,
            "name": self._name,
            "surname": self._surname,
            "email": self._email,
            "password": self._password,
            "refresh_token": self._refresh_token,
        }

    @staticmethod
    def unmarshall(
        data_from_database: {
            "id": str,
            "name": str,
            "surname": str,
            "email": str,
            "password": str,
            "refresh_token": Optional[str],
        },
    ) -> Self:
        return User(
            data_from_database["id"],
            data_from_database["name"],
            data_from_database["surname"],
            data_from_database["email"],
            data_from_database["password"],
            data_from_database["refresh_token"],
        )
