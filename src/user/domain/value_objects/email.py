from src.user.domain.exceptions.email_not_well_formed_exception import (
    EmailNotWellFormedException,
)

from src.user.domain.helpers.guard_email_well_formed import is_mail_well_formed
from src.user.domain.value_objects.value_inteface import ValueInterface


class Email(ValueInterface):
    def __init__(self, value: str) -> None:
        well_formed = is_mail_well_formed(value)

        if well_formed is False:
            raise EmailNotWellFormedException(f"Email {value} is not well formed")

        self._value = value

    def get_value(self) -> str:
        return self._value
