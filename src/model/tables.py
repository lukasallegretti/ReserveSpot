from sqlalchemy import (
    Integer,
    String,
    ForeignKey,
    Date,
    Float,
)
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(30), nullable=False)
    email: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    phone_number: Mapped[int] = mapped_column(Integer(15))
    first_name: Mapped[str] = mapped_column(String(30), nullable=False)
    last_name: Mapped[str] = mapped_column(String(30), nullable=False)
    birth_date = mapped_column(Date, nullable=False)
    address: Mapped[str] = mapped_column(String(150))
    cpf: Mapped[int] = mapped_column(Integer(11), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f"""
            User(id={self.id!r},
            username={self.username!r},
            password={self.password!r},
            email={self.email!r},
            phone_number={self.phone_number!r},
            first_name={self.first_name!r},
            last_name={self.last_name!r},
            birth_date={self.birth_date!r},
            address={self.address!r},
            cpf={self.cpf!r})
        """


class Hotel(Base):
    __tablename__ = "hotels"

    hotel_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    hotel_name: Mapped[str] = mapped_column(String(50), nullable=False)
    address: Mapped[str] = mapped_column(String(150), nullable=False)
    cep: Mapped[int] = mapped_column(Integer(8), nullable=False)
    phone_number: Mapped[int] = mapped_column(Integer(15), nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)

    def __repr__(self) -> str:
        return f"""
            Hotel(hotel_id={self.hotel_id!r},
            hotel_name={self.hotel_name!r},
            address={self.address!r},
            cep={self.cep!r},
            phone_number={self.phone_number!r},
            description={self.description!r})
        """


class Room(Base):
    __tablename__ = "rooms"

    room_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    hotel_id: Mapped[int] = mapped_column(ForeignKey("hotels.hotel_id"), nullable=False)
    type: Mapped[str] = mapped_column(String(50), nullable=False)
    price: Mapped[float] = mapped_column(Float(10), nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    max_customers: Mapped[int] = mapped_column(Integer(3), nullable=False)
    total_rooms: Mapped[int] = mapped_column(Integer(3), nullable=False)

    def __repr__(self) -> str:
        return f"""
            Room(room_id={self.room_id!r},
            hotel_id={self.hotel_id!r},
            type={self.type!r},
            price={self.price!r},
            description={self.description!r},
            max_customers={self.max_customers!r},
            total_rooms={self.total_rooms!r})
        """


class Booking(Base):
    __tablename__ = "bookings"

    booking_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.room_id"), nullable=False)
    hotel_id: Mapped[int] = mapped_column(ForeignKey("hotels.hotel_id"), nullable=False)
    check_in: Mapped[Date] = mapped_column(Date, nullable=False)
    check_out: Mapped[Date] = mapped_column(Date, nullable=False)
    total_price: Mapped[float] = mapped_column(Float(10), nullable=False)
    total_nights: Mapped[int] = mapped_column(Integer(3), nullable=False)
    total_customers: Mapped[int] = mapped_column(Integer(3), nullable=False)
    status: Mapped[str] = mapped_column(String(50), nullable=False)

    def __repr__(self) -> str:
        return f"""
            Booking(booking_id={self.booking_id!r},
            user_id={self.user_id!r},
            room_id={self.room_id!r},
            hotel_id={self.hotel_id!r},
            check_in={self.check_in!r},
            check_out={self.check_out!r},
            total_price={self.total_price!r},
            total_nights={self.total_nights!r},
            total_customers={self.total_customers!r},
            status={self.status!r})
        """
