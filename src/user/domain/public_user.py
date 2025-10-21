class PublicUser:
    def __init__(self, id: str, name: str, surname: str, email: str) -> None:
        self.id = id
        self.name = name
        self.surname = surname
        self.email = email

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "email": self.email,
        }
