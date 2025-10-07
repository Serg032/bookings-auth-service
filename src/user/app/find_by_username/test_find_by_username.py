from src.user.app.create.register_create import CreateHandler
from src.user.infrastructure.repository_in_memory import RepositoryInMemory
from src.user.domain.register_command import CreateCommand
from src.user.app.find_by_username.find_by_username_handler import FindByUsernameHandler


def test_when_asking_for_a_user_by_username_it_should_by_retrieve():
    repository = RepositoryInMemory()
    register_handler = CreateHandler(repository)
    username = "Jonh"
    register_command = CreateCommand(username, "123456")
    find_by_username_handler = FindByUsernameHandler(repository)

    register_handler.handle(register_command)
    user = find_by_username_handler.handle(username)
    not_found_user = find_by_username_handler.handle("Tim")

    assert user._username == username
    assert not_found_user is None


def test_when_asking_for_a_user_by_username_which_doesnt_exist_should_return_none():
    repository = RepositoryInMemory()
    find_by_username_handler = FindByUsernameHandler(repository)
    not_found_user = find_by_username_handler.handle("Tim")

    assert not_found_user is None
