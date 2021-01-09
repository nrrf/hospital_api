from sqlalchemy import Column, Integer, String, Date, ForeignKey
import datetime
from db.db_connection import Base, engine 

class PatientInDB(Base): 
    __tablename__ = "patient"
    
    idpatient = Column(Integer, primary_key=True, autoincrement=True)
    iduser = Column(String, ForeignKey("user.iduser"), unique= True) 
    nombre = Column(String)
    direccion = Column(String) 
    fecha_nacimiento = Column(String)
Base.metadata.create_all(bind=engine) 