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
from time import sleep

import sys
sys.path.extend(["/home/cody/PycharmProjects/Transportation_model"])

import station_mapping
from Database.create_database import Base, CurrentStatus, FutureStatus

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def arg_parser():
    """Capture transportation orders from user."""
    parser = argparse.ArgumentParser(description="Get the transportation move order.")
    parser.add_argument("db_location", help="Path of database to use.")
    parser.add_argument("who", help="Engine or car identification. Options: 'Engine', 'Car 1', 'Car 2', 'Car 2'")
    parser.add_argument("where", help="Destination station. Option: 'Station 1', 'Station 2', 'Station 3, 'Station 4'")
    parser.add_argument("--what", default="N/A", type=str, help="Cargo description")
    parser.add_argument("--priority", default=False, type=bool, help="Rush delivery. Default = False")
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
    new_loc = f"route_{curr_location[-1]}_{destination[-1]}"  # Alternative string formatting
    route = station_mapping.get_route_info(new_loc, session)

    return route


def commit_session(session, movement):
    """Update the database with staged data."""
    session.add(movement)
    session.commit()


def update_curr_location(session, orders):
    """After waiting for a period of time, update the current location based on orders."""
    new_status = session.query(CurrentStatus).filter(CurrentStatus.identification == orders.who).one()
    new_status.location = orders.where

    session.add(new_status)
    session.commit()


def clear_orders(session):
    """Clear entries from FutureStatus table."""
    orders = session.query(FutureStatus).first()
    session.delete(orders)
    session.commit()


def close_session(session):
    """Close connection to database."""
    session.close()


if __name__ == "__main__":
    user_args = arg_parser()
    db_path = user_args["db_location"]
    who = user_args["who"]
    where = user_args["where"]
    what = user_args["what"]
    priority = user_args["priority"]

    db_access = access_db(db_path)
    move_train = create_orders(who, where, what, priority, db_access)
    sleep(5)
    update_curr_location(db_access, move_train)

    commit_session(db_access, move_train)
    clear_orders(db_access)
    close_session(db_access)