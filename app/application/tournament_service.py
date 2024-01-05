from typing import List
from app.domain.tournament import Tournament
from app.domain.tournament_repository import TournamentRepository


class TournamentService:
    def __init__(self, repo: TournamentRepository):
        self.repo = repo
    
    def create_tournament(self, tournament: Tournament) -> Tournament:
        return self.repo.create(tournament)

    def get_all_tournaments(self) -> List[Tournament]:
        return self.repo.get_all()
    
    def get_tournament_by_id(self, id: int) -> Tournament:
        return self.repo.get_by_id(id)
