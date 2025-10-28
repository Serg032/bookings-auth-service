from typing import Optional, TypedDict


class UpdateCommandType(TypedDict):
    id: str
    name: Optional[str]
    surname: Optional[str]
    email: Optional[str]
    refresh_token: Optional[str]


class UpdateCommand:
    def __init__(self, args: UpdateCommandType) -> None:
        self._id = args["id"]
        self._name = args["name"]
        self._surname = args["surname"]
        self._email = args["email"]
        self._refresh_token = args["refresh_token"]
