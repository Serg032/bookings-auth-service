import pytest
from src.user.domain.email_not_well_formed_exception import EmailNotWellFormedException
from src.user.domain.entity import User
from src.user.app.create.register_create import CreateHandler
from src.user.infrastructure.repository_in_memory import RepositoryInMemory
from src.user.domain.register_command import CreateCommand
from src.user.domain.user_already_created_exception import UserAlreadyCreatedException


def test_when_creating_a_user_it_shuould_be_created_and_return_the_public_user():
    repository = RepositoryInMemory()
    handler = CreateHandler(repository)
    user_name = "Jonh"
    user_surname = "Doe"
    user_email = "johndoe@test.com"
    user_password = "123456"
    command = CreateCommand(user_name, user_surname, user_email, user_password)

    handler.handle(command)
    user: User | None = None

    for user_at_repository in repository._users:
        if user_at_repository._email == user_email:
            user = user_at_repository

    assert user._name == user_name
    assert user._surname == user_surname
    assert user._email == user_email
    assert user._password == user_password


def test_register_handler_should_return_an_exception_if_the_email_is_not_well_formed():
    repository = RepositoryInMemory()
    handler = CreateHandler(repository)
    user_name = "Jonh"
    user_surname = "Doe"
    user_email = "johndoe@.com"
    user_password = "123456"
    command = CreateCommand(user_name, user_surname, user_email, user_password)

    with pytest.raises(EmailNotWellFormedException):
        handler.handle(command)


def test_register_handler_should_return_an_exception_if_the_username_already_exists():
    repository = RepositoryInMemory()
    handler = CreateHandler(repository)
    user_name = "Jonh"
    user_surname = "Doe"
    user_email = "johndoe@test.com"
    user_password = "123456"
    command = CreateCommand(user_name, user_surname, user_email, user_password)

    handler.handle(command)
    with pytest.raises(UserAlreadyCreatedException):
        handler.handle(command)
