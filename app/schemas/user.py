from pydantic import BaseModel, EmailStr

class UserBases(BaseModel):
    email: EmailStr
class UserCreate(UserBases):
    password: str
class User(UserBases):
    id: int
    is_active: bool

    class Config:
        from_attributes = True