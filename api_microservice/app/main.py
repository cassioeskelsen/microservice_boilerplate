from fastapi import FastAPI
from core.configs import Configuration as config
from core.logger import logger

from cadastre.api import cadastre_api_router
from reservations.api import reservations_api_router


logger.info(f"Starting {config.PROJECT_NAME}")
app = FastAPI(title=config.PROJECT_NAME,)

app.include_router(cadastre_api_router, prefix="/cadastre")
app.include_router(reservations_api_router , prefix="/reservation")
