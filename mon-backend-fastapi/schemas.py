from pydantic import BaseModel

class UserLogin(BaseModel):
    email: str
    password: str

class UserOut(BaseModel):
    user_id: int
    user_name: str
    user_firstname: str
    user_email: str
    user_phone: int
    user_adress: str

class Config:
    from_attributes = True
