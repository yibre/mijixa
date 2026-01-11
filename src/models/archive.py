from sqlmodel import SQLModel, Field,Column
import sqlalchemy.dialects.postgresql as pg
from uuid import UUID, uuid4
from datetime import datetime

class Archive(SQLModel, table=True):
    __tablename__ = 'archives'
    uid: UUID=Field(
        sa_column=Column(pg.UUID ,primary_key=True,
        unique=True, default=uuid4)
    )
    title:str
    #TODO: 여기 추가로 만들어야함