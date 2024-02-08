import logging
from src.adapters.db.repositories.product_reposirtory import ProductRepository
from src.adapters.db.repositories.task_repositories import TaskRepository
from src.presentation.web_api.providers.abstract.product import product_service_provider
from src.interactors.product_service import ProductService
from src.presentation.web_api.providers.abstract.task import task_service_provider
from src.adapters.db.connection import get_session
from src.interactors.task_service import TaskService
from src.presentation.web_api.endpoints.task import task_router
from src.presentation.web_api.endpoints.product import product_router
from fastapi import FastAPI, Depends

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()],
)
app = FastAPI()

app.include_router(task_router)
app.include_router(product_router)


def get_task_repository(session=Depends(get_session)):
    return TaskRepository(session)


def get_product_repository(session=Depends(get_session)):
    return ProductRepository(session)


def get_task_service(task_repository=Depends(get_task_repository)):
    return TaskService(task_repository)


def get_product_service(product_repository=Depends(get_product_repository)):
    return ProductService(product_repository)


app.dependency_overrides[task_service_provider] = get_task_service
app.dependency_overrides[product_service_provider] = get_product_service
