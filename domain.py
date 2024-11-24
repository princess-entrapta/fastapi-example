from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from db import Session
from pydantic import BaseModel


class GameRequest(BaseModel):
    nb_players: int


class Player(BaseModel):
    id: int
    name: str


async def get_game_players(rq: GameRequest, session: "Session") -> list[Player]:
    return [await session.create_player("hero" if i == 0 else "vilain") for i in range(rq.nb_players)]
