from src.user.app.create.register_create import CreateHandler
from src.user.app.update.update_handler import UpdateHandler
from src.user.domain.register_command import CreateCommand
from src.user.domain.update_command import UpdateCommand
from src.user.infrastructure.repository_in_memory import RepositoryInMemory


def test_update_username_handler():
    repository = RepositoryInMemory()
    create_handler = CreateHandler(repository)
    username = "John"
    password = "123456"
    create_command = CreateCommand(username, password)
    create_handler.handle(create_command)
    update_handler = UpdateHandler(repository)
