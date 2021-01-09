from pydantic import BaseModel 
from datetime import date 


class CitaRegistrationIn(BaseModel): 
    idhospital : int
    idpatient : int
    fecha : date