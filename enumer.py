class User:
    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname


user_list = [
    User("sergio", "radigales"),
    User("nacho", "gonzalez"),
    User("carlos", "radigales"),
]


for x in enumerate(user_list):
    print(x)
    print(type(x))
    

