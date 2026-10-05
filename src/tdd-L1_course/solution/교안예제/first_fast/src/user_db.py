import time


class UserDB:
    """진짜 DB 를 흉내 낸다 — 연결에 1초가 걸린다"""
    def connect(self):
        time.sleep(1)

    def get_name(self, user_id):
        return {1: "Hello"}[user_id]
