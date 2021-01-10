from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from db.db_connection import get_db
from db.user_db import UserInDB
from db.patient_db import PatientInDB
from db.hospital_db import HospitalInDB
from db.cita_db import CitaInDB
from models.cita_models import CitaRegistrationIn, CitaRegistration

router = APIRouter() 


@router.post("/user/cita/registration") 
async def register_cita(register_cita_in: CitaRegistrationIn, db:Session=Depends(get_db)): 
    # Verificacion (no por el id de la base de datos) sino con la de usuario
    hospital_in_db = db.query(HospitalInDB).filter(HospitalInDB.iduser==register_cita_in.iduserhospital).first()
    patient_in_db = db.query(PatientInDB).filter(PatientInDB.iduser==register_cita_in.iduserpatient).first()

    
    if hospital_in_db == None or patient_in_db==None: 
        raise HTTPException(status_code=500, detail="El medico o el paciente no estan registrados")

    
    cita_add =  CitaInDB(idhospital=hospital_in_db.idhospital, idpatient=patient_in_db.idpatient , fecha=register_cita_in.fecha)
    db.add(cita_add)
    db.commit() 
    db.refresh(cita_add)
    
    return {"Cita Registrada":True}