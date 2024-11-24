from aiosqlite import connect, Connection
from .domain import Player


class Session:
    @classmethod
    async def connect(cls) -> "Session":
        conn = await connect("sample.sqlite")
        cursor = await conn.execute("CREATE TABLE IF NOT EXISTS players (name TEXT, id INTEGER PRIMARY KEY)")
        await cursor.close()
        return cls(conn)

    def __init__(self, conn: Connection):
        self.conn = conn

    async def create_player(self, name: str) -> Player:
        cursor = await self.conn.execute("INSERT INTO players (name) VALUES (?) RETURNING id, name;", [name])
        player_tuple = await cursor.fetchone()
        await self.conn.commit()
        await cursor.close()
        return Player(id=player_tuple[0], name=player_tuple[1])
