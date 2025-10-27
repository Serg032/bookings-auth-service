from abc import ABC, abstractmethod


class Controller(ABC):
    @abstractmethod
    def execute(self, args: dict | None):
        pass
