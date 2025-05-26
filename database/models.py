import sqlalchemy as db
from sqlalchemy import Table, Column, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from datetime import datetime
from typing import List

engine = db.create_engine('sqlite:///data.db')

class Base(DeclarativeBase): pass

cascad = 'CASCADE'
cascad1 = 'all, delete'

class Cities(Base):
    __tablename__ = "Cities"
    city_ID: Mapped[int] = mapped_column(primary_key=True,nullable=False)
    city_Name: Mapped[str] = mapped_column(String(128),nullable=False)
    stations = relationship('Stations', back_populates='city', cascade=cascad1)

class Stations(Base):
    __tablename__ = "Stations"
    station_ID: Mapped[int] = mapped_column(primary_key=True,nullable=False)
    station_Name: Mapped[str] = mapped_column(String(128),nullable=False)
    city_ID: Mapped[int] = mapped_column(ForeignKey("Cities.city_ID", ondelete=cascad),nullable=False)
    city = relationship('Cities', back_populates='stations')
    structures = relationship('RoutesStructure', back_populates='station', cascade=cascad1)

class Routes(Base):
    __tablename__ = "Routes"
    route_ID: Mapped[int] = mapped_column(primary_key=True,nullable=False)
    route_Name: Mapped[str] = mapped_column(String(128),nullable=False)
    structures = relationship('RoutesStructure', back_populates='route', cascade=cascad1)
    transports = relationship('Transport', back_populates='route')

class RoutesStructure(Base):
    __tablename__ = "RoutesStructure"
    struct_ID: Mapped[int] = mapped_column(primary_key=True,nullable=False)
    route_ID: Mapped[int] = mapped_column(ForeignKey("Routes.route_ID", ondelete=cascad),nullable=False)
    station_ID: Mapped[int] = mapped_column(ForeignKey("Stations.station_ID", ondelete=cascad),nullable=False)
    time: Mapped[datetime] = mapped_column(nullable=False)
    route = relationship('Routes', back_populates='structures')
    station = relationship('Stations', back_populates='structures')

class TransportTypes(Base):
    __tablename__ = "TransportTypes"
    type_ID: Mapped[int] = mapped_column(primary_key=True,nullable=False)
    type_Name: Mapped[str] = mapped_column(String(128),nullable=False)
    type_Average_Speed: Mapped[int] = mapped_column(nullable=False)
    transport = relationship('Transport', back_populates='type', cascade=cascad1)

class Transport(Base):
    __tablename__ = "Transport"
    ts_ID: Mapped[int] = mapped_column(primary_key=True,nullable=False)
    commissioning_date: Mapped[datetime] = mapped_column(nullable=False)
    type_ID: Mapped[int] = mapped_column(ForeignKey("TransportTypes.type_ID", ondelete=cascad),nullable=False)
    route_ID: Mapped[int] = mapped_column(ForeignKey("Routes.route_ID", ondelete='SET NULL'),nullable=True)
    type = relationship('TransportTypes', back_populates='transport')
    route = relationship('Routes', back_populates='transports')

