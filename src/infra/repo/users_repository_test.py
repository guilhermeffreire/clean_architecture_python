from faker import Faker
from src.infra.config import DBConnectionHandler
from .users_repository import UsersRepository

faker = Faker()
user_repository = UsersRepository()
db_connection_handler = DBConnectionHandler()


def test_insert_user():
    name = faker.name()
    password = faker.word()
    engine = db_connection_handler.get_engine()

    new_user = user_repository.insert_value(name, password)
    get_user = engine.execute(
        "SELECT * FROM users WHERE id= '{}';".format(new_user.id)
    ).fetchone()

    print("GET USER ", get_user)

    assert new_user.id == get_user.id
    assert new_user.name == get_user.name
    assert new_user.password == get_user.password
