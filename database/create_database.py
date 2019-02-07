#!/usr/bin/env python3
"""
create_database.py

Purpose: Creates a transportation database and populates it with initial values

Classes:
    CurrentStatus: table for tracking the current data of transportation vehicle
    SwitchStatus: table for tracking the data for routing switches
    FutureStatus: table to hold user orders of transportation changes

Author: Cody Jackson

Date: 1/9/19
################################
Version 0.4
    Set default table creation values
Version 0.3
    Added station status table
Version 0.2
    Added orders speed request
Version 0.1
    Initial build
"""
import os

from sqlalchemy import Column, Integer, String, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class TrainStatus(Base):
    """Table for tracking the current data of transportation vehicle"""
    __tablename__ = "current"
    id = Column(Integer, primary_key=True)
    identification = Column(String(length=250), nullable=False)  # Engine or car number
    location = Column(String(length=50), nullable=False)  # Station or RFID tag
    speed = Column(Integer, nullable=False, default=0)  # Scaled to real world
    car_status = Column(Boolean, nullable=False, default=True)  # Operational = True, Broken = False


class SwitchStatus(Base):
    """Table for tracking the data for routing switches"""
    __tablename__ = "switches"
    id = Column(Integer, primary_key=True)
    switch_name = Column(String(length=50), nullable=False)
    switch_status = Column(Boolean, nullable=False, default=True)  # Operational = True, Broken = False
    switch_position = Column(Boolean, nullable=False, default=True)  # Straight = True, Switched = False


class TrainOrders(Base):
    """Table to hold user orders of transportation changes"""
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    who = Column(String(length=250), nullable=False)  # Engine or car number
    where_to = Column(String(length=50), nullable=False)  # Station number
    how = Column(String)  # Route
    estimated_time = Column(Integer, nullable=False)  # ETA
    cargo = Column(String(length=250))  # Cargo description
    priority = Column(Boolean)  # High priority = True, normal priority = False
    speed_request = Column(Integer)  # Requested speed to the train


class StationStatus(Base):
    """Table for station conditions."""
    __tablename__ = "stations"
    id = Column(Integer, primary_key=True)
    station_id = Column(String(length=250), nullable=False)
    station_status = Column(Boolean, nullable=False, default=True)  # Operational = True, Shutdown = False
    speed_restriction = Column(Integer, nullable=False, default=10)  # Station speed limit
    track_status = Column(Boolean, nullable=False, default=True)  # Station available = True, Station occupied = False


def create_db(path):
    """Create the database."""
    engine = create_engine(
        "sqlite:///{}".format(path))  # Interact w/ DB file
    Base.metadata.create_all(engine)  # Create the tables
    Base.metadata.bind = engine  # Bind engine to Base to access classes

    db_session = sessionmaker(bind=engine)  # Establish comms with DB
    session = db_session()  # Create staging area

    return session


def initial_db_fill(session):
    """Populates the newly created database with initial system data."""
    # Switches
    sw_1a = SwitchStatus(switch_name="1a")
    sw_1b = SwitchStatus(switch_name="1b")
    sw_2a = SwitchStatus(switch_name="2a")
    sw_2b = SwitchStatus(switch_name="2b")
    sw_3a = SwitchStatus(switch_name="3a")
    sw_3b = SwitchStatus(switch_name="3b")
    sw_4a = SwitchStatus(switch_name="4a")
    sw_4b = SwitchStatus(switch_name="4b")

    # Train location
    train_engine = TrainStatus(identification="Engine", location="Station 1")
    car1 = TrainStatus(identification="Car 1", location="Station 2")
    car2 = TrainStatus(identification="Car 2", location="Station 3")
    car3 = TrainStatus(identification="Car 3", location="Station 4")

    # Orders
    train_section = TrainOrders(who="", where_to="", how="", estimated_time=0, cargo="", priority=False,
                                speed_request=0)

    # Stations
    station_1 = StationStatus(station_id="Station 1")
    station_2 = StationStatus(station_id="Station 2")
    station_3 = StationStatus(station_id="Station 3")
    station_4 = StationStatus(station_id="Station 4")

    items = (sw_1a, sw_1b, sw_2a, sw_2b, sw_3a, sw_3b, sw_4a, sw_4b, train_engine, car1, car2, car3, train_section,
             station_1, station_2, station_3, station_4)

    session.add_all(items)
    session.commit()


if __name__ == "__main__":
    db_path = input("Please provide the path for the database: ")
    db_path = os.path.join(db_path)  # Cross-platform compatibility

    sess = create_db(db_path)

    initial_db_fill(sess)
