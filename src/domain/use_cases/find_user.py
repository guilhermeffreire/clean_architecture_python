from typing import List, Dict
from abc import ABC, abstractmethod
from src.domain.models.users import Users


class FindUsers(ABC):

    @abstractmethod
    def find_by_id(self, user_id: int) -> Dict[bool, List[Users]]:
        raise Exception("Should implement method: find_by_id")

    @abstractmethod
    def find_all_users(self) -> Dict[bool, List[Users]]:
        raise Exception("Should implement method: find_all_users")
