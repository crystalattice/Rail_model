from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_database import Base, CurrentStatus, SwitchStatus, FutureStatus  # Import tables from database creation

engine = create_engine("sqlite:///transportation.db")  # Create DB engine
Base.metadata.bind = engine  # Bind engine to Base to access classes

DBSession = sessionmaker(bind=engine)  # Establish comms with DB
session = DBSession()  # Create staging area

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
engine = CurrentStatus(identification="Engine", location="Station 1", speed=0, car_status=True)
car1 = CurrentStatus(identification="Car 1", location="Station 2", speed=0, car_status=True)
car2 = CurrentStatus(identification="Car 2", location="Station 3", speed=0, car_status=True)
car3 = CurrentStatus(identification="Car 3", location="Station 4", speed=0, car_status=True)

# Orders
train_section = FutureStatus(who="", where="", how="", when=0, what="", priority=False)

items = (_1a, _1b, _2a, _2b, _3a, _3b, _4a, _4b, engine, car1, car2, car3, train_section)

session.add_all(items)
session.commit()

if __name__ == "__main__":
    switched = session.query(SwitchStatus).all()
    for switch in switched:
        print(switch.switch_name)
        print(switch.switch_status)
        print(switch.switch_position)

    train = session.query(CurrentStatus).all()
    for section in train:
        print(section.identification)
        print(section.location)
        print(section.speed)
        print(section.car_status)

    orders = session.query(FutureStatus).first()
    print(orders.who)
    print(orders.where)
    print(orders.how)
    print(orders.when)
    print(orders.what)
    print(orders.priority)
