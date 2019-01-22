# import sys
# sys.path.extend(["/home/cody/PycharmProjects/Transportation_model"])

from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from create_database import CurrentStatus, SwitchStatus, FutureStatus  # Import tables from database creation

Base = declarative_base()


engine = create_engine(
    "sqlite:////home/cody/PycharmProjects/Transportation_model/transportation.db")
Base.metadata.bind = engine  # Bind engine to Base to access classes

DBSession = sessionmaker(bind=engine)  # Establish comms with DB
session = DBSession()  # Create staging area


def get_route_info(routing, sess):
    # Assume 30mph and 30 miles between stations
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

    # items = (_1b, _2a)

    # session.add_all(items)
    # sess.commit()


if __name__ == "__main__":
    route = "route_4_3"
    print(get_route_info(route, session))

    # sw_1b = session.query(SwitchStatus).filter(SwitchStatus.switch_name == "1b").one()
    # print(sw_1b.switch_position)
    # sw_1b.switch_position = False
    # print(sw_1b.switch_position)

    # switched = session.query(SwitchStatus).filter(SwitchStatus.switch_name == "1b").all()
    switched = session.query(SwitchStatus).all()
    for switch in switched:
        print(switch.switch_name)
        print(switch.switch_status)
        print(switch.switch_position)
