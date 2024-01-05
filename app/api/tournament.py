from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.domain.tournament import Tournament
from app.application.tournament_service import TournamentService
from app.infra.repositories.tournament_repository import TournamentRepository
from app.infra.db import get_db

tournament_router = APIRouter(
    prefix="/tournaments",
)


def get_tournament_service(db: Session = Depends(get_db)) -> TournamentService:
    return TournamentService(TournamentRepository(db))


@tournament_router.post("/")
def create_tournament(
    tournament: Tournament, 
    service: TournamentService = Depends(get_tournament_service)
):
    return service.create_tournament(tournament)


@tournament_router.get("/")
def get_all_tournaments(service: TournamentService = Depends(get_tournament_service)):
    return service.get_all_tournaments()


@tournament_router.get("/{id}")
def get_tournament_by_id(
    id: int, 
    service: TournamentService = Depends(get_tournament_service)
):
    return service.get_tournament_by_id(id)


