from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine("sqlite:///cafeteria.db")
Base = declarative_base()

# association_table = Table(
#     "association",
#     Base.metadata,
#     #     Column("id", Integer, primary_key=True),
#     #     Column("movie_id", Integer, ForeignKey("movie.id")),
#     #     Column("actor_id", Integer, ForeignKey("actor.id")),
# )


class Menu(Base):
    __tablename__ = "menu"
    id = Column(Integer, primary_key=True)
    food_name = Column(String)
    price = Column(Float)
    # actors = relationship("Actor", secondary=association_table, back_populates="movies")


class Tables(Base):
    __tablename__ = "tables"
    id = Column(Integer, primary_key=True)
    two_places = Column(String)
    four_places = Column(String)
    six_places = Column(String)
    condition = Column(String)
    # movies = relationship("Movie", secondary=association_table, back_populates="actors")


class Reservations(Base):
    __tablename__ = "reservations"
    id = Column(Integer, primary_key=True)
    client_name = Column(String)
    client_surname = Column(String)
    client_phone = Column(String)
    booking_nr = Column(String)
    # movies = relationship("Movie", secondary=association_table, back_populates="actors")


class Orders(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    


Base.metadata.create_all(engine)
