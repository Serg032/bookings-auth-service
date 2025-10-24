import pytest
from src.user.app.create.create_handler import CreateHandler
from src.user.domain.exceptions.user_not_found_exception import UserNotFoundException
from src.user.infrastructure.repository_in_memory import RepositoryInMemory
from src.user.app.create.create_command import CreateCommand
from src.user.domain.repository_interface import Repository
from src.user.domain.entities.public_user import PublicUser


class FindByEmailHandler:
    def __init__(self, repository: Repository) -> None:
        self._repository = repository

    def handle(self, email: str) -> PublicUser:

        user = self._repository.find_by_email(email)

        if user is None:
            raise UserNotFoundException(f"email {email}")

        return PublicUser(user._id, user._name, user._surname, user._email.get_value())


def test_when_asking_for_a_user_by_email_it_should_retrieve_the_user():
    repository = RepositoryInMemory()
    create_handler = CreateHandler(repository)
    user_name = "Jonh"
    user_surname = "Doe"
    user_email = "johndoe@test.com"
    user_password = "12345678"
    command = CreateCommand(user_name, user_surname, user_email, user_password)

    create_handler.handle(command)

    find_by_email_handler = FindByEmailHandler(repository)

    user_by_email = find_by_email_handler.handle(user_email)

    assert user_email == user_by_email.email
    assert user_name == user_by_email.name
    assert user_surname == user_by_email.surname
    assert user_email == user_by_email.email


def test_when_asking_for_a_user_by_email_it_should_retrieve_a_exception_if_the_user_doesnt_exist():
    repository = RepositoryInMemory()
    handler = FindByEmailHandler(repository)

    with pytest.raises(UserNotFoundException):
        handler.handle("wrong_email")
