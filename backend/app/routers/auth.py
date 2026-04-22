from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.user import UserCreate, UserLogin, UserResponse
from app.services.auth_service import create_user, authenticate_user
from app.core.dependencies import get_db
from app.core.security import create_access_token

router = APIRouter()

@router.post("/register", response_model=UserResponse)
async def register(user_in: UserCreate, db: AsyncSession = Depends(get_db)):
    return await create_user(db, user_in)

@router.post("/login")
async def login(user_in: UserLogin, db: AsyncSession = Depends(get_db)):
    user = await authenticate_user(db, user_in.email, user_in.password)
    token = create_access_token(user.id)
    return {"access_token": token, "token_type": "bearer"}