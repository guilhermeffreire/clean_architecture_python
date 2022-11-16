from .pets_repository import PetsRepository
from faker import Faker
from src.infra.config import DBConnectionHandler

faker = Faker()
pets_repository = PetsRepository()
db_connection_handler = DBConnectionHandler()


def test_insert_pets():
    name = faker.name()
    specie = "dog"
    age = faker.random_number(digits=1)
    user_id = faker.random_number()

    new_pet = pets_repository.insert_pet(name, specie, age, user_id)
    engine = db_connection_handler.get_engine()

    get_pet = engine.execute(
        "SELECT * FROM pets WHERE id= '{}';".format(new_pet.id)
    ).fetchone()

    assert new_pet.id == get_pet.id
    assert new_pet.user_id == get_pet.user_id
    assert new_pet.name == get_pet.name
    assert new_pet.specie == get_pet.specie
    assert new_pet.age == get_pet.age
