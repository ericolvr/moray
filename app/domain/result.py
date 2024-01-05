from pydantic import BaseModel
from typing import Optional


class Result(BaseModel):
    tournament_id: int
    match_id: int
    winner: str
    
