from abc import ABC, abstractmethod
from typing import List
from app.domain.competitor import Competitor


class CompetitorRepository(ABC):
    @abstractmethod
    def create(self, competitor: Competitor) -> Competitor:
        pass
    
    @abstractmethod
    def get_all(self) -> List[Competitor]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Competitor:
        pass
