from sqlalchemy import Column, Integer, String, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CurrentStatus(Base):
    __tablename__ = "current"
    id = Column(Integer, primary_key=True)
    identification = Column(String(length=250), nullable=False)  # Engine or car number
    location = Column(String(length=50), nullable=False)  # Station or RFID tag
    speed = Column(Integer, nullable=False)  # Scaled to real world
    car_status = Column(Boolean, nullable=False)  # Operational = True, Broken = False


class SwitchStatus(Base):
    __tablename__ = "switches"
    id = Column(Integer, primary_key=True)
    switch_name = Column(String(length=50), nullable=False)
    switch_status = Column(Boolean, nullable=False)  # Operational = True, Broken = False
    switch_position = Column(Boolean, nullable=False)  # Straight = True, Switched = False


class FutureStatus(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    who = Column(String(length=250), nullable=False)  # Engine or car number
    where = Column(String(length=50), nullable=False)  # Station number
    how = Column(String)  # Route
    when = Column(Integer, nullable=False)  # ETA
    what = Column(String(length=250))  # Cargo description
    priority = Column(Boolean)  # High priority = True, normal priority = False


engine = create_engine("sqlite:///transportation.db")  # Create engine to interact w/ DB file

Base.metadata.create_all(engine)  # Create the tables
