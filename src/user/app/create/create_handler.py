from uuid import uuid4
from src.user.domain.entities.entity import User
from src.user.domain.exceptions.email_not_well_formed_exception import (
    EmailNotWellFormedException,
)
from src.user.domain.exceptions.user_already_created_exception import (
    UserAlreadyCreatedException,
)
from src.user.domain.repository_interface import Repository
from src.user.domain.register_command import CreateCommand
from src.user.domain.helpers.guard_email_well_formed import is_mail_well_formed


class CreateHandler:
    def __init__(
        self,
        repository: Repository,
    ) -> None:
        self._repository = repository

    def handle(self, command: CreateCommand) -> None:
        is_mail_well_formed_result = is_mail_well_formed(command._email)

        if is_mail_well_formed_result is False:
            raise EmailNotWellFormedException(
                f"Email {command._email} is not well formed"
            )

        created_user = self._repository.find_by_email(command._email)

        if created_user is not None:
            raise UserAlreadyCreatedException(
                f"User already created with email {command._email}"
            )

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
