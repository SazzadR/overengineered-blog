from contextlib import asynccontextmanager

import anyio.to_thread
from fastapi import FastAPI, APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy import text
from sqlalchemy.orm import Session

from .database import get_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    limiter = anyio.to_thread.current_default_thread_limiter()
    limiter.total_tokens = 1

    yield


app = FastAPI(lifespan=lifespan)

v1_router = APIRouter(prefix="/api/v1")
app.include_router(v1_router)


@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    try:
        db.scalar(text("select 1 from (select pg_sleep(5)) as delay"))
    except Exception:
        print("RDBMS connection failed.")
        raise HTTPException(detail="Health check failed.", status_code=500)

    return JSONResponse(content={"status": "Ok."}, status_code=200)
