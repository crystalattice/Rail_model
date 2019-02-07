#!/usr/bin/env python3
"""
station_mapping.py

Purpose: Determine switch positions based on current and future location of train car.

Author: Cody Jackson

Date: 1/18/19
################################
Version 0.1
    Initial build
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from database.create_database import SwitchStatus


def get_route_info(routing, sess):
    """Update database with necessary switch positions, based on current and desired stations.

    Assumes 30mph and 30 miles between stations.
    """
    if routing == "route_1_2":
        sw_1b = sess.query(SwitchStatus).filter(SwitchStatus.switch_name == "1b").one()
        sw_1b.switch_position = False

        sw_2a = sess.query(SwitchStatus).filter(SwitchStatus.switch_name == "2a").one()
        sw_2a.switch_position = False
        time = 1
    elif routing == "route_1_3":
        sw_1b = sess.query(SwitchStatus).filter(SwitchStatus.switch_name == "1b").one()
        sw_1b.switch_position = False

        sw_3a = sess.query(SwitchStatus).filter(SwitchStatus.switch_name == "3a").one()
        sw_3a.switch_position = False
        time = 2
    elif routing == "route_1_4":
        sw_1b = sess.query(SwitchStatus).filter(SwitchStatus.switch_name == "1b").one()
        sw_1b.switch_position = False

        sw_4a = sess.query(SwitchStatus).filter(SwitchStatus.switch_name == "4a").one()
        sw_4a.switch_position = False
        time = 3
    elif routing == "route_2_1":
        sw_2b = sess.query(SwitchStatus).filter(SwitchStatus.switch_name == "2b").one()
        sw_2b.switch_position = False

        sw_1a = sess.query(SwitchStatus).filter(SwitchStatus.switch_name == "1a").one()
        sw_1a.switch_position = False
        time = 3
    elif routing == "route_2_3":
        sw_2b = sess.query(SwitchStatus).filter(SwitchStatus.switch_name == "2b").one()
        sw_2b.switch_position = False

        sw_3a = sess.query(SwitchStatus).filter(SwitchStatus.switch_name == "3a").one()
        sw_3a.switch_position = False
        time = 1
    elif routing == "route_2_4":
        sw_2b = sess.query(SwitchStatus).filter(SwitchStatus.switch_name == "2b").one()
        sw_2b.switch_position = False

        sw_4a = sess.query(SwitchStatus).filter(SwitchStatus.switch_name == "4a").one()
        sw_4a.switch_position = False
        time = 3
    elif routing == "route_3_1":
        sw_3b = sess.query(SwitchStatus).filter(SwitchStatus.switch_name == "3b").one()
        sw_3b.switch_position = False

        sw_1a = sess.query(SwitchStatus).filter(SwitchStatus.switch_name == "1a").one()
        sw_1a.switch_position = False
        time = 2
    elif routing == "route_3_2":
        sw_3b = sess.query(SwitchStatus).filter(SwitchStatus.switch_name == "3b").one()
        sw_3b.switch_position = False

        sw_2a = sess.query(SwitchStatus).filter(SwitchStatus.switch_name == "2a").one()
        sw_2a.switch_position = False
        time = 3
    elif routing == "route_3_4":
        sw_3b = sess.query(SwitchStatus).filter(SwitchStatus.switch_name == "3b").one()
        sw_3b.switch_position = False

        sw_4a = sess.query(SwitchStatus).filter(SwitchStatus.switch_name == "4a").one()
        sw_4a.switch_position = False
        time = 1
    elif routing == "route_4_1":
        sw_4b = sess.query(SwitchStatus).filter(SwitchStatus.switch_name == "4b").one()
        sw_4b.switch_position = False

        sw_1a = sess.query(SwitchStatus).filter(SwitchStatus.switch_name == "1a").one()
        sw_1a.switch_position = False
        time = 1
    elif routing == "route_4_2":
        sw_4b = sess.query(SwitchStatus).filter(SwitchStatus.switch_name == "4b").one()
        sw_4b.switch_position = False

        sw_2a = sess.query(SwitchStatus).filter(SwitchStatus.switch_name == "2a").one()
        sw_2a.switch_position = False
        time = 2
    elif routing == "route_4_3":
        sw_4b = sess.query(SwitchStatus).filter(SwitchStatus.switch_name == "4b").one()
        sw_4b.switch_position = False

        sw_3a = sess.query(SwitchStatus).filter(SwitchStatus.switch_name == "3a").one()
        sw_3a.switch_position = False
        time = 3

    return time


if __name__ == "__main__":
    pass
