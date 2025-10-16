from typing import Optional, Self


class User:
    def __init__(
        self, id: str, username: str, password: str, refresh_token: Optional[str]
    ) -> None:
        self._id = id
        self._username = username
        self._password = password
        self._refresh_token = refresh_token

    def set_username(self, username: str):
        self._username = username

    def set_refresh_token(self, refresh_token: str):
        self._refresh_token = refresh_token

    def to_dict(self):
        return {
            "id": self._id,
            "username": self._username,
            "password": self._password,
            "refresh_token": self._refresh_token,
        }

    @staticmethod
    def unmarshall(
        data_from_database: {
            "id": str,
            "username": str,
            "password": str,
            "refresh_token": Optional[str],
        },
    ) -> Self:
        return User(
            data_from_database["id"],
            data_from_database["username"],
            data_from_database["password"],
            data_from_database["refresh_token"],
        )
