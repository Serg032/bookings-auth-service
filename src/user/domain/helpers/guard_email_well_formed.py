import re

EMAIL_REGEX_PERMISSIVE = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")


def is_mail_well_formed(email: str) -> bool:
    return bool(EMAIL_REGEX_PERMISSIVE.fullmatch(email))
