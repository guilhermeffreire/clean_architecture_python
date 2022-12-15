from src.main.interfaces import RoutesInterface
from src.presenters.controllers import RegisterUserController
from src.data.use_cases.register_user import RegisterUser
from src.infra.repo.users_repository import UsersRepository


def register_user_composer() -> RoutesInterface:
    repository = UsersRepository()
    use_case = RegisterUser(repository)
    register_user_route = RegisterUserController(use_case)

    return register_user_route
