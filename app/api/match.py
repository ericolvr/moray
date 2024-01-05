from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.domain.match import Match
from app.application.match_service import MatchService
from app.infra.mysql_match_repository import MySQLMatchRepository
from app.infra.db import get_db


match_router = APIRouter(
    prefix="/matches"
)


def get_match_service(db: Session = Depends(get_db)) -> MatchService:
    return MatchService(MySQLMatchRepository(db))


@match_router.post("/")
def create_match(
    match: Match, 
    service: MatchService = Depends(get_match_service)
):
    return service.create_match(match)


@match_router.get("/")
def get_all_matches(service: MatchService = Depends(get_match_service)):
    return service.get_all_matches()


@match_router.get("/{id}")
def get_match_by_id(
    id: int, 
    service: MatchService = Depends(get_match_service)
):
    return service.get_match_by_id(id)