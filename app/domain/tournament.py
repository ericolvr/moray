from pydantic import BaseModel
from typing import Optional


class Tournament(BaseModel):
    name: str
