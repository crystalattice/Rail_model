import argparse

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_database import Base, CurrentStatus, SwitchStatus, FutureStatus  # Import tables from database creation


def arg_parser():
    parser = argparse.ArgumentParser(description="Get the transportation move order.")
    parser.add_argument("who", help="Engine or car identification")
    parser.add_argument("where", help="Destination")
    parser.add_argument("what", default="N/A", help="Cargo description")
    parser.add_argument("priority", default=False, type=bool, help="Rush delivery. Default = False")
    var_args = vars(parser.parse_args())

    return var_args


def access_db():
    engine = create_engine("sqlite:///transportation.db")  # Create DB engine
    Base.metadata.bind = engine  # Bind engine to Base to access classes

    db_session = sessionmaker(bind=engine)  # Establish comms with DB
    session = db_session()  # Create staging area

    return session


# TODO: get route information and ETA from station_mapping.py
def create_orders(vehicle, destination, cargo, turbo):
    move_car = FutureStatus(who=vehicle, where=destination, how="", when=0, what=cargo, priority=turbo)


def close_session(session):
    session.add_all(items)
    session.commit()


if __name__ == "__main__":
    user_args = arg_parser()
    who = user_args["who"]
    where = user_args["where"]
    what = user_args["what"]
    priority = user_args["priority"]

    db_access = access_db()
    create_orders(who, where, what, priority)

    close_session(db_access)
