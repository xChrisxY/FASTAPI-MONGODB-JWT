from pydantic import BaseModel, Field
from typing import Optional

class Item(BaseModel):
    name: str = Field(..., description="Name of the item")
    description : Optional[str] = Field(None, description="Description of the item")
    price : float = Field(..., ge=0, description="Price of the item")
