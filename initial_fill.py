from db_setter_procs import *
from voltdbclient import *

client = FastSerializer("localhost", 21212)

if __name__ == "__main__":
    set_switches_proc.call(["1a", "True", "True"])
    set_switches_proc.call(["1b", "True", "True"])
    set_switches_proc.call(["2a", "True", "True"])
    set_switches_proc.call(["2b", "True", "True"])
    set_switches_proc.call(["3a", "True", "True"])
    set_switches_proc.call(["3b", "True", "True"])
    set_switches_proc.call(["4a", "True", "True"])
    set_switches_proc.call(["4b", "True", "True"])

    set_trains_proc.call(["Engine", "Station 1", 0, "True"])
    set_trains_proc.call(["Car 1", "Station 2", 0, "True"])
    set_trains_proc.call(["Car 2", "Station 3", 0, "True"])
    set_trains_proc.call(["Car 3", "Station 4", 0, "True"])

    set_orders_proc.call([0, "", "", "", 0, "", "False", 0])

    set_stations_proc.call(["Station 1", "True", 10, "True"])
    set_stations_proc.call(["Station 2", "True", 10, "True"])
    set_stations_proc.call(["Station 3", "True", 10, "True"])
    set_stations_proc.call(["Station 4", "True", 10, "True"])

