from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.models import TimeStampModel


class Post(TimeStampModel):
    __tablename__ = "posts_post"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
