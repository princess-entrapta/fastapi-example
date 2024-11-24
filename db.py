from psycopg import rows, AsyncConnection
from .domain import Player


class Session:
    @classmethod
    async def connect(cls) -> "Session":
        async with await AsyncConnection.connect("dbname=test user=postgres") as conn:
            return cls(conn)

    def __init__(self, conn: AsyncConnection):
        self.conn = conn

    async def insert_hero(self, name: str) -> Player:
        async with self.conn.cursor(row_factory=rows.class_row(Player)) as acur:
            return await acur.fetchone("INSERT INTO heroes (name) VALUES (%s) RETURNING id, name;", name)
