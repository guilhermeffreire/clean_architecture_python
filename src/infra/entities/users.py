from sqlalchemy import Column, String, Integer
from src.infra.config import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    # id_pet = relationship("pets")

    def __rep__(self):
        return f"User [name={self.name}]"
