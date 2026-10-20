from datetime import datetime

from pydantic import BaseModel


class PostResponse(BaseModel):
    id: int
    title: str
    created_at: datetime
    updated_at: datetime
