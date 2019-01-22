from sqlalchemy import Column, Integer, String, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class CurrentStatus(Base):
    __tablename__ = "current"
    id = Column(Integer, primary_key=True)
    identification = Column(String(length=250), nullable=False)  # Engine or car number
    location = Column(String(length=50), nullable=False)  # Station or RFID tag
    speed = Column(Integer, nullable=False)  # Scaled to real world
    car_status = Column(Boolean, nullable=False)  # Operational = True, Broken = False


class SwitchStatus(Base):
    __tablename__ = "switches"
    id = Column(Integer, primary_key=True)
    switch_name = Column(String(length=50), nullable=False)
    switch_status = Column(Boolean, nullable=False)  # Operational = True, Broken = False
    switch_position = Column(Boolean, nullable=False)  # Straight = True, Switched = False


class FutureStatus(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    who = Column(String(length=250), nullable=False)  # Engine or car number
    where = Column(String(length=50), nullable=False)  # Station number
    how = Column(String)  # Route
    when = Column(Integer, nullable=False)  # ETA
    what = Column(String(length=250))  # Cargo description
    priority = Column(Boolean)  # High priority = True, normal priority = False


engine = create_engine(
    "sqlite:////home/cody/PycharmProjects/Transportation_model/transportation.db")  # Interact w/ DB file
Base.metadata.create_all(engine)  # Create the tables
Base.metadata.bind = engine  # Bind engine to Base to access classes

DBSession = sessionmaker(bind=engine)  # Establish comms with DB
session = DBSession()  # Create staging area


def initial_db_fill():
    # Populate database
    # Switches
    _1a = SwitchStatus(switch_name="1a", switch_status=True, switch_position=True)
    _1b = SwitchStatus(switch_name="1b", switch_status=True, switch_position=True)
    _2a = SwitchStatus(switch_name="2a", switch_status=True, switch_position=True)
    _2b = SwitchStatus(switch_name="2b", switch_status=True, switch_position=True)
    _3a = SwitchStatus(switch_name="3a", switch_status=True, switch_position=True)
    _3b = SwitchStatus(switch_name="3b", switch_status=True, switch_position=True)
    _4a = SwitchStatus(switch_name="4a", switch_status=True, switch_position=True)
    _4b = SwitchStatus(switch_name="4b", switch_status=True, switch_position=True)

    # Train location
    train_engine = CurrentStatus(identification="Engine", location="Station 1", speed=0, car_status=True)
    car1 = CurrentStatus(identification="Car 1", location="Station 2", speed=0, car_status=True)
    car2 = CurrentStatus(identification="Car 2", location="Station 3", speed=0, car_status=True)
    car3 = CurrentStatus(identification="Car 3", location="Station 4", speed=0, car_status=True)

    # Orders
    train_section = FutureStatus(who="", where="", how="", when=0, what="", priority=False)

    items = (_1a, _1b, _2a, _2b, _3a, _3b, _4a, _4b, train_engine, car1, car2, car3, train_section)

    session.add_all(items)
    session.commit()


if __name__ == "__main__":
    initial_db_fill()

