import bcrypt
from src.user.domain.ports.password_hasher_interface import PasswordHasher


class BcryptPasswordHasher(PasswordHasher):
    def __init__(self) -> None:
        self._bcrypt = bcrypt

    def hash(self, raw_password: str) -> str:
        return self._bcrypt.hashpw(
            raw_password.encode(), self._bcrypt.gensalt()
        ).decode()

    def verify(self, hashed_password: str, raw_password: str) -> bool:
        return self._bcrypt.checkpw(raw_password.encode(), hashed_password.encode())
