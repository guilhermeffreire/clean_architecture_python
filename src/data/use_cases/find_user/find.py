from typing import Type, Dict, List
from src.domain.use_cases.find_user import FindUsers as FindUsersInterface
from src.data.interfaces import IUsersRepository
from src.domain.models import Users


class Find(FindUsersInterface):
    def __init__(self, user_repository: Type[IUsersRepository]):
        self.user_repository = user_repository

    def find_by_id(self, user_id: int) -> Dict[bool, List[Users]]:
        response = None
        validate_entry = isinstance(user_id, int)

        if validate_entry:
            response = self.user_repository.select_user(user_id=user_id)

        return {"Success": validate_entry, "Data": response}

    def find_all_users(self) -> Dict[bool, List[Users]]:
        response = self.user_repository.select_user()

        return {"Success": True, "Data": response}
