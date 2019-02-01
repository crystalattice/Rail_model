import pytest
from sqlalchemy.orm.exc import NoResultFound
from Database.create_database import FutureStatus, CurrentStatus
from Database import create_database
import set_orders


@pytest.fixture()
def transportation_db(tmpdir):
    db_file = tmpdir.join("temp_train.db")
    sess = create_database.create_db(db_file)
    create_database.initial_db_fill(sess)

    yield sess

    set_orders.close_session(sess)


def test_engine_sta3(transportation_db):
    """Test Engine to valid station."""
    set_orders.create_orders(vehicle="Engine", destination="Station 3", cargo="N/A", turbo=False,
                             session=transportation_db)

    orders = transportation_db.query(FutureStatus).one()
    assert orders.who == "Engine"
    assert orders.where == "Station 3"


def test_car1_sta4(transportation_db):
    """Test car to valid station."""
    set_orders.create_orders(vehicle="Car 1", destination="Station 4", cargo="Denim", turbo=False,
                             session=transportation_db)

    orders = transportation_db.query(FutureStatus).one()
    assert orders.who == "Car 1"
    assert orders.where == "Station 4"
    assert orders.what == "Denim"


def test_invalid_car(transportation_db):
    """Test invalid car to valid station."""
    with pytest.raises(NoResultFound):
        set_orders.create_orders(vehicle="Car 6", destination="Station 2", cargo="N/A", turbo=False,
                                 session=transportation_db)


def test_invalid_station(transportation_db):
    """Test valid car to invalid station."""
    with pytest.raises(UnboundLocalError):
        set_orders.create_orders(vehicle="Car 1", destination="Station 6", cargo="N/A", turbo=False,
                                 session=transportation_db)


def test_engine_invalid_station(transportation_db):
    """Test valid car to invalid station."""
    with pytest.raises(UnboundLocalError):
        set_orders.create_orders(vehicle="Engine", destination="Station 6", cargo="N/A", turbo=False,
                                 session=transportation_db)


def test_vehicle_int(transportation_db):
    """Test vehicle entry passed as non-string."""
    with pytest.raises(NoResultFound):
        set_orders.create_orders(vehicle=6, destination="Station 2", cargo="N/A", turbo=False,
                                 session=transportation_db)


def test_station_int(transportation_db):
    """Test station entry passed as non-string."""
    with pytest.raises(TypeError):
        set_orders.create_orders(vehicle="Engine", destination=2, cargo="N/A", turbo=False,
                                 session=transportation_db)


def test_cargo_int(transportation_db):
    """Test cargo entry passed as non-string. Arguments should be converted to string."""
    set_orders.create_orders(vehicle="Car 1", destination="Station 4", cargo=8, turbo=False,
                             session=transportation_db)

    orders = transportation_db.query(FutureStatus).one()
    assert orders.what == "8"


def test_engine_turbo(transportation_db):
    """Test Engine to valid station with priority flag."""
    set_orders.create_orders(vehicle="Engine", destination="Station 3", cargo="N/A", turbo=True,
                             session=transportation_db)

    orders = transportation_db.query(FutureStatus).one()
    assert orders.who == "Engine"
    assert orders.where == "Station 3"
    assert orders.priority == True


def test_current_status_update(transportation_db):
    """Test CurrentStatus table is updated to new status after transportation orders made."""
    new_orders = set_orders.create_orders(vehicle="Engine", destination="Station 3", cargo="N/A", turbo=False,
                                          session=transportation_db)

    set_orders.update_curr_location(transportation_db, new_orders)
    new_status = transportation_db.query(CurrentStatus).filter(CurrentStatus.identification == new_orders.who).one()
    assert new_status.identification == "Engine"
    assert new_status.location == "Station 3"


def test_orders_status_cleared(transportation_db):
    """Test that future orders table is cleared after move performed."""
    new_orders = set_orders.create_orders(vehicle="Engine", destination="Station 3", cargo="N/A", turbo=False,
                                          session=transportation_db)

    set_orders.update_curr_location(transportation_db, new_orders)
    set_orders.clear_orders(transportation_db)
    with pytest.raises(NoResultFound):
        transportation_db.query(FutureStatus).one()
