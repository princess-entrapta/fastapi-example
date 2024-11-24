import psycopg
from .domain import Player

class Session:
    @classmethod
    async def connect(cls) -> "Session": ...
    conn: psycopg.AsyncConnection
    def __init__(self, conn: psycopg.AsyncConnection) -> None: ...
    async def create_player(self, name: str) -> Player: ...
