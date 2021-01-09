from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from db.db_connection import get_db
from db.user_db import UserInDB
from db.patient_db import PatientInDB
from db.hospital_db import HospitalInDB
from db.cita_db import CitaInDB
from models.cita_models import CitaRegistrationIn

router = APIRouter() 


@router.post("/user/cita/registration") 
async def register_cita(register_cita_in: CitaRegistrationIn, db:Session=Depends(get_db)): 
    hospital_in_db = db.query(HospitalInDB).get(register_cita_in.idhospital)
    patient_in_db = db.query(PatientInDB).get(register_cita_in.idpatient)

    
    if hospital_in_db == None or patient_in_db==None: 
        raise HTTPException(status_code=500, detail="Error no esperado en el sistema")

    
    cita_add =  CitaInDB(**register_cita_in.dict())
    db.add(cita_add)
    db.commit() 
    db.refresh(cita_add)
    

    return {"Cita Registrada":True}