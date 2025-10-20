import os
from dotenv import load_dotenv
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from src.user.app.create.register_create import CreateHandler
from src.user.app.find_by_id.find_by_id_handler import FindByIdHandler
from src.user.app.find_by_username.find_by_username_handler import FindByUsernameHandler
from src.user.app.update.update_handler import UpdateHandler
from src.user.domain.register_command import CreateCommand
from src.user.domain.update_command import UpdateCommand
from src.user.infrastructure.auth_adapter import JWTAuthAdapter
from src.user.infrastructure.postgres_repository import PostgresRepository
from src.user.infrastructure.bcrypt_password_hasher import BcryptPasswordHasher
from src.user.infrastructure.repository_in_memory import RepositoryInMemory
from src.user.domain.user_already_created_exception import UserAlreadyCreatedException
from src.user.domain.user_not_found_exception import UserNotFoundException

load_dotenv()


class RegisterBody(BaseModel):
    username: str
    password: str


class UpdateBody(BaseModel):
    username: str | None
    refresh_token: str | None


app = FastAPI()
users_tablename = os.getenv("USERS_TABLENAME", "users")


@app.post("/register", status_code=status.HTTP_201_CREATED)
async def register(body: RegisterBody):
    password_hasher = BcryptPasswordHasher()
    repository = PostgresRepository(users_tablename, password_hasher)
    auth_adapter = JWTAuthAdapter(repository, password_hasher)
    command = CreateCommand(body.username, body.password)
    register_handler = CreateHandler(repository)

    try:
        public_user = register_handler.handle(command)
    except UserAlreadyCreatedException as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    login_output = auth_adapter.login(body.username, body.password)

    return {
        "id": public_user.id,
        "username": public_user.username,
        "access_token": login_output._access_token,
    }


@app.get("/find-by-id/{id}")
async def find_by_id(id: str):
    try:
        repository = PostgresRepository(users_tablename, None)
        find_by_id_handler = FindByIdHandler(repository)
        return find_by_id_handler.handle(id)
    except UserNotFoundException as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc))
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        )


@app.get("/get-by-username/{username}")
async def get_by_username(username):
    try:
        repository = PostgresRepository(users_tablename, None)
        find_by_username_handler = FindByUsernameHandler(repository)
        return find_by_username_handler.handle(username)
    except UserNotFoundException as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc))
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        )


@app.put("/update/{id}")
async def update(id: str, body: UpdateBody):
    try:
        repository = PostgresRepository(users_tablename, None)
        update_handler = UpdateHandler(repository)
        update_command = UpdateCommand(body.username, body.refresh_token)
        return update_handler.handle(id, update_command)
    except UserNotFoundException as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc))
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        )
