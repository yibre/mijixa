from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.posgresql as pg


class Picture(SQLModel, table=True):
    """
    아카이빙용 사진목록
    """
    __tablename__ = 'pictures'
    uid:UUID = Field(
        sa_column=Column(pg.UUID ,primary_key=True,
        unique=True, default=uuid4)
    )
    language: str # 사용 언어
    description: str = Field(sa_column=Column(TEXT))
    picture_path: str
