from uuid import uuid4
from src.user.app.create.create_command import CreateCommand
from src.user.app.create.create_handler import CreateHandler
from src.user.app.update.update_command import UpdateCommand
from src.user.app.update.update_handler import UpdateHandler
from src.user.domain.entities.entity import User
from src.user.infrastructure.adapters.repository_in_memory import RepositoryInMemory


def test_update_name_handler():
    repository = RepositoryInMemory()
    handler = CreateHandler(repository)
    id = uuid4()
    user_name = "Jonh"
    user_surname = "Doe"
    user_email = "johndoe@test.com"
    user_password = "12345678"
    command = CreateCommand(id, user_name, user_surname, user_email, user_password)

    handler.handle(command)

    update_handler = UpdateHandler(repository)
    updated_user_name = "Nemandja"
    update_command = UpdateCommand(
        {
            "id": id,
            "name": updated_user_name,
            "surname": None,
            "email": None,
            "refresh_token": None,
        }
    )

    update_handler.handle(update_command)

    updated_user: User | None = None

    for user in repository._users:
        if user._id == id:
            updated_user = user

    assert updated_user._name == updated_user_name


def test_update_surname_handler():
    repository = RepositoryInMemory()
    handler = CreateHandler(repository)
    id = uuid4()
    user_name = "Jonh"
    user_surname = "Doe"
    user_email = "johndoe@test.com"
    user_password = "12345678"
    command = CreateCommand(id, user_name, user_surname, user_email, user_password)

    handler.handle(command)

    update_handler = UpdateHandler(repository)
    updated_user_surname = "Vidic"
    update_command = UpdateCommand(
        {
            "id": id,
            "name": None,
            "surname": updated_user_surname,
            "email": None,
            "refresh_token": None,
        }
    )

    update_handler.handle(update_command)

    updated_user: User | None = None

    for user in repository._users:
        if user._id == id:
            updated_user = user

    assert updated_user._surname == updated_user_surname


def test_update_email_handler():
    repository = RepositoryInMemory()
    handler = CreateHandler(repository)
    id = uuid4()
    user_name = "Jonh"
    user_surname = "Doe"
    user_email = "johndoe@test.com"
    user_password = "12345678"
    command = CreateCommand(id, user_name, user_surname, user_email, user_password)

    handler.handle(command)

    update_handler = UpdateHandler(repository)
    updated_user_email = "nemandjavidic@test.com"
    update_command = UpdateCommand(
        {
            "id": id,
            "name": None,
            "surname": None,
            "email": updated_user_email,
            "refresh_token": None,
        }
    )

    update_handler.handle(update_command)

    updated_user: User | None = None

    for user in repository._users:
        if user._id == id:
            updated_user = user

    assert updated_user._email == updated_user_email


def test_update_refresh_token_handler():
    repository = RepositoryInMemory()
    handler = CreateHandler(repository)
    id = uuid4()
    user_name = "Jonh"
    user_surname = "Doe"
    user_email = "johndoe@test.com"
    user_password = "12345678"
    command = CreateCommand(id, user_name, user_surname, user_email, user_password)

    handler.handle(command)

    update_handler = UpdateHandler(repository)
    updated_user_refresh_token = "token"
    update_command = UpdateCommand(
        {
            "id": id,
            "name": None,
            "surname": None,
            "email": None,
            "refresh_token": updated_user_refresh_token,
        }
    )

    update_handler.handle(update_command)

    updated_user: User | None = None

    for user in repository._users:
        if user._id == id:
            updated_user = user

    assert updated_user._refresh_token == updated_user_refresh_token


def test_update_attributes():
    repository = RepositoryInMemory()
    handler = CreateHandler(repository)
    id = uuid4()
    user_name = "Jonh"
    user_surname = "Doe"
    user_email = "johndoe@test.com"
    user_password = "12345678"
    command = CreateCommand(id, user_name, user_surname, user_email, user_password)

    handler.handle(command)

    update_handler = UpdateHandler(repository)
    updated_user_name = "Nemandja"
    updated_user_surname = "Vidic"
    updated_user_refresh_token = "token"
    update_command = UpdateCommand(
        {
            "id": id,
            "name": updated_user_name,
            "surname": updated_user_surname,
            "email": None,
            "refresh_token": updated_user_refresh_token,
        }
    )

    update_handler.handle(update_command)

    updated_user: User | None = None

    for user in repository._users:
        if user._id == id:
            updated_user = user

    assert updated_user._name == updated_user_name
    assert updated_user._surname == updated_user_surname
    assert updated_user._refresh_token == updated_user_refresh_token
