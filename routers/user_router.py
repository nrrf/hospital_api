from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from db.db_connection import get_db
from db.user_db import UserInDB
from db.patient_db import PatientInDB
from db.hospital_db import HospitalInDB
from models.user_models import UserRegistrationIn, UserIn, NewUserPassword

router = APIRouter() 

@router.post("/user/registration")
async def register_user(register_in: UserRegistrationIn, db:Session=Depends(get_db)): 
    user_in_db = db.query(UserInDB).get(register_in.iduser)
    
    if user_in_db != None: 
        raise HTTPException(status_code=404, detail="El usuario ya se encuentra registrado")
    if len(register_in.password)<8: 
        raise HTTPException(status_code=403, detail="Password demasiado corto")

    # obviamente habrian mas restricciones en las q posiblemente se necesite usar regex o metodos similares
    user_add =  UserInDB(**register_in.dict())
    db.add(user_add)
    db.commit() 
    db.refresh(user_add)
    

    return {"Registrado Usuario":True}


@router.post("/user/login")
async def login_user(user_in: UserIn , db:Session=Depends(get_db)): 
    user_in_db = db.query(UserInDB).get(user_in.iduser) 

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El cliente no existe")
    if user_in_db.password != user_in.password:
        raise HTTPException(status_code=403, detail="El password no es correcto")
    return {"Autenticado Usuario": True}

@router.put("/user/changepassword")
async def changepassword(user_in:NewUserPassword, db:Session=Depends(get_db)): 
    user_in_db = db.query(UserInDB).get(user_in.iduser) 

    if user_in_db == None: 
        raise HTTPException(status_code=500, detail="Error del sistema, intentelo mas tarde")
    if user_in_db.password != user_in.password:
        raise HTTPException(status_code=403, detail="El password no es correcto")
    if len(user_in.newpassword)<8: 
        raise HTTPException(status_code=403, detail="New password demasiado corto") 

    user_in_db.password=user_in.newpassword
    
    db.commit() 
    db.refresh(user_in_db)

    return {"Cambio Contraseña":True}
