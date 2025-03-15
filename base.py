from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from configs import DATABASE_URL_ASYNC, DATABASE_URL_SYNC
from models import Base


engine_async_engine = create_async_engine(DATABASE_URL_ASYNC, echo=True)
async_session = sessionmaker(
    engine_async_engine, class_=AsyncSession, expire_on_commit=False
)

engine = create_engine(DATABASE_URL_SYNC, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


async def init_models() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session


# import asyncio
# import typer

# cli = typer.Typer()

# @cli.command()
# def db_init_models():
#     asyncio.run(init_models())
#     print("Done")

# cli()
