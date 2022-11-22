from abc import ABC, abstractmethod
from typing import Dict, List
from src.domain.models.pets import Pets


class FindPet(ABC):

    @abstractmethod
    def find_by_id(self, pet_id: int) -> Dict[bool, List[Pets]]:
        raise Exception("Should implement method: find_by_id")

    @abstractmethod
    def find_by_user_id(self, user_id: int) -> Dict[bool, List[Pets]]:
        raise Exception("Should implement method find_by_user_id")

    @abstractmethod
    def find_all_pets(self) -> Dict[bool, List[Pets]]:
        raise Exception("Should implement method find_all_pets")
