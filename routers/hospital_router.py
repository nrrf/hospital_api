from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from db.db_connection import get_db
from db.user_db import UserInDB
from db.patient_db import PatientInDB
from db.hospital_db import HospitalInDB
from models.hospital_models import HospitalRegistrationIn

router = APIRouter() 


@router.post("/user/hospital/registration")
async def register_hospital(register_hospital_in: HospitalRegistrationIn, db:Session=Depends(get_db)): 
    user_in_db = db.query(UserInDB).get(register_hospital_in.iduser)
    
    if user_in_db == None: 
        raise HTTPException(status_code=500, detail="Error no esperado en el sistema")

    
    hospital_add =  HospitalInDB(**register_hospital_in.dict())
    db.add(hospital_add)
    db.commit() 
    db.refresh(hospital_add)
    

    return {"Registrado Hospital":True}


@router.get("/user/hospital/{userid}")
async def user_information(userid: str, db:Session=Depends(get_db)): 
    hospital_in_db = db.query(UserInDB,HospitalInDB).join(HospitalInDB, UserInDB.iduser==HospitalInDB.iduser).filter(UserInDB.iduser==userid).first()
    #print(type(patient_in_db))
    return hospital_in_db