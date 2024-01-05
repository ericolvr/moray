from abc import ABC, abstractmethod
from typing import List
from app.domain.result import Result


class ResultRepository(ABC):
    @abstractmethod
    def create(self, result: Result) -> Result:
        pass
    
    @abstractmethod
    def get_all(self) -> List[Result]:
        pass
