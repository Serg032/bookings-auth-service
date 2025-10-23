from uuid import uuid4
from src.user.domain.entities.entity import User
from src.user.domain.exceptions.email_not_well_formed_exception import (
    EmailNotWellFormedException,
)
from src.user.domain.exceptions.user_already_created_exception import (
    UserAlreadyCreatedException,
)
from src.user.domain.repository_interface import Repository
from src.user.app.create.create_command import CreateCommand
from src.user.domain.helpers.guard_email_well_formed import is_mail_well_formed


class CreateHandler:
    def __init__(
        self,
        repository: Repository,
    ) -> None:
        self._repository = repository

    def handle(self, command: CreateCommand) -> None:

        self._repository.create(
            User(
                str(uuid4()),
                command._name,
                command._surname,
                command._email,
                command._password,
                None,
            )
        )
