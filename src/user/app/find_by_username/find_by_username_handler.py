from typing import Optional
from src.user.domain.repository_interface import Repository
from src.user.domain.entities.entity import User


class FindByUsernameHandler:
    def __init__(self, repository: Repository) -> None:
        self._repository = repository

    def handle(self, username: str) -> Optional[User]:
        # is already created by username
        return self._repository.find_by_username(username)
