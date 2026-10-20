from typing import List, Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_db

from . import services as posts_service
from .schemas import PostResponse

router = APIRouter(
    prefix="/posts",
    tags=["posts"],
)

@router.get("/", response_model=list[PostResponse])
async def get_posts(db: Annotated[AsyncSession, Depends(get_db)]):
    posts = await posts_service.get_posts(db=db)

    return posts
