from typing import Optional
from pydantic import BaseModel


class OrderSchema(BaseModel):
    
    product: str
    quantity: int
    total_amount: float
    