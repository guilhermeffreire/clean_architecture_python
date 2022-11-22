from faker import Faker
from src.infra.test import PetRepositorySpy
from .find import Find

faker = Faker()


def test_find_by_id():
    pet_repo = PetRepositorySpy()
    find_pet = Find(pet_repo)

    attributes = {"pet_id": faker.random_number(digits=2)}
    response = find_pet.find_by_id(pet_id=attributes["pet_id"])

    # Testing inputs
    assert pet_repo.select_pet_params["pet_id"] == attributes["pet_id"]

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_find_by_user_id():
    pet_repo = PetRepositorySpy()
    find_pet = Find(pet_repo)

    attributes = {"user_id": faker.random_number(digits=2)}
    response = find_pet.find_by_user_id(user_id=attributes["user_id"])

    # Testing inputs
    assert pet_repo.select_pet_params["user_id"] == attributes["user_id"]

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_find_all_pets():
    pet_repo = PetRepositorySpy()
    find_pet = Find(pet_repo)

    response = find_pet.find_all_pets()

    assert response["Success"] is True
    assert response["Data"]


