from fastapi import APIRouter, Depends, HTTPException
from src.interactors.product_service import ProductService
from src.presentation.web_api.providers.abstract.product import product_service_provider
from src.presentation.web_api.schemas.shift_task import ProductSchema
from src.presentation.web_api.dependencies.depends_stub import Stub
product_router = APIRouter(
    tags=['product'],

)


@product_router.post('/tasks/product/add')
async def add_products(product: list[ProductSchema], product_service: ProductService = Depends(Stub(product_service_provider))):
    return await product_service.add_products(product)


@product_router.get('/tasks/product/aggregate')
async def aggregate_product(unique_product_code: str, batch_number: int,  product_service: ProductService = Depends(Stub(product_service_provider))):
    # проверка на наличие
    if not await product_service.is_product_exists(unique_product_code):
        raise HTTPException(
            status_code=404, detail="There are no products with this unique code")

    # проверка привязки к партии
    if not await product_service.is_product_bound_to_shift_task(unique_product_code, batch_number):
        raise HTTPException(
            status_code=400, detail="Unique code is attached to another batch")

    return await product_service.aggregate_product(unique_product_code, batch_number)
