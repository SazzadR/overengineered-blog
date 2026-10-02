from fastapi import FastAPI, APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy import text
from sqlalchemy.orm import Session

from .database import get_db

app = FastAPI()

v1_router = APIRouter(prefix="/api/v1")
app.include_router(v1_router)


@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    try:
        db.scalar(text("SELECT 1"))
    except Exception:
        print("RDBMS connection failed.")
        raise HTTPException(detail="Health check failed.", status_code=500)

    return JSONResponse(content={"status": "Ok."}, status_code=200)
