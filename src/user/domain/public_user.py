class PublicUser:
    def __init__(self, id: str, username: str) -> None:
        self.id = id
        self.username = username

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
        }
