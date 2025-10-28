from src.user.app.update.update_command import UpdateCommand
from src.user.domain.ports.repository_interface import Repository


class UpdateHandler:
    def __init__(self, repository: Repository) -> None:
        self._repository = repository

    def handle(self, command: UpdateCommand) -> None:
        return self._repository.update(command)
