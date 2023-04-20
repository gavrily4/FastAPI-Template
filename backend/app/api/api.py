from fastapi import APIRouter

from app.api.auth_controller import auth_router
from app.api.user_controller import user_router

api_router = APIRouter(prefix="/v1")
api_router.include_router(auth_router, tags=["auth-controller"], prefix='/auth')
api_router.include_router(user_router, tags=['user-controller'], prefix='/users')
