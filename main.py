from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine("sqlite:///cafeteria.db")
Base = declarative_base()

# association_table = Table(
#     "association",
#     Base.metadata,
#     #     Column("id", Integer, primary_key=True),
#     #     Column("menu_id", Integer, ForeignKey("menu.id")),
#     #     Column("tables_2_places", Integer, ForeignKey("tables_2_places.id")),
# )


class Menu(Base):
    __tablename__ = "menu"
    id = Column(Integer, primary_key=True)
    food_name = Column(String)
    price = Column(Float)


class Tables_2_places(Base):
    __tablename__ = "tables_2"
    id = Column(Integer, primary_key=True)
    condition = Column(String)


class Tables_4_places(Base):
    __tablename__ = "tables_4"
    id = Column(Integer, primary_key=True)
    condition = Column(String)


class Tables_6_places(Base):
    __tablename__ = "tables_6"
    id = Column(Integer, primary_key=True)
    condition = Column(String)


class Reservations(Base):
    __tablename__ = "reservations"
    id = Column(Integer, primary_key=True)
    client_name = Column(String)
    client_surname = Column(String)
    client_phone = Column(String)
    booking_nr = Column(String)


class Orders(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)


Base.metadata.create_all(engine)
