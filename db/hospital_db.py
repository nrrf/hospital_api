from sqlalchemy import Column, Integer, String, ForeignKey
from db.db_connection import Base, engine 

class HospitalInDB(Base): 
    __tablename__ = "hospital"
    
    idhospital = Column(Integer, primary_key=True, autoincrement=True)
    iduser = Column(String, ForeignKey("user.iduser"), unique= True) 
    nombre = Column(String)
    direccion = Column(String) 
    Serviciosmedicos = Column(String)
Base.metadata.create_all(bind=engine)