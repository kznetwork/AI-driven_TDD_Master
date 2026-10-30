class UserRepository:
    def __init__(self, users):
        self._users = dict(users)

    def find_by_id(self, user_id):
        return self._users.get(user_id)          # 없으면 None
