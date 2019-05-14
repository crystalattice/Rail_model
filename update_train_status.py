# from db_setter_procs import set_speed_proc
from db_setter_procs import set_trains_proc
import del_train_row
from db_getter_procs import get_trains_proc
from voltdbclient import *

client = FastSerializer("localhost", 21212)


def update_train_status(new_speed):
    del_train_row.del_train("Engine")
    set_trains_proc.call(["Engine", "Station 1", new_speed, "True"])


if __name__ == "__main__":
    speed = int(input("How fast? "))
    update_train_status(speed)
