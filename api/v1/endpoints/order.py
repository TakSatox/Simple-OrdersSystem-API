from fastapi import APIRouter, HTTPException, status
from models.order_model import OrderModel
from schemas.order_schema import OrderSchema
from core.database import db



router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=OrderSchema)
def post_order(order: OrderSchema):
    new_order: OrderModel = OrderModel(product=order.product, quantity=order.quantity, total_amount=order.total_amount)

    try:
        db.collection('orders-test-project').add({'product': new_order.product, 'quantity': new_order.quantity, 'total_amount': new_order.total_amount})

        return new_order
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="The document wasn't added to the collection")