from typing import Dict
from src.domain.models import Pets
from abc import ABC, abstractmethod


class RegisterPet(ABC):
    @abstractmethod
    def registry(
        self, name: str, specie: str, user_information: Dict[int, str], age: int = None
    ) -> Dict[bool, Pets]:
        raise Exception("Should implement method: registry")
