from enum import Enum
from typing import Optional, List

from pydantic import BaseModel

from app.models.move import Move
from app.models.user import User


class GameStatus(str, Enum):
    PLAYING = 'playing'
    ENDED = 'ended'
    CREATED = 'created'
    WAITING = 'waiting'


class GameBase(BaseModel):
    status: GameStatus = GameStatus.CREATED
    players: Optional[List[User]]


class Game(GameBase):
    active_players: int = 0
    moves: Optional[List[Move]]


class GameInDB(GameBase):
    id: int
