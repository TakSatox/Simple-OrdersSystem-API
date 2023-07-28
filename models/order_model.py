from pydantic import BaseModel

class OrderModel(BaseModel):
    product: str
    quantity: int
    total_amount: float