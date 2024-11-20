from typing import Optional
from fastapi import Depends, Request
from fastapi_users import BaseUserManager
from app.auth.schemas import UserCreate, UserRead
from app.auth.db import get_user_db

SECRET = "SECRET"


class UserManager(BaseUserManager[UserCreate, UserRead]):
    user_db_model = UserRead
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: UserRead, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
            self, user: UserRead, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgotten their password. Reset token: {token}")

    async def on_after_request_verify(
            self, user: UserRead, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")

    def parse_id(self, user_id: str) -> int:
        return int(user_id)


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
