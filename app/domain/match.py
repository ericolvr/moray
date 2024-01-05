from pydantic import BaseModel
from typing import Optional


class Match(BaseModel):
    tournament_id: int
    competitor_a: str
    competitor_b: str
