from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.domain.competitor import Competitor
from app.application.competitor_service import CompetitorService
from app.infra.mysql_competitor_repository import MySQLCompetitorRepository
from app.infra.db import get_db


competitor_router = APIRouter(
    prefix="/competitors"
)


def get_competitor_service(db: Session = Depends(get_db)) -> CompetitorService:
    return CompetitorService(MySQLCompetitorRepository(db))


@competitor_router.post("/")
def create_competitor(
    competitor: Competitor, 
    service: CompetitorService = Depends(get_competitor_service)
):
    return service.create_competitor(competitor)


@competitor_router.get("/{tournament_id}")
def get_all_competitors(
    tournament_id: int,
    service: CompetitorService = Depends(get_competitor_service)
):
    return service.get_all_competitors(tournament_id)


@competitor_router.get("/{id}")
def get_competitor_by_id(
    id: int, 
    service: CompetitorService = Depends(get_competitor_service)
):
    return service.get_competitor_by_id(id)