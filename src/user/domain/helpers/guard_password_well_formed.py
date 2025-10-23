def is_password_well_formed(password: str) -> bool:
    if len(password) < 9:
        return False

    return True
