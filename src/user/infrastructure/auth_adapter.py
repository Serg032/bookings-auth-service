import os
import jwt
from typing import Optional
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from src.user.domain.auth_adapter_interface import AuthAdapter
from src.user.domain.login_output import LoginOutput
from src.user.domain.repository_interface import Repository
from src.user.domain.password_hasher_interface import PasswordHasher


class JWTAuthAdapter(AuthAdapter):
    def __init__(self, repository: Repository, password_hasher: PasswordHasher) -> None:
        load_dotenv()
        self._repository = repository
        self._password_hasher = password_hasher
        self._access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")
        self._refresh_token_secret = os.environ.get("REFRESH_TOKEN_SECRET")

    def create_access_token_payload():
        return

    def login(self, username: str, password: str) -> Optional[LoginOutput]:
        user = self._repository.find_by_username(username)

        if user is None:
            return None

        if not self._password_hasher.verify(user._password, password):
            return None

        now = datetime.now(timezone.utc)
        access_payload = {
            "sub": user._id,
            "typ": "access",
            "iat": int(now.timestamp()),
            "exp": int((now + timedelta(minutes=15)).timestamp()),
        }
        refresh_payload = {
            "sub": user._id,
            "typ": "refresh",
            "iat": int(now.timestamp()),
            "exp": int((now + timedelta(days=14)).timestamp()),
        }

        access_token = jwt.encode(
            access_payload, self._access_token_secret, algorithm="HS256"
        )
        refresh_token = jwt.encode(
            refresh_payload, self._refresh_token_secret, algorithm="HS256"
        )

        return LoginOutput(access_token, refresh_token)
