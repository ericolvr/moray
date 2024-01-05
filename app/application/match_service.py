from typing import List
from app.domain.match import Match
from app.domain.match_repository import MatchRepository


class MatchService:
    def __init__(self, repo: MatchRepository):
        self.repo = repo
    
    def create_match(self, match: Match) -> Match:
        return self.repo.create(match)

    def get_all_matches(self) -> List[Match]:
        return self.repo.get_all()
    
    def get_match_by_id(self, id: int) -> Match:
        return self.repo.get_by_id(id)
