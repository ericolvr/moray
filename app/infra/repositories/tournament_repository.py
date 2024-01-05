from typing import List
from sqlalchemy.orm import Session
from app.domain.tournament import Tournament
from app.domain.tournament_repository import TournamentRepository
from app.infra.db import Base, get_db
from sqlalchemy import Column, Integer, String


class TournamentModel(Base):
    __tablename__ = "tournaments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    
    def to_domain(self) -> Tournament:
        return Tournament(
            id=self.id,
            name=self.name,
        )


class TournamentRepository(TournamentRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, tournament: Tournament) -> Tournament:
        new  = TournamentModel(
            name=tournament.name
        )
        self.session.add(new)
        self.session.commit()
        self.session.refresh(new)
        return new.to_domain()

    def get_all(self) -> List[Tournament]:
        return self.session.query(TournamentModel).all()

    def get_by_id(self, id: int) -> Tournament:
        return self.session.query(TournamentModel).filter(TournamentModel.id == id).first()
