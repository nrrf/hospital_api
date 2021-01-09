from pydantic import BaseModel 
from datetime import date

class PatientRegistrationIn(BaseModel):
    iduser : str
    nombre: str
    direccion : str
    fecha_nacimiento: str 

class PatientOut(BaseModel): 
    iduser : str
    email : str
    nombre: str 
    phone : str
    password: str
    direccion: str 
    fecha_nacimiento: str 
    class Config:
        orm_mode = True