from typing import Optional


class UpdateCommand:
    def __init__(self, username: Optional[str], refresh_token: Optional[str]) -> None:
        self._username = username
        self._refresh_token = refresh_token
