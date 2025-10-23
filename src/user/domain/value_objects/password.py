from src.user.domain.exceptions.password_minimun_len_exception import (
    PasswordMinimunLenException,
)
from src.user.domain.helpers.guard_password_well_formed import is_password_well_formed
from src.user.domain.value_objects.value_inteface import ValueInterface


class Password(ValueInterface):
    def __init__(self, value: str) -> None:
        if is_password_well_formed(value) == False:
            raise PasswordMinimunLenException()

        self._value = value

    def get_value(self) -> str:
        return self._value
