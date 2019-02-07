#!/usr/bin/env python3
"""
set_station.py

Purpose: Allows changes to a station, such as speed restrictions and availability

Author: Cody Jackson

Date: 2/5/19
################################
Version 0.1
    Initial build
"""

import argparse
from time import sleep

import sys
sys.path.extend(["/home/cody/PycharmProjects/Transportation_model"])

from database.create_database import Base, StationStatus

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def arg_parser():
    """Capture transportation orders from user."""
    parser = argparse.ArgumentParser(description="Update train station status.")
    parser.add_argument("db_location", help="Path of database to use.")
    parser.add_argument("station", help="Station identification. Options: 'Station 1', 'Station 2', 'Station 3, "
                                        "'Station 4'")
    parser.add_argument("--status", default=True, type=bool, help="Station status. Operational = True; Closed = False")
    parser.add_argument("--speed", default=10, type=str, help="Speed limit for the station. Default = 10")
    parser.add_argument("--empty", default=True, type=bool, help="Station available for train. "
                                                                 "Station available = True; Occupied = False")
    var_args = vars(parser.parse_args())

    return var_args


def access_db(path):
    """Establish connection to created database."""
    engine = create_engine(
        "sqlite:///{}".format(path))  # Interact w/ DB file
    Base.metadata.bind = engine  # Bind engine to Base to access classes

    db_session = sessionmaker(bind=engine)  # Establish comms with DB
    session = db_session()  # Create staging area

    return session


def update_station(session, station_id, status=True, speed=10, empty=True):
    """Change the status of a station."""
    station = session.query(StationStatus).filter(StationStatus.station_id == station_id).one()
    station.station_status = status
    station.speed_restriction = speed
    station.track_status = empty

    session.add(station)
    session.commit()
    session.close()


if __name__ == "__main__":
    user_args = arg_parser()
    db_path = user_args["db_location"]
    station_name = user_args["station"]
    working_status = user_args["status"]
    restrict_speed = user_args["speed"]
    available = user_args["empty"]

    db_access = access_db(db_path)
    update_station(db_access, station_name, working_status, restrict_speed, available)
