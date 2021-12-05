class User:
    id: int = None
    user_id: str = None
    password: str = None
    name: str = None

    def __init__(self, id, user_id, password, name):
        self.id = id
        self.user_id = user_id
        self.password = password
        self.name = name

    def __str__(self):
        return f'user_id : {self.user_id} name : {self.name}'
