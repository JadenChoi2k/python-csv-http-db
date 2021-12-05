from model.user.user import User


class UserRepository:
    __users: dict = {}
    seq = 0

    @staticmethod
    def create_user(user: User) -> User:
        if UserRepository.__users.get(user.user_id):
            return None
        else:
            UserRepository.seq += 1
            user.id = UserRepository.seq
            UserRepository.__users[user.id] = user
        return user

    @staticmethod
    def find_by_id(user_id: str) -> User:
        return UserRepository.__users.get(user_id)

    @staticmethod
    def find_all() -> list:
        return list(UserRepository.__users.values())
