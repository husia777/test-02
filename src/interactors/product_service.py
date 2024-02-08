from src.domain.entities.shift_task import ProductEntity


class ProductService:
    def __init__(self, product_repository):
        self.product_repository = product_repository

    async def add_products(self, product: list[ProductEntity]):
        return await self.product_repository.add_products(product)

    async def is_product_bound_to_shift_task(self, unique_product_code: int, batch_number: int):
        return await self.product_repository.is_product_bound_to_shift_task(unique_product_code, batch_number)

    async def is_product_exists(self, unique_product_code: int):
        return await self.product_repository.is_product_exists(unique_product_code)

    async def aggregate_product(self, unique_product_code: str, batch_number: int):
        return await self.product_repository.aggregate_product(unique_product_code, batch_number)
