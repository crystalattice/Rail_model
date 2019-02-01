#!/usr/bin/env python3
"""
db_queries.py

Purpose: Utility program to generate DB queries for testing, without adding extraneous code to actual program files.

Author: Cody Jackson

Date: 1/ 22/19
################################
Version 0.1
    Initial build
"""
import os
import sys
sys.path.extend(["/home/cody/PycharmProjects/Transportation_model"])

from Database.create_database import Base, CurrentStatus, SwitchStatus, FutureStatus
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sqlalchemy.orm.exc as sqlerror

db_path = input("Please provide the path for the database: ")
db_path = os.path.join(db_path)  # Cross-platform compatibility

engine = create_engine(
    "sqlite:////{}".format(db_path))  # Interact w/ DB file
Base.metadata.bind = engine  # Bind engine to Base to access classes

db_session = sessionmaker(bind=engine)  # Establish comms with DB
db_access = db_session()  # Create staging area

print("SWITCH POSITION")
switched = db_access.query(SwitchStatus).all()
for switch in switched:
    print("Switch name: {}".format(switch.switch_name))
    print("Switch status: {}".format(switch.switch_status))
    print("Switch position: {}".format(switch.switch_position))

print("*"*25)
print("CURRENT STATUS")
train = db_access.query(CurrentStatus).all()
for section in train:
    print("Train section ID: {}".format(section.identification))
    print("Current location: {}".format(section.location))
    print("Current speed: {}".format(section.speed))
    print("Current status: {}".format(section.car_status))

print("*"*25)
print("ORDERS")
orders = db_access.query(FutureStatus).one()
print("Ordered car: {}".format(orders.who))
print("Ordered location: {}".format(orders.where))
# print(orders.how)
print("ETA: {}".format(orders.when))
print("Cargo: {}".format(orders.what))
print("Ordered priority: {}".format(orders.priority))

print("*"*25)
print("CURRENT STATUS AFTER MOVE")
train = db_access.query(CurrentStatus).all()
for section in train:
    print("Train section ID: {}".format(section.identification))
    print("Current location: {}".format(section.location))
    print("Current speed: {}".format(section.speed))
    print("Current status: {}".format(section.car_status))

print("*"*25)
print("ORDERS AFTER MOVE")
try:
    orders = db_access.query(FutureStatus).one()
except sqlerror.NoResultFound:
    pass

