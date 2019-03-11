from voltdbclient import *

client = FastSerializer("localhost", 21212)
set_switches_proc = VoltProcedure(client, "Insert_Switches", [FastSerializer.VOLTTYPE_STRING,
                                                              FastSerializer.VOLTTYPE_STRING,
                                                              FastSerializer.VOLTTYPE_STRING])
set_trains_proc = VoltProcedure(client, "Insert_Trains", [FastSerializer.VOLTTYPE_STRING,
                                                          FastSerializer.VOLTTYPE_STRING,
                                                          FastSerializer.VOLTTYPE_INTEGER,
                                                          FastSerializer.VOLTTYPE_STRING])
set_orders_proc = VoltProcedure(client, "Insert_Orders", [FastSerializer.VOLTTYPE_INTEGER,
                                                          FastSerializer.VOLTTYPE_STRING,
                                                          FastSerializer.VOLTTYPE_STRING,
                                                          FastSerializer.VOLTTYPE_STRING,
                                                          FastSerializer.VOLTTYPE_INTEGER,
                                                          FastSerializer.VOLTTYPE_STRING,
                                                          FastSerializer.VOLTTYPE_STRING,
                                                          FastSerializer.VOLTTYPE_INTEGER])
set_stations_proc = VoltProcedure(client, "Insert_Stations", [FastSerializer.VOLTTYPE_STRING,
                                                              FastSerializer.VOLTTYPE_STRING,
                                                              FastSerializer.VOLTTYPE_INTEGER,
                                                              FastSerializer.VOLTTYPE_STRING])
