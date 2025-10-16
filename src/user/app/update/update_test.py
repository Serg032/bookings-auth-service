from src.user.app.create.register_create import CreateHandler
from src.user.app.update.update_handler import UpdateHandler
from src.user.domain.register_command import CreateCommand
from src.user.domain.update_command import UpdateCommand
from src.user.infrastructure.repository_in_memory import RepositoryInMemory


def test_update_username_handler():
    repository = RepositoryInMemory()
    register_handler = CreateHandler(repository)
    update_handler = UpdateHandler(repository)
    username = "Jonh"
    password = "123456"
    command = CreateCommand(username, password)
    register_handler.handle(command)
    user_to_update = repository.find_by_username("Jonh")
    update_username_command = UpdateCommand("Wilfred", None)
    update_result = update_handler.handle(user_to_update._id, update_username_command)

    assert update_result is not None
    assert update_result.username == "Wilfred"


def test_update_refresh_token_handler():
    repository = RepositoryInMemory()
    register_handler = CreateHandler(repository)
    update_handler = UpdateHandler(repository)
    username = "Jonh"
    password = "123456"
    refresh_token = "refresh_token"
    command = CreateCommand(username, password)
    register_handler.handle(command)
    user_to_update = repository.find_by_username("Jonh")
    update_username_command = UpdateCommand(None, refresh_token)
    update_result = update_handler.handle(user_to_update._id, update_username_command)
    updated_user = repository.find_by_username("Jonh")

    assert update_result is not None
    assert update_result.username == "Jonh"
    assert updated_user._refresh_token == refresh_token


def test_update_all_handler():
    repository = RepositoryInMemory()
    register_handler = CreateHandler(repository)
    update_handler = UpdateHandler(repository)
    username = "Jonh"
    password = "123456"
    refresh_token = "refresh_token"
    command = CreateCommand(username, password)
    register_handler.handle(command)
    user_to_update = repository.find_by_username("Jonh")
    update_username_command = UpdateCommand("Wilfred", refresh_token)
    update_result = update_handler.handle(user_to_update._id, update_username_command)
    updated_user = repository.find_by_username("Wilfred")

    assert update_result is not None
    assert update_result.username == "Wilfred"
    assert updated_user._refresh_token == refresh_token


def test_update_username():
    repository = RepositoryInMemory()
    register_handler = CreateHandler(repository)
    username = "Jonh"
    password = "123456"
    command = CreateCommand(username, password)
    a = register_handler.handle(command)
    print(f"Public USER {a} {a.username}")
    update_handler = UpdateHandler(repository)
    t = update_handler.handle()

