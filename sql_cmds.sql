create table TrainStatus(
    car_id varchar(250) not null,
    car_location varchar(50) not null,
    car_speed integer not null,
    car_status varchar not null,
    primary key (car_id)
);

create table SwitchStatus(
    switch_name varchar(50) not null,
    switch_status varchar not null,
    switch_position varchar not null,
    primary key (switch_name)
);

create table TrainOrders(
    orders_id integer unique not null,
    car_num varchar(250) not null,
    destination varchar(50) not null,
    route varchar,
    estimated_time integer not null,
    cargo varchar(250),
    priority varchar,
    requested_speed integer,
    primary key (orders_id)
);

create table StationStatus(
    station_name varchar(250) not null,
    station_status varchar not null,
    station_speed integer not null,
    station_avail varchar not null,
    primary key (station_name)
);

create table RFID(
    uid varchar(50) not null,
    description varchar(250),
    primary key (uid)
);

truncate table TrainStatus;
partition table TrainStatus on column car_id;

truncate table SwitchStatus;
partition table SwitchStatus on column switch_name;

truncate table TrainOrders;
partition table TrainOrders on column orders_id;

truncate table StationStatus;
partition table StationStatus on column station_name;

truncate table RFID;
partition table RFID on column uid;

create procedure Insert_Switches
    partition on table SwitchStatus column switch_name
        as insert into SwitchStatus (switch_name, switch_status, switch_position) values (?, ?, ?);

create procedure Select_Switches
    partition on table SwitchStatus column switch_name
        as select switch_name, switch_status, switch_position from SwitchStatus where switch_name = ?;

create procedure Insert_Trains
    partition on table TrainStatus column car_id
        as insert into TrainStatus (car_id, car_location, car_speed, car_status) values (?, ?, ?, ?);

create procedure Select_Trains
    partition on table TrainStatus column car_id
        as select car_id, car_location, car_speed, car_status from TrainStatus where car_id = ?;

create procedure Insert_Orders
    partition on table TrainOrders column orders_id
        as insert into TrainOrders (orders_id, car_num, destination, route, estimated_time, cargo, priority, requested_speed)
            values (?, ?, ?, ?, ?, ?, ?, ?);

create procedure Select_Orders
    partition on table TrainOrders column orders_id
        as select car_num, destination, route, estimated_time, cargo, priority, requested_speed
        from TrainOrders where orders_id = ?;

create procedure Insert_Stations
    partition on table StationStatus column station_name
        as insert into StationStatus (station_name, station_status, station_speed, station_avail) values (?, ?, ?, ?);

create procedure Select_Stations
    partition on table StationStatus column station_name
        as select station_name, station_status, station_speed, station_avail from StationStatus where station_name= ?;

create procedure Insert_RFID
    partition on table RFID column uid
        as insert into RFID (uid, description) values (?, ?);

create procedure Select_RFID
    partition on table RFID column uid
        as select description from RFID where uid = ?;

create procedure Delete_Train
    partition on table TrainStatus column car_id
        as delete from TrainStatus where car_id = ?;

create procedure Update_Speed
    partition on table TrainStatus column car_id
        as update TrainStatus set car_speed = ? where car_id = ?;
