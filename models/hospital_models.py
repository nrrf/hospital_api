from pydantic import BaseModel 
from datetime import date

class HospitalRegistrationIn(BaseModel):
    iduser : str
    nombre : str
    direccion : str
    Serviciosmedicos : str

class HospitalOut(BaseModel): 
    nombre: str 
    direccion: str 
    Serviciosmedicos: str 
    class Config:
        orm_mode = True