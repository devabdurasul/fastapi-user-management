from fastapi import APIRouter
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTStrategy, AuthenticationBackend, BearerTransport
from app.auth.models import User
from app.auth.manager import get_user_manager
from app.auth.schemas import UserCreate, UserRead, UserUpdate
from app.core.config import settings


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=settings.SECRET, lifetime_seconds=3600)


bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

jwt_authentication = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy
)

# Initialize FastAPIUsers with the wrapped authentication backend
fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [jwt_authentication],
)

# Define the auth router and include all routes
router = APIRouter()

router.include_router(
    fastapi_users.get_auth_router(jwt_authentication),
    prefix="/auth/jwt",
    tags=["auth"]
)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"]
)
router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"]
)
