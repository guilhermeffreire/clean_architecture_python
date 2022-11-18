from typing import Type, Dict
from src.domain.use_cases import RegisterUser as RegisterUserInterface
from src.data.interfaces import IUsersRepository as UsersRepository
from src.domain.models import Users


class RegisterUser(RegisterUserInterface):

    def __init__(self, user_repository: Type[UsersRepository]):
        self.user_repository = user_repository

    def register(self, name: str, password: str) -> Dict[bool, Users]:
        response = None
        validate_entry = isinstance(name, str) and isinstance(password, str)

        if validate_entry:
            response = self.user_repository.insert_user(name=name, password=password)

        return {"Success": validate_entry, "Data": response}

