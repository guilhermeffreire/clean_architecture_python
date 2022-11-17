from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Users


class IUsersRepository(ABC):
    def insert_user(self, name: str, password: str) -> Users:
        raise Exception("Method not implemented")

    def select_user(self, user_id: int = None) -> List[Users]:
        raise Exception("Method not implemented")

