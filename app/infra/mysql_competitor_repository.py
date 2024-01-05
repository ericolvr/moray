from typing import List
from sqlalchemy.orm import Session
from app.domain.competitor import Competitor
from app.domain.competitor_repository import CompetitorRepository
from app.infra.db import Base, get_db
from sqlalchemy import Column, Integer, String, ForeignKey


class CompetitorModel(Base):
    __tablename__ = "competitors"

    id = Column(Integer, primary_key=True, index=True)
    tournament_id = Column(Integer)
    name = Column(String(50), nullable=False)
    
    def to_domain(self) -> Competitor:
        return Competitor(
            tournament_id=self.tournament_id,
            name=self.name,
        )


class MySQLCompetitorRepository(CompetitorRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, competitor: Competitor) -> Competitor:
        new  = CompetitorModel(
            tournament_id=competitor.tournament_id,
            name=competitor.name
        )
        self.session.add(new)
        self.session.commit()
        self.session.refresh(new)
        return new.to_domain()

    def get_all(self, tournament_id: int) -> List[Competitor]:
        return self.session.query(CompetitorModel)\
            .filter(CompetitorModel.tournament_id == tournament_id).all()


    def get_by_id(self, id: int) -> Competitor:
        return self.session.query(CompetitorModel).filter(CompetitorModel.id == id).first()
