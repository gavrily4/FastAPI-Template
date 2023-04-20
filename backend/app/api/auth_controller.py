from fastapi import APIRouter

from app.schemas.auth import LoginModel, TokenModel
from app.config import log

auth_router = APIRouter()


@auth_router.post('/login', response_model=TokenModel)
async def login(login_data: LoginModel):
    token_model = TokenModel(access_token='jfdljs;', refresh_token='fjdljfldj')
    return token_model
