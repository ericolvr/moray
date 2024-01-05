from abc import ABC, abstractmethod
from typing import List
from app.domain.tournament import Tournament


class TournamentRepository(ABC):
    @abstractmethod
    def create(self, tournament: Tournament) -> Tournament:
        pass
    
    @abstractmethod
    def get_all(self) -> List[Tournament]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Tournament:
        pass
