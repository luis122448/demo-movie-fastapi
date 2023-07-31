from fastapi import APIRouter
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from utils.jwt_manger import create_token

auth_router = APIRouter()

class User(BaseModel):
    email: str
    password: str

@auth_router.post('/auth/login', tags=["auth"], response_model=dict)
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "123456":
        token = create_token(user.dict())
        return JSONResponse(content={"token": token}, status_code=200)
    return JSONResponse(content={"message": "Unauthorized"}, status_code=401)