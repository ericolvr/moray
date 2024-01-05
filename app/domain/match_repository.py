from abc import ABC, abstractmethod
from typing import List
from app.domain.match import Match


class MatchRepository(ABC):
    @abstractmethod
    def create(self, match: Match) -> Match:
        pass
    
    @abstractmethod
    def get_all(self) -> List[Match]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Match:
        pass
