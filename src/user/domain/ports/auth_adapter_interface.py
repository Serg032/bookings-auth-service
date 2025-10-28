from abc import ABC, abstractmethod
from typing import Optional
from src.user.app.auth.login.login_output import LoginOutput


class AuthAdapter(ABC):
    @abstractmethod
    def login(self, email: str, password: str) -> Optional[LoginOutput]:
        pass
