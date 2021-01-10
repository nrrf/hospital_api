from pydantic import BaseModel 
from datetime import date 


class CitaRegistrationIn(BaseModel): 
    iduserhospital : str
    iduserpatient : str
    fecha : str

class CitaRegistration(BaseModel): 
    idhospital: int 
    idpatient: str 
    fecha: str