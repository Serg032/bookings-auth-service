import os
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from src.user.app.auth.login.login_handler import LoginHandler
from src.user.app.create.create_handler import CreateHandler
from src.user.app.find_by_email.find_by_email_handler import FindByEmailHandler
from src.user.domain.exceptions.email_not_well_formed_exception import (
    EmailNotWellFormedException,
)
from src.user.domain.exceptions.password_minimun_len_exception import (
    PasswordMinimunLenException,
)
from src.user.domain.exceptions.wrong_login import WrongLoginException
from src.user.infrastructure.adapters.bcrypt_password_hasher import BcryptPasswordHasher
from src.user.infrastructure.adapters.jwt_auth_adapter import JWTAuthAdapter
from src.user.infrastructure.controllers.create_controller import CreateController
from src.user.infrastructure.controllers.find_by_email_controller import (
    FindByEmailController,
)
from src.user.infrastructure.adapters.postgres_repository import PostgresRepository
from src.user.domain.exceptions.user_already_created_exception import (
    UserAlreadyCreatedException,
)
from fastapi import HTTPException

load_dotenv()


class RegisterBody(BaseModel):
    id: str
    name: str
    surname: str
    email: str
    password: str


class UpdateBody(BaseModel):
    username: str | None
    refresh_token: str | None


app = FastAPI()
users_tablename = os.getenv("USERS_TABLENAME", "users")


@app.post("/register")
async def controller(body: RegisterBody):
    try:
        # Is email already registered?
        password_hasher = BcryptPasswordHasher()
        repository = PostgresRepository(users_tablename, password_hasher)
        find_by_email_handler = FindByEmailHandler(repository)
        find_by_email_controller = FindByEmailController(find_by_email_handler)
        command = body.model_dump()

        user_by_email = find_by_email_controller.execute(command)

        if user_by_email is not None:
            raise UserAlreadyCreatedException(
                f"User with email {body.email} already registered"
            )

        # Create User
        create_handler = CreateHandler(repository)
        create_controller = CreateController(create_handler)

        create_controller.execute(command)

        # Logging
        auth_adapter = JWTAuthAdapter(repository, password_hasher)
        login_handler = LoginHandler(auth_adapter)

        login_output = login_handler.handle(command["email"], command["password"])

        if login_output is None:
            raise WrongLoginException()

        # TODO Update user with refresh token

        return {
            "succesfull-message": "going well",
            "login-output": login_output.to_dict(),
        }

    except UserAlreadyCreatedException as e:
        raise HTTPException(status_code=409, detail=str(e))

    except EmailNotWellFormedException as e:
        raise HTTPException(status_code=409, detail=str(e))

    except PasswordMinimunLenException as e:
        raise HTTPException(status_code=409, detail=str(e))

    except WrongLoginException as e:
        raise HTTPException(status_code=409, detail=str(e))
