from typing import Type, Dict, List
from src.data.use_cases.find_user import Find as FindUser
from src.data.interfaces import IPetsRepository as PetsRepository
from src.domain.use_cases import RegisterPet as RegisterPetInterface
from src.domain.models import Pets, Users


class RegisterPet(RegisterPetInterface):
    def __init__(self, pet_repository: [PetsRepository], find_user: Type[FindUser]):
        self.pet_repository = pet_repository
        self.find_user = find_user

    def registry(self, name: str, specie: str, user_information: Dict[int, str], age: int = None) -> Dict[bool, Pets]:
        response = None
        validate_entry = isinstance(name, str) and isinstance(specie, str)
        user = self.__find_user_information(user_information)
        checker = validate_entry and user["Success"]

        if checker:
            response = self.pet_repository.insert_pet(name, specie, age, user_information["user_id"])

        return {"Success": checker, "Data": response}

    def __find_user_information(self, user_information: Dict[int, str]) -> Dict[bool, List[Users]]:
        user_founded = None
        user_params = user_information.keys()

        if "user_id" in user_params:
            user_founded = self.find_user.find_by_id(user_information["user_id"])
        else:
            user_founded = self.find_user.find_all_users()

        if not user_founded:
            return {"Success": False, "Data": None}

        return user_founded
