from fastapi import HTTPException
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import log
from app.models.user import User
from app.schemas.user import UserCreateSchema, UserUpdateSchema


class UserRepository:
    async def get_user_by_id(self, session: AsyncSession, user_id: int) -> User:
        query = select(User).where(User.id == user_id)
        result = await session.execute(query)
        log.info(f'Query "{query}" executed successfully')
        user = result.scalar()
        if user:
            return user
        raise HTTPException(status_code=404, detail=f'User with ID={user_id} not found')

    async def get_users(self, session: AsyncSession, limit: int = 10, offset: int = 0) -> list[User]:
        query = select(User).limit(limit).offset(offset)
        result = await session.execute(query)
        log.info(f'Query "{query}" executed successfully')
        users = result.scalars().all()
        return list(users)

    async def add_user(self, session: AsyncSession, user: UserCreateSchema) -> User:
        new_user = User(name=user.name)
        session.add(new_user)
        await session.commit()
        log.info(f'User "{new_user.name}" created in DB successfully')
        return new_user

    async def update_user(self, session: AsyncSession, user: UserUpdateSchema) -> User:
        query = update(User).where(User.id == user.id).values(name=user.name)
        await session.execute(query)
        await session.commit()
        log.info(f'Query "{query}" executed successfully')
        user = await self.get_user_by_id(session, user.id)
        return user



