from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.postgresql as pg
from sqlalchemy import TEXT
from uuid import UUID, uuid4
from typing import Optional


class Pinage(SQLModel, table=True):
    """
    아카이빙용 사진목록
    """
    __tablename__ = 'pictures'
    uid: UUID = Field(
        sa_column=Column(pg.UUID, primary_key=True,
        unique=True, default=uuid4)
    )
    post_id: UUID = Field(foreign_key="posts.uid")
    language: str # 사용 언어
    description: str = Field(sa_column=Column(TEXT))
    picture_path: str
    