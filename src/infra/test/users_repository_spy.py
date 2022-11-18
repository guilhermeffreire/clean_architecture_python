from src.domain.models import Users
from src.domain.test import mock_users
from typing import List


class UserRepositorySpy:

    def __init__(self):
        self.insert_user_params = {}
        self.select_user_params = {}

    def insert_user(self, name: str, password: str) -> Users:
        self.insert_user_params["name"] = name
        self.insert_user_params["password"] = password

        return mock_users()

    def select_user(self, user_id: int = None) -> List[Users]:
        self.select_user_params["user_id"] = user_id

        return [mock_users()]

