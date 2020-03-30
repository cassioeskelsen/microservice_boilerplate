from fastapi import FastAPI
from core.configs import Configuration as config
from core.logger import logger

from api_v1.api import api_router

logger.info(f"Starting {config.PROJECT_NAME}")
app = FastAPI(title=config.PROJECT_NAME,)

app.include_router(api_router, prefix=f"/{config.PROJECT_NAME}")
