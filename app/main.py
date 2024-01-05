from fastapi import FastAPI
from app.api.tournament import tournament_router
from app.api.competitor import competitor_router
from app.api.match import match_router
from app.api.result import result_router
from app.infra.db import Base, get_db, engine

app = FastAPI()

app.include_router(tournament_router)
app.include_router(competitor_router)
app.include_router(match_router)
app.include_router(result_router)


# TODO setup alembic
def create_tables():
    Base.metadata.create_all(bind=engine)


@app.on_event("startup")
async def startup_event():
    create_tables()

