from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class User(BaseModel):
    username: str = Field(..., description="Username of the user")
    email: EmailStr
    password : str = Field(..., description="Password of the user")
    age: int = Field(..., description="Age of the user")
    is_active: bool = Field(default=True, description="Indicates if the user is active")