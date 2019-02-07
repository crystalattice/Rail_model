#!/usr/bin/env python3
"""
set_switch.py

Purpose: Allows changes to a switch, including position and status

Author: Cody Jackson

Date: 2/7/19
################################
Version 0.1
    Initial build
"""

import argparse

import sys
sys.path.extend(["/home/cody/PycharmProjects/Transportation_model"])

from database.create_database import Base, SwitchStatus

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def arg_parser():
    """Capture transportation orders from user."""
    parser = argparse.ArgumentParser(description="Update switch position and status.")
    parser.add_argument("db_location", help="Path of database to use.")
    parser.add_argument("switch", help="Switch name")
    parser.add_argument("position", default=True, type=bool, help="Switch position. Straight = True; Switched = False")
    parser.add_argument("--status", default=True, type=bool, help="Switch status. Operational = True; "
                                                                  "Inoperable = False")
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


def update_switch(session, sw_name, status=True, position=True):
    """Change the status of a station."""
    switch = session.query(SwitchStatus).filter(SwitchStatus.switch_name == sw_name).one()
    switch.switch_status = status
    switch.switch_position = position

    session.add(switch)
    session.commit()
    session.close()


if __name__ == "__main__":
    user_args = arg_parser()
    db_path = user_args["db_location"]
    switch_name = user_args["switch"]
    working_status = user_args["status"]
    switch_position = user_args["position"]

    db_access = access_db(db_path)
    update_switch(db_access, switch_name, working_status, switch_position)
