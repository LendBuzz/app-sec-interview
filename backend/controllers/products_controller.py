from fastapi import APIRouter, Depends
from middlewares import get_current_user

router = APIRouter(prefix="/products", tags=["products"])

@router.get("/")
async def get_all_products(user: dict = Depends(get_current_user)):
    """
    Get all products for the authenticated user.
    """
    return {
        "products": [
            {"id": 1, "name": "Product 1", "price": 100.0},
            {"id": 2, "name": "Product 2", "price": 150.0},
            {"id": 3, "name": "Product 3", "price": 200.0}
        ]
    }
