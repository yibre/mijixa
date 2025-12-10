from sqlmodel import SQLModel, Field,Column
import sqlalchemy.dialects.postgresql as pg
from uuid import UUID, uuid4
from datetime import datetime


# 참고자료: https://github.com/jod35/lib-api/blob/main/src/db/models.py
# 유튜브 링크: https://www.youtube.com/watch?v=I8WiIXMDydw

class Book(SQLModel, table = True):
    """
    This class represents a book in the database
    """
    __tablename__ = 'books'
    uid:UUID = Field(
        sa_column=Column(pg.UUID ,primary_key=True,
        unique=True, default=uuid4)
    )
    title:str
    author:str
    isbn:str
    description:str
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    updated_at:datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))

    def __repr__(self) -> str:
        return f"Book => {self.title}"