from fastapi import APIRouter

from .endpoints import movies

router = APIRouter()
router.include_router(movies.router, prefix="", tags=['Movies'])