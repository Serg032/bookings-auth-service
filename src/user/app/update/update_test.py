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
    created_user = create_handler.handle(create_command)
    update_handler = UpdateHandler(repository)

    user_id = repository._users[0]._id

    username_to_update = "Sergio"
    command = UpdateCommand(username_to_update, None)

    updated_public_user = update_handler.handle(user_id, command)

    assert updated_public_user.id == created_user.id
    assert updated_public_user.username == username_to_update
