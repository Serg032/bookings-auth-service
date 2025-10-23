# from src.user.app.create.create_handler import CreateHandler
# from src.user.app.update.update_handler import UpdateHandler
# from src.user.domain.register_command import CreateCommand
# from src.user.domain.update_command import UpdateCommand
# from src.user.infrastructure.repository_in_memory import RepositoryInMemory


def test_update_username_handler():
    pass
    # repository = RepositoryInMemory()
    # create_handler = CreateHandler(repository)
    # user_name = "Jonh"
    # user_surname = "Doe"
    # user_email = "johndoe@test.com"
    # user_password = "123456"
    # command = CreateCommand(user_name, user_surname, user_email, user_password)
    # created_user = create_handler.handle(command)
    # update_handler = UpdateHandler(repository)

    # user_id = repository._users[0]._id

    # username_to_update = "Sergio"
    # command = UpdateCommand(username_to_update, None)

    # updated_public_user = update_handler.handle(user_id, command)

    # assert updated_public_user.id == created_user.id
    # assert updated_public_user.username == username_to_update
