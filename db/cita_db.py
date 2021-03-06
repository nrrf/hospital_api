from sqlalchemy import Column, Integer, String, ForeignKey, Date
from db.db_connection import Base, engine 

# Registro de citas medicas
class CitaInDB(Base): 
    __tablename__ = "cita"
    
    idcita = Column(Integer, primary_key=True, autoincrement=True)
    idhospital = Column(Integer, ForeignKey("hospital.idhospital"))
    idpatient = Column(Integer, ForeignKey("patient.idpatient"))
    fecha = Column(String)
Base.metadata.create_all(bind=engine)