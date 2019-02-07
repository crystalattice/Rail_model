import pytest

import set_train_orders
import set_station

from database.create_database import StationStatus


def test_station(transportation_db):
    """Test that a station is set up properly."""
    check_station = transportation_db.query(StationStatus).filter(StationStatus.station_id == "Station 1").one()
    assert check_station.station_status is True
    assert check_station.speed_restriction == 10
    assert check_station.track_status is True


def test_invalid_station(transportation_db):
    """Test valid car to invalid station."""
    with pytest.raises(UnboundLocalError):
        set_train_orders.create_orders(vehicle="Car 1", destination="Station 6", session=transportation_db)


def test_engine_invalid_station(transportation_db):
    """Test valid car to invalid station."""
    with pytest.raises(UnboundLocalError):
        set_train_orders.create_orders(vehicle="Engine", destination="Station 6", session=transportation_db)


def test_station_int(transportation_db):
    """Test station entry passed as non-string."""
    with pytest.raises(TypeError):
        set_train_orders.create_orders(vehicle="Engine", destination=2, session=transportation_db)


def test_station_update(transportation_db):
    """Test station updates."""
    set_station.update_station(session=transportation_db, station_id="Station 1", status=False, speed=30, empty=False)
    get_station = transportation_db.query(StationStatus).filter(StationStatus.station_id == "Station 1").one()
    assert get_station.station_status is False
    assert get_station.speed_restriction == 30
    assert get_station.track_status is False
