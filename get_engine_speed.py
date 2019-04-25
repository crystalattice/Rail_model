from db_getter_procs import get_trains_proc
from voltdbclient import *

client = FastSerializer("localhost", 21212)


def get_speed():
    engine_speed = str(get_trains_proc.call(["Engine"]))
    return engine_speed


if __name__ == "__main__":
    speed_value = get_speed()
    print(speed_value[-10:-9])
