from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Pets


class IPetsRepository(ABC):
    @staticmethod
    @abstractmethod
    def insert_pet(self,  name: str, specie: str, age: int, user_id: str) -> Pets:
        raise Exception("Method not implemented")

    @staticmethod
    @abstractmethod
    def select_pet(self, pet_id: int, user_id: int) -> List[Pets]:
        raise Exception("Method not implemented")

