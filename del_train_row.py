from db_setter_procs import del_trains_proc
from db_getter_procs import get_trains_proc
from voltdbclient import *

client = FastSerializer("localhost", 21212)


def del_train(car):
    del_trains_proc.call([car])


if __name__ == "__main__":
    car_id = input("Name of car/engine id: ")
    del_train(car_id)

    print("Engine")
    print(get_trains_proc.call(["Engine"]))
    print("*" * 8)
    print("Car 1")
    print(get_trains_proc.call(["Car 1"]))
    print("*" * 8)
    print("Car 2")
    print(get_trains_proc.call(["Car 2"]))
    print("*" * 8)
    print("Car 3")
    print(get_trains_proc.call(["Car 3"]))
