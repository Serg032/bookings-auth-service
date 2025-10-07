from abc import ABC, abstractmethod
from typing import Optional
from src.user.domain.login_output import LoginOutput


class AuthAdapter(ABC):
    @abstractmethod
    def login(self, username: str, password: str) -> Optional[LoginOutput]:
        pass
