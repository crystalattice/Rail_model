#!/usr/bin/env python3
"""
set_orders.py

Purpose: Takes user input and updates the database accordingly

Author: Cody Jackson

Date: 1/15/19
################################
Version 0.1
    Initial build
"""

import argparse
import sys
sys.path.extend(["/home/cody/PycharmProjects/Transportation_model"])
from Database import station_mapping

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_database import Base, CurrentStatus, SwitchStatus, FutureStatus  # Import tables from database creation


def access_db():
    """Establish connection to created database."""
    engine = create_engine(
        "sqlite:////home/cody/PycharmProjects/Transportation_model/transportation.db")  # Interact w/ DB file
    Base.metadata.bind = engine  # Bind engine to Base to access classes

    db_session = sessionmaker(bind=engine)  # Establish comms with DB
    session = db_session()  # Create staging area

    return session


def arg_parser():
    """Capture transportation orders from user."""
    parser = argparse.ArgumentParser(description="Get the transportation move order.")
    parser.add_argument("who", help="Engine or car identification. Options: 'Engine', 'Car 1', 'Car 2', 'Car 2'")
    parser.add_argument("where", help="Destination station. Option: 'Station 1', 'Station 2', 'Station 3, 'Station 4'")
    parser.add_argument("--what", default="N/A", help="Cargo description")
    parser.add_argument("--priority", default=False, type=bool, help="Rush delivery. Default = False")
    var_args = vars(parser.parse_args())

    return var_args


def create_orders(vehicle, destination, cargo, turbo, session):
    """Stage updates to database based on user input."""
    route_time = get_route(vehicle, destination, session)
    move_car = session.query(FutureStatus).first()
    move_car.who = vehicle
    move_car.where = destination
    move_car.what = cargo
    move_car.how = ""
    move_car.when = route_time
    move_car.priority = turbo

    return move_car


def get_curr_location(vehicle, session):
    """Determine the current location of the desired train car."""
    selected_car = session.query(CurrentStatus).filter(CurrentStatus.identification == vehicle).one()
    curr_loc = selected_car.location

    return curr_loc


def get_route(vehicle, destination, session):
    """Based on the current location and ordered location, determine the switch lineup required and ETA."""
    curr_location = get_curr_location(vehicle, session)
    new_loc = f"route_{curr_location[-1]}_{destination[-1]}"
    route = station_mapping.get_route_info(new_loc, session)

    return route


def commit_session(session, movement):
    """Update the database with staged data."""
    session.add(movement)
    session.commit()


def close_session(session):
    """Close connection to database."""
    session.close()


if __name__ == "__main__":
    user_args = arg_parser()
    who = user_args["who"]
    where = user_args["where"]
    what = user_args["what"]
    priority = user_args["priority"]

    db_access = access_db()
    move_train = create_orders(who, where, what, priority, db_access)

    commit_session(db_access, move_train)
    user_close = input("Do you want to close the access to the database? [y/N]")
    if user_close.lower() == "y":
        close_session(db_access)
