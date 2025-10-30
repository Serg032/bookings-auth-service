from src.user.app.update.update_command import UpdateCommand
from src.user.app.update.update_handler import UpdateHandler
from src.user.infrastructure.controllers.controller_interface import Controller


class UpdateController(Controller):
    def __init__(self, handler: UpdateHandler) -> None:
        self._handler = handler

    def execute(self, args: dict | None) -> None:
        command = UpdateCommand(
            {
                "id": args["id"],
                "name": args["name"],
                "surname": args["surname"],
                "email": args["email"],
                "refresh_token": args["refresh_token"],
            }
        )
        return self._handler.handle(command)
