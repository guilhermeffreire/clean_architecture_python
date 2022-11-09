from src.infra.entities import Pets
from src.infra.config import DBConnectionHandler


class PetsRepository:
    @classmethod
    def insert_value(self, name: str, specie: str, age: int, user_id: str) -> Pets:

        with DBConnectionHandler() as db_connection:
            try:
                new_pet = Pets(name=name, specie=specie, age=age, user_id=user_id)
                db_connection.session.add(new_pet)
                db_connection.session.commit()

            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None
