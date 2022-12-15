from typing import List, Dict, Type
from src.domain.use_cases.find_pet import FindPet as FindPetInterface
from src.data.interfaces import IPetsRepository
from src.domain.models import Pets


class Find(FindPetInterface):
    def __init__(self, pet_repository: Type[IPetsRepository]):
        self.pet_repository = pet_repository

    def find_by_id(self, pet_id: int) -> Dict[bool, List[Pets]]:
        response = None

        validate_entry = isinstance(pet_id, int)

        if validate_entry:
            response = self.pet_repository.select_pet(pet_id=pet_id)

        return {"Success": validate_entry, "Data": response}

    def find_by_user_id(self, user_id: int) -> Dict[bool, List[Pets]]:
        response = None

        validate_entry = isinstance(user_id, int)

        if validate_entry:
            response = self.pet_repository.select_pet(user_id=user_id)

        return {"Success": validate_entry, "Data": response}

    def find_all_pets(self) -> Dict[bool, List[Pets]]:
        response = self.pet_repository.select_pet()

        data = True if response else False

        return {"Success": data, "Data": response}
