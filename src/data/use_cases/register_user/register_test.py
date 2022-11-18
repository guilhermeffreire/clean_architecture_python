from faker import Faker
from .register import RegisterUser
from src.infra.test import UserRepositorySpy

faker = Faker()


def test_register():
    user_repo = UserRepositorySpy()
    register_user = RegisterUser(user_repo)

    attributes = {
        "name": faker.name(),
        "password": faker.name()
    }

    response = register_user.register(name=attributes["name"], password=attributes["password"])

    # Testing inputs
    assert user_repo.insert_user_params["name"] == attributes["name"]
    assert user_repo.insert_user_params["password"] == attributes["password"]

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_fail():
    user_repo = UserRepositorySpy()
    register_user = RegisterUser(user_repo)

    attributes = {
        "name": faker.random_number(digits=4),
        "password": faker.name()
    }

    response = register_user.register(name=attributes["name"], password=attributes["password"])

    # Testing inputs
    assert user_repo.insert_user_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None

