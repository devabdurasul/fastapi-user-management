from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Create an async engine
engine = create_async_engine(settings.DATABASE_URL, echo=True, connect_args={"check_same_thread": False})

# Create an async session factory
async_session = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


# Dependency to get the async session
async def get_db():
    async with async_session() as session:
        try:
            yield session
        finally:
            await session.close()
