from typing import List, Optional

from sqlalchemy import MetaData, Table, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean
from pydantic import BaseModel
from sqlalchemy.orm import Session, DeclarativeBase, mapped_column, Mapped, relationship

engine = create_engine(
    "postgresql+psycopg2://postgres:postgres@172.18.0.3:5432/postgres"
)

print(engine.connect())

SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


class Teste(Base):
    __tablename__ = "teste"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)


class User(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]

    addresses: Mapped[List["Address"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


class Address(Base):
    __tablename__ = "address2"

    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))

    user: Mapped["User"] = relationship(back_populates="addresses")

    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"


Base.metadata.create_all(engine)

with Session(engine) as session:
    spongebob = User(
        name="spongebob2",
        fullname="Spongebob Squarepants",
        addresses=[Address(email_address="spongebob@sqlalchemy.org")],
    )
    sandy = User(
        name="sandy2",
        fullname="Sandy Cheeks",
        addresses=[
            Address(email_address="sandy@sqlalchemy.org"),
            Address(email_address="sandy@squirrelpower.org"),
        ],
    )
    patrick = User(name="patrick2", fullname="Patrick Star")

    session.add_all([spongebob, sandy, patrick])

    session.commit()


# Table('teste', MetaData(),
#             Column('id', Integer(), table=<teste>, primary_key=True, nullable=False),
#             Column('name', String(), table=<users>),
#             Column('fullname', String(), table=<users>),
#             Column('nickname', String(), table=<users>), schema=None)
# print(Teste.__table__)


# class UserBase(BaseModel):
#     email: str


# class TestePy(UserBase):
#     id: int
#     hashed_password: str
#     is_active: bool


# def create_user(db: Session, user: TestePy):
#     db_user = Teste(
#         email=user.email, hashed_password=user.hashed_password, is_active=user.is_active
#     )
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user


# a = Teste(id=1, email="lukas@test.com", hashed_password="123", is_active=True)

# # create_user(SessionLocal, a)
