import pytest
from src.user.domain.exceptions.email_not_well_formed_exception import (
    EmailNotWellFormedException,
)
from src.user.domain.entities.entity import User
from src.user.app.create.create_handler import CreateHandler
from src.user.domain.exceptions.password_minimun_len_exception import (
    PasswordMinimunLenException,
)
from src.user.infrastructure.repository_in_memory import RepositoryInMemory
from src.user.app.create.create_command import CreateCommand


def test_when_creating_a_user_it_shuould_be_created_and_return_the_public_user():
    repository = RepositoryInMemory()
    handler = CreateHandler(repository)
    user_name = "Jonh"
    user_surname = "Doe"
    user_email = "johndoe@test.com"
    user_password = "12345678"
    command = CreateCommand(user_name, user_surname, user_email, user_password)

    handler.handle(command)
    user: User | None = None

    for user_at_repository in repository._users:
        if user_at_repository._email.get_value() == user_email:
            user = user_at_repository

    assert user._name == user_name
    assert user._surname == user_surname
    assert user._email.get_value() == user_email
    assert user._password.get_value() == user_password


def test_register_handler_should_return_an_exception_if_the_email_is_not_well_formed():
    repository = RepositoryInMemory()
    handler = CreateHandler(repository)
    user_name = "Jonh"
    user_surname = "Doe"
    user_email = "johndoe@.com"
    user_password = "12345678"
    command = CreateCommand(user_name, user_surname, user_email, user_password)

    with pytest.raises(EmailNotWellFormedException):
        handler.handle(command)


def test_register_handler_should_return_an_exception_if_the_password_is_not_well_formed():
    repository = RepositoryInMemory()
    handler = CreateHandler(repository)
    user_name = "Jonh"
    user_surname = "Doe"
    user_email = "johndoe@test.com"
    user_password = "12345"
    command = CreateCommand(user_name, user_surname, user_email, user_password)

    with pytest.raises(PasswordMinimunLenException):
        handler.handle(command)
