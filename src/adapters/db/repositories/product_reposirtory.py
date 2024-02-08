from sqlalchemy import select
from abc import ABC, abstractmethod
from datetime import datetime
from src.adapters.db.models.product import Product
from src.adapters.db.repositories.converters.product import product_entity_to_model
from src.domain.entities.shift_task import ProductEntity
from sqlalchemy.ext.asyncio import AsyncSession


class ProductRepositoryInterface(ABC):
    @abstractmethod
    async def add_products(self, products: list[ProductEntity]):
        pass

    @abstractmethod
    async def aggregate_product(self, products: list[ProductEntity]):
        pass


class ProductRepository(ProductRepositoryInterface):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_products(self, products: list[ProductEntity]):
        for product in products:
            product_in_db = await product_entity_to_model(product)
            self.session.add(product_in_db)
        await self.session.commit()

    async def is_product_exists(self, unique_product_code: int):
        product = await self.session.execute(
            select(Product).where(
                Product.unique_product_code == unique_product_code)
        )

        return True if product.scalars().first() else False

    async def is_product_bound_to_shift_task(
        self, unique_product_code: int, batch_number: int
    ):
        product = await self.session.execute(
            select(Product)
            .where(Product.unique_product_code == unique_product_code)
            .where(Product.batch_number == batch_number)
        )
        return True if product.scalars().first() else False

    async def aggregate_product(self, unique_product_code: str, batch_number: int):
        query = await self.session.execute(
            select(Product)
            .where(Product.unique_product_code == unique_product_code)
            .where(Product.batch_number == batch_number)
        )
        product = query.scalars().first()

        if product.is_aggregated is True:
            return f"unique code already used at {product.aggregated_at}."
        else:
            product.is_aggregated = True
            product.aggregated_at = datetime.now()
            await self.session.commit()
            return f"unique code aggregated at {product.aggregated_at}."
