from typing import List
from sqlalchemy.orm import Session
from app.domain.result import Result
from app.domain.result_repository import ResultRepository
from app.infra.db import Base, get_db
from sqlalchemy import Column, Integer, String, ForeignKey


class ResultModel(Base):
    __tablename__ = "results"

    id = Column(Integer, primary_key=True, index=True)
    tournament_id = Column(Integer)
    match_id = Column(Integer)
    winner = Column(String(100))

    def to_domain(self) -> Result:
        return Result(
            tournament_id=self.tournament_id,
            match_id=self.match_id,
            winner=self.winner,
        )


class MySQLResultRepository(ResultRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, result: Result) -> Result:
        new  = ResultModel(
            tournament_id=result.tournament_id,
            match_id=result.match_id,
            winner=result.winner,
        )
        self.session.add(new)
        self.session.commit()
        self.session.refresh(new)
        return new.to_domain()

    def get_all(self) -> List[Result]:
        return self.session.query(ResultModel).all()

