from fastapi import FastAPI
from app.auth.routes import router as auth_router
from app.db.base import Base
from app.db.session import engine
from contextlib import asynccontextmanager


# Define the lifespan context to handle startup and shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code: create tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield  # This separates startup and shutdown code
    # Shutdown code (optional cleanup can be done here)

# Initialize FastAPI with the lifespan context
app = FastAPI(docs_url='/', lifespan=lifespan)

# Include the authentication router
app.include_router(auth_router)

if __name__ == "__main__":
    import uvicorn

    # Run the app using uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
