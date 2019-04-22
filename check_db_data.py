from db_getter_procs import *
from voltdbclient import *

client = FastSerializer("localhost", 21212)

if __name__ == "__main__":
    print("Stations")
    print(get_stations_proc.call(["Station 1"]))
    print("*" * 8)
    print(get_stations_proc.call(["Station 2"]))
    print("*" * 8)
    print(get_stations_proc.call(["Station 3"]))
    print("*" * 8)
    print(get_stations_proc.call(["Station 4"]))

    print("*" * 8)
    print("Orders")
    print("*" * 8)
    print(get_orders_proc.call([0]))

    print("*" * 8)
    print("Switches")
    print("*" * 8)
    print(get_switches_proc.call(["1a"]))
    print(get_switches_proc.call(["1b"]))
    print(get_switches_proc.call(["2a"]))
    print(get_switches_proc.call(["2b"]))
    print(get_switches_proc.call(["3a"]))
    print(get_switches_proc.call(["3b"]))
    print(get_switches_proc.call(["4a"]))
    print(get_switches_proc.call(["4b"]))

    print("*" * 8)
    print("Cars")
    print("*" * 8)
    print(get_trains_proc.call(["Engine"]))
    print(get_trains_proc.call(["Car 1"]))
    print(get_trains_proc.call(["Car 2"]))
    print(get_trains_proc.call(["Car 3"]))

