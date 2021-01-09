from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from db.db_connection import get_db
from db.user_db import UserInDB
from db.patient_db import PatientInDB
from db.hospital_db import HospitalInDB
from models.patient_models import PatientRegistrationIn, PatientOut

router = APIRouter() 

@router.post("/user/patient/registration")
async def register_patient(register_patient_in: PatientRegistrationIn, db:Session=Depends(get_db)): 
    user_in_db = db.query(UserInDB).get(register_patient_in.iduser)
    
    if user_in_db == None: 
        raise HTTPException(status_code=500, detail="Error no esperado en el sistema")

    
    patient_add =  PatientInDB(**register_patient_in.dict())
    db.add(patient_add)
    db.commit() 
    db.refresh(patient_add)
    

    return {"Registrado Paciente":True}
    
    
@router.get("/user/patient/{userid}")
async def user_information(userid: str, db:Session=Depends(get_db)): 
    patient_in_db = db.query(UserInDB,PatientInDB).join(PatientInDB, UserInDB.iduser==PatientInDB.iduser).filter(UserInDB.iduser==userid).first()
    #print(type(patient_in_db))
    return patient_in_db