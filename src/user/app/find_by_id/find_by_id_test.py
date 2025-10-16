import pytest
from src.user.app.create.register_create import CreateHandler
from src.user.app.find_by_id.find_by_id_handler import FindByIdHandler
from src.user.domain.register_command import CreateCommand
from src.user.domain.user_not_found_exception import UserNotFoundException
from src.user.infrastructure.repository_in_memory import RepositoryInMemory


def test_find_by_id_handler_successfull():
    repository = RepositoryInMemory()
    create_handler = CreateHandler(repository)

    username = "John"
    password = "123456"

    create_command = CreateCommand(username, password)
    create_handler.handle(create_command)

    user_id = repository._users[0]._id
    find_by_id_handler = FindByIdHandler(repository)
    user = find_by_id_handler.handle(user_id)

    user_to_dict = user.to_dict()

    assert user_to_dict["id"] == user_id
    assert user_to_dict["username"] == username


def test_find_by_id_handler_failed():
    repository = RepositoryInMemory()
    wrong_id = "wrong_id"
    find_by_id_handler = FindByIdHandler(repository)

    with pytest.raises(UserNotFoundException):
        find_by_id_handler.handle(wrong_id)
