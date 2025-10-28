from typing import Optional
from src.user.app.auth.login.login_handler import LoginHandler
from src.user.app.auth.login.login_output import LoginOutput
from src.user.infrastructure.controllers.controller_interface import Controller


class LoginController(Controller):
    def __init__(self, handler: LoginHandler) -> None:
        self._handler = handler

    def execute(self, args: dict | None) -> Optional[LoginOutput]:
        return self._handler.handle(args["email"], args["password"])
