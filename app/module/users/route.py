from app.module.users.dto.model import Product
from fastapi import APIRouter as Router
router = Router()
@router.get("/")
async def read_root():
    return {"Hello": "World"}

@router.get("/")
async def read_root():
    return {"Hello": "World"}

products=[
    Product(id=1, name="Product 1", description="Description 1", price=10.0, quantity=100),
    Product(id=2, name="Product 2", description="Description 2", price=20.0, quantity=200),
    Product(id=3, name="Product 3", description="Description 3", price=30.0, quantity=300),
    Product(id=4, name="Product 4", description="Description 4", price=40.0, quantity=400),
    Product(id=5, name="Product 5", description="Description 5", price=50.0, quantity=500),
]
@router.get("/products")
async def read_products():
    return products

@router.get("/products/{product_id}")
async def read_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    return {"error": "Product not found"}

@router.post("/products")
async def create_product(product: Product):
    products.append(product)
    return product