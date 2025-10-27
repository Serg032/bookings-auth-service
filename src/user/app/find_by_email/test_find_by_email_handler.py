import uuid
from src.user.app.create.create_handler import CreateHandler
from src.user.domain.exceptions.user_not_found_exception import UserNotFoundException
from src.user.infrastructure.adapters.repository_in_memory import RepositoryInMemory
from src.user.app.create.create_command import CreateCommand
from src.user.app.find_by_email.find_by_email_handler import FindByEmailHandler


def test_when_asking_for_a_user_by_email_it_should_retrieve_the_user():
    repository = RepositoryInMemory()
    create_handler = CreateHandler(repository)
    id = uuid.uuid4()
    user_name = "Jonh"
    user_surname = "Doe"
    user_email = "johndoe@test.com"
    user_password = "12345678"
    command = CreateCommand(id, user_name, user_surname, user_email, user_password)

    create_handler.handle(command)

    find_by_email_handler = FindByEmailHandler(repository)

    user_by_email = find_by_email_handler.handle(user_email)

    assert user_email == user_by_email.email
    assert user_name == user_by_email.name
    assert user_surname == user_by_email.surname
    assert user_email == user_by_email.email


def test_when_asking_for_a_user_by_email_it_should_retrieve_a_exception_if_the_user_doesnt_exist():
    repository = RepositoryInMemory()
    handler = FindByEmailHandler(repository)

    user = handler.handle("wrong_email")

    assert user == None
