from faker import Faker
from src.infra.test import UserRepositorySpy


faker = Faker()


def test_find():
    # user_repo = User