
from src.adapters.db.models.product import Product
from src.domain.entities.shift_task import ProductEntity


async def product_entity_to_model(product: ProductEntity):
    product_db = Product(
        unique_product_code=product.unique_product_code,
        batch_number=product.batch_number,
        batch_date=product.batch_date

    )
    return product_db
