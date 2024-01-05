from typing import List
from app.domain.competitor import Competitor
from app.domain.competitor_repository import CompetitorRepository


class CompetitorService:
    def __init__(self, repo: CompetitorRepository):
        self.repo = repo
    
    def create_competitor(self, competitor: Competitor) -> Competitor:
        return self.repo.create(competitor)

    def get_all_competitors(self, tournament_id: int) -> List[Competitor]:
        return self.repo.get_all(tournament_id)
    
    def get_competitor_by_id(self, id: int) -> Competitor:
        return self.repo.get_by_id(id)
