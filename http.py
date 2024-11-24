from contextlib import asynccontextmanager
from fastapi import FastAPI
from .domain import get_game_players, Player, GameRequest
from .db import Session

db_session = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    global db_session
    db_session = Session.connect()
    yield
    # Clean up the db session
    db_session = None


app = FastAPI(lifespan=lifespan)


@app.post("/game/")
async def post_game_request(game_request: GameRequest) -> list[Player]:
    return await get_game_players(game_request, db_session)
