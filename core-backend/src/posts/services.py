from sqlalchemy import select, Sequence
from sqlalchemy.ext.asyncio import AsyncSession

from .models import Post


async def get_posts(*, db: AsyncSession) -> Sequence[Post]:
    statement = (
        select(Post)
        .order_by(Post.created_at.desc())
    )

    result = await db.scalars(statement)
    return result.all()
