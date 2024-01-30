from fastapi import APIRouter
from src.adapter.spi.api.router.health_check_router import router as HealthCheck
from src.adapter.spi.api.router.order_router import router as OrderRouter


api_router = APIRouter()
api_router.include_router(HealthCheck, prefix='/health', tags=["healthCheck"])
api_router.include_router(OrderRouter, prefix='/orders', tags=["orders"])
