from sqlalchemy import String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from sqlmodel import SQLModel, Field,Column
import sqlalchemy.dialects.postgresql as pg
from uuid import UUID, uuid4
from datetime import datetime
from app.core.config import config

engine = create_engine(config.db_url, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, index=True)

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
