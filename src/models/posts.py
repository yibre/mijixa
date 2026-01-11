from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.postgresql as pg
from uuid import UUID, uuid4
from typing import Optional

class Post(SQLModel, table=True):
    __tablename__ = 'posts'
    uid: UUID = Field(
        sa_column=Column(pg.UUID, primary_key=True,
        unique=True, default=uuid4)
    )
    uploader: UUID = Field(default=None, foreign_key="users.uid")
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    updated_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    
    # pinage는 유저가 직접 접근 불가, pinage 여러개가 모여 post가 되며 유저는 늘 post 생성 함수에서 pinage도 생성 시작
