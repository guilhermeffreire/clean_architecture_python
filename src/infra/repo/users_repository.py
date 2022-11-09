from typing import List
from src.infra.config import DBConnectionHandler
from src.infra.entities import Users as UsersModel
from src.domain.models import Users


class UsersRepository:
    @classmethod
    def insert_value(cls, name: str, password: str) -> Users:

        with DBConnectionHandler() as db_connection:
            try:
                new_user = UsersModel(name=name, password=password)
                db_connection.session.add(new_user)
                db_connection.session.commit()

                return Users(new_user.id, new_user.name, new_user.password)
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None

    @classmethod
    def select_user(cls, user_id: int = None) -> List[Users]:

        try:
            result = None

            if user_id:
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(UsersModel)
                        .filter_by(id=user_id)
                        .one()
                    )
                    result = [data]
            else:
                with DBConnectionHandler as db_connection:
                    data = db_connection.session.query(UsersModel).all()
                    result = [data]

            return result

        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()

        return None
