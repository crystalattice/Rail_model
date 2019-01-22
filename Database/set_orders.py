import argparse
import sys
sys.path.extend(["/home/cody/PycharmProjects/Transportation_model"])
from Database import station_mapping

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_database import Base, CurrentStatus, SwitchStatus, FutureStatus  # Import tables from database creation


def access_db():
    engine = create_engine(
        "sqlite:////home/cody/PycharmProjects/Transportation_model/transportation.db")  # Interact w/ DB file
    Base.metadata.bind = engine  # Bind engine to Base to access classes

    db_session = sessionmaker(bind=engine)  # Establish comms with DB
    session = db_session()  # Create staging area

    return session


def arg_parser():
    parser = argparse.ArgumentParser(description="Get the transportation move order.")
    parser.add_argument("who", help="Engine or car identification. Options: 'Engine', 'Car 1', 'Car 2', 'Car 2'")
    parser.add_argument("where", help="Destination station. Option: 'Station 1', 'Station 2', 'Station 3, 'Station 4'")
    parser.add_argument("--what", default="N/A", help="Cargo description")
    parser.add_argument("--priority", default=False, type=bool, help="Rush delivery. Default = False")
    var_args = vars(parser.parse_args())

    return var_args


def create_orders(vehicle, destination, cargo, turbo, session):
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
    selected_car = session.query(CurrentStatus).filter(CurrentStatus.identification == vehicle).one()
    curr_loc = selected_car.location

    return curr_loc


def get_route(vehicle, destination, session):
    curr_location = get_curr_location(vehicle, session)
    new_loc = f"route_{curr_location[-1]}_{destination[-1]}"
    route = station_mapping.get_route_info(new_loc, session)

    return route


def close_session(session, movement):
    session.add(movement)
    session.commit()


if __name__ == "__main__":
    user_args = arg_parser()
    who = user_args["who"]
    where = user_args["where"]
    what = user_args["what"]
    priority = user_args["priority"]

    db_access = access_db()
    move_train = create_orders(who, where, what, priority, db_access)

    close_session(db_access, move_train)


