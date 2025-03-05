from pydantic import BaseModel, Field 
from typing import Optional 

class ItemUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    price: Optional[float]


