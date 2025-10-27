from uuid import uuid4
import pytest
from src.user.app.create.create_handler import CreateHandler
from src.user.app.find_by_id.find_by_id_handler import FindByIdHandler
from src.user.app.create.create_command import CreateCommand
from src.user.domain.exceptions.user_not_found_exception import UserNotFoundException
from src.user.infrastructure.adapters.repository_in_memory import RepositoryInMemory


def test_find_by_id_handler_successfull():
    repository = RepositoryInMemory()
    create_handler = CreateHandler(repository)
    id = uuid4()
    user_name = "Jonh"
    user_surname = "Doe"
    user_email = "johndoe@test.com"
    user_password = "12345678"
    command = CreateCommand(id, user_name, user_surname, user_email, user_password)
    create_handler.handle(command)

    user_id = repository._users[0]._id
    find_by_id_handler = FindByIdHandler(repository)
    user = find_by_id_handler.handle(user_id)

    user_to_dict = user.to_dict()

    assert user_to_dict["id"] == user_id
    assert user_to_dict["name"] == user_name
    assert user_to_dict["surname"] == user_surname
    assert user_to_dict["email"] == user_email


def test_find_by_id_handler_failed():
    repository = RepositoryInMemory()
    wrong_id = "wrong_id"
    find_by_id_handler = FindByIdHandler(repository)

    with pytest.raises(UserNotFoundException):
        find_by_id_handler.handle(wrong_id)
