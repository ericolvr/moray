from pydantic import BaseModel
from typing import Optional


class Competitor(BaseModel):
    tournament_id: int
    name: str
