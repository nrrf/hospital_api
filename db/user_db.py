from sqlalchemy import Column, Integer, String
from db.db_connection import Base, engine

class UserInDB(Base): 
    __tablename__ = "user"

    iduser = Column(String, primary_key= True, unique=True)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    password = Column(String, nullable=False)
Base.metadata.create_all(bind=engine)