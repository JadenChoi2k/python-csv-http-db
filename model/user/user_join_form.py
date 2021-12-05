class UserJoinForm:
    userid: str = None
    password: str = None
    name: str = None

    def __init__(self, userid=None, password=None, name=None):
        self.userid = userid
        self.password = password
        self.name = name

