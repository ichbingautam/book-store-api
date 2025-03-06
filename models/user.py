from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    username: str
    role: str

class UserInDB(User):
    id: int
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str