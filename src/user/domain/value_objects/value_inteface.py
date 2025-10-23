from abc import ABC, abstractmethod


class ValueInterface(ABC):
    @abstractmethod
    def get_value(self):
        pass
