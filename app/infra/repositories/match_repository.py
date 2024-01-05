from typing import List
from sqlalchemy.orm import Session
from app.domain.match import Match
from app.domain.match_repository import MatchRepository
from app.infra.db import Base, get_db
from sqlalchemy import Column, Integer, String, ForeignKey


class MatchModel(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True, index=True)
    tournament_id = Column(Integer)
    competitor_a = Column(String(100))
    competitor_b = Column(String(100))

    def to_domain(self) -> Match:
        return Match(
            tournament_id=self.tournament_id,
            competitor_a=self.competitor_a,
            competitor_b=self.competitor_b,
        )


class MatchRepository(MatchRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, match: Match) -> Match:
        new  = MatchModel(
            tournament_id=match.tournament_id,
            competitor_a=match.competitor_a,
            competitor_b=match.competitor_b,
        )
        self.session.add(new)
        self.session.commit()
        self.session.refresh(new)
        return new.to_domain()

    def get_all(self) -> List[Match]:
        return self.session.query(MatchModel).all()


    def get_by_id(self, id: int) -> Match:
        return self.session.query(MatchModel).filter(MatchModel.id == id).first()
