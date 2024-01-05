from typing import List
from app.domain.result import Result
from app.domain.result_repository import ResultRepository


class ResultService:
    def __init__(self, repo: ResultRepository):
        self.repo = repo
    
    def create_result(self, result: Result) -> Result:
        return self.repo.create(result)

    def get_all_results(self) -> List[Result]:
        return self.repo.get_all()
    