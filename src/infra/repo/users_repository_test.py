from faker import Faker
from src.infra.config import DBConnectionHandler
from .users_repository import UsersRepository

faker = Faker()
users_repository = UsersRepository()
db_connection_handler = DBConnectionHandler()


def test_insert_users():
    name = faker.name()
    password = faker.word()
    engine = db_connection_handler.get_engine()

    new_user = users_repository.insert_value(name, password)
    get_user = engine.execute(
        "SELECT id, name, password FROM users WHERE id= '{}';".format(new_user.id)
    ).fetchone()

    assert new_user.id == get_user.id
    assert new_user.name == get_user.name
    assert new_user.password == get_user.password


def test_select_one_user():
    id = 1

    user = users_repository.select_user(id)

    print(user)
