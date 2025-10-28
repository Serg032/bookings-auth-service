from typing import Optional
from src.user.domain.ports.auth_adapter_interface import AuthAdapter
from src.user.app.auth.login.login_output import LoginOutput


class LoginHandler:
    def __init__(self, auth_handler: AuthAdapter) -> None:
        self._auth_adapter = auth_handler

    def handle(self, email: str, password: str) -> Optional[LoginOutput]:
        return self._auth_adapter.login(email, password)
