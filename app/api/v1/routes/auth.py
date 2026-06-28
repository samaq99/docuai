from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.core.security import hash_password, verify_password, create_access_token

class RegisterRequest(BaseModel):
    username: str
    password: str

class LoginRequest(BaseModel):
    username: str
    password: str

router = APIRouter()
users_db: dict = {}

@router.post('/register')
def register(body: RegisterRequest)->dict:
    if body.username in users_db:
        raise HTTPException(status_code=400, detail="User already exist")
    users_db[body.username] = hash_password(body.password)
    return {"message": "User registered"}

@router.post("/login")
def login(body: LoginRequest):
    hashed = users_db.get(body.username)
    if not hashed or not verify_password(body.password, hashed):
        raise HTTPException(status_code=401, detail="Error in username/password")
    token = create_access_token({"sub": body.username})
    return {"access_token":token, "token_type": "bearer"}
        