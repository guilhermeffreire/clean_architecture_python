from faker import Faker
from src.infra.test import UserRepositorySpy
from .find import Find

faker = Faker()


def test_find_by_id():
    user_repo = UserRepositorySpy()
    find_user = Find(user_repo)

    attributes = {"id": faker.random_number(digits=2)}
    response = find_user.find_by_id(user_id=attributes["id"])

    # Testing inputs
    assert user_repo.select_user_params["user_id"] == attributes["id"]

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_find_all_users():
    user_repo = UserRepositorySpy()
    find_users = Find(user_repo)

    response = find_users.find_all_users()

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]
