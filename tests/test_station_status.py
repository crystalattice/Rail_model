import pytest

from Database.create_database import StationStatus

import set_train_orders


def test_station(transportation_db):
    """Test that a station is set up properly."""
    check_station = transportation_db.query(StationStatus).filter(StationStatus.station_id == "Station 1").one()
    assert check_station.station_status == True
    assert check_station.speed_restriction == 10
    assert check_station.track_status == True


def test_invalid_station(transportation_db):
    """Test valid car to invalid station."""
    with pytest.raises(UnboundLocalError):
        set_train_orders.create_orders(vehicle="Car 1", destination="Station 6", cargo="N/A", turbo=False, speed=30,
                                       session=transportation_db)


def test_engine_invalid_station(transportation_db):
    """Test valid car to invalid station."""
    with pytest.raises(UnboundLocalError):
        set_train_orders.create_orders(vehicle="Engine", destination="Station 6", cargo="N/A", turbo=False, speed=30,
                                       session=transportation_db)


def test_station_int(transportation_db):
    """Test station entry passed as non-string."""
    with pytest.raises(TypeError):
        set_train_orders.create_orders(vehicle="Engine", destination=2, cargo="N/A", turbo=False, speed=30,
                                       session=transportation_db)
