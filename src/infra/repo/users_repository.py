from collections import namedtuple
from src.infra.config import DBConnectionHandler
from src.infra.entities import Users


class UsersRepository:
    def insert_value(self, name: str, password: str) -> Users:

        insertData = namedtuple("Users", "id, name, password")

        with DBConnectionHandler() as db_connection:
            try:
                new_user = Users(name=name, password=password)
                db_connection.session.add(new_user)
                db_connection.session.commit()

                return insertData(new_user.id, new_user.name, new_user.password)
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None
