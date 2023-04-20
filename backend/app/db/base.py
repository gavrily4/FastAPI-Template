from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from app.config import settings

engine = create_async_engine(
    settings.DB_URL,
    echo=True
)

async_session = async_sessionmaker(engine, expire_on_commit=False)


# create get session function for use as dependency
async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session


# import to db models as parent class
Base = declarative_base()

