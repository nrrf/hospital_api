from fastapi import FastAPI, Depends
from fastapi import HTTPException

from routers.hospital_router import router as router_hospital
from routers.user_router import router as router_user
from routers.patient_router import router as router_patient 
from routers.cita_router import router as router_cita
from fastapi.middleware.cors import CORSMiddleware

api = FastAPI() 

origins = [
"http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
"http://localhost", "http://localhost:8080"
] 
api.add_middleware(
CORSMiddleware, allow_origins=origins,
allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

api.include_router(router_user)
api.include_router(router_patient)
api.include_router(router_hospital)
api.include_router(router_cita)