from voltdbclient import *

client = FastSerializer("localhost", 21212)

get_switches_proc = VoltProcedure(client, "Select_Switches", [FastSerializer.VOLTTYPE_STRING])
get_trains_proc = VoltProcedure(client, "Select_Trains", [FastSerializer.VOLTTYPE_STRING])
get_orders_proc = VoltProcedure(client, "Select_Orders", [FastSerializer.VOLTTYPE_INTEGER])
get_stations_proc = VoltProcedure(client, "Select_Stations", [FastSerializer.VOLTTYPE_STRING])

