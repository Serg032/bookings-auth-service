from typing import TypedDict
from src.user.app.create.create_command import CreateCommand
from src.user.app.create.create_handler import CreateHandler
from src.user.infrastructure.controllers.controller_interface import Controller


class CreateCommandDict(TypedDict):
    id: str
    name: str
    surname: str
    email: str
    password: str


class CreateController(Controller):
    def __init__(self, handler: CreateHandler) -> None:
        self._handler = handler

    def execute(
        self,
        command: CreateCommandDict | None,
    ) -> None:
        print("COMMAND", command)
        command_obj = CreateCommand(
            command["id"],
            command["name"],
            command["surname"],
            command["email"],
            command["password"],
        )
        self._handler.handle(command_obj)
