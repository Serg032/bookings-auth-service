from typing import Optional
from src.user.app.find_by_email.find_by_email_handler import FindByEmailHandler
from src.user.domain.entities.public_user import PublicUser
from src.user.infrastructure.controllers.controller_interface import Controller


class FindByEmailController(Controller):
    def __init__(self, handler: FindByEmailHandler) -> None:
        self._handler = handler

    def execute(self, args: dict | None) -> Optional[PublicUser]:
        return self._handler.handle(args["email"])
