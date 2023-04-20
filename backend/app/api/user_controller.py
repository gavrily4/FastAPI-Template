from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.base import get_session
from app.schemas.user import UserSchema, UserCreateSchema, UserUpdateSchema
from app.config import log
from app.repositories.user import UserRepository

user_router = APIRouter()


@user_router.get('/{user_id}', response_model=UserSchema)
async def get_user(user_id: int, session: AsyncSession = Depends(get_session)):
    user_repo = UserRepository()
    user = await user_repo.get_user_by_id(session, user_id)
    log.info(f'User with id {user_id} received successfully')
    return UserSchema(**user.__dict__)


@user_router.get('/', response_model=list[UserSchema])
async def get_users(
        session: AsyncSession = Depends(get_session),
        limit: int | None = None,
        offset: int | None = None
):
    user_repo = UserRepository()
    users = await user_repo.get_users(session, limit, offset)
    log.info(f'Users received successfully')
    return [UserSchema(**user.__dict__) for user in users]


@user_router.post('/', response_model=UserSchema)
async def create_user(
        user: UserCreateSchema,
        session: AsyncSession = Depends(get_session)
):
    user_repo = UserRepository()
    user = await user_repo.add_user(session, user)
    log.info(f'User created successfully')
    return UserSchema(**user.__dict__)


@user_router.put('/', response_model=UserSchema)
async def update_user(
        user: UserUpdateSchema,
        session: AsyncSession = Depends(get_session)
):
    user_repo = UserRepository()
    user = await user_repo.update_user(session, user)
    log.info(f'User updated successfully')
    return UserSchema(**user.__dict__)
