import pytest

import set_switch

from database.create_database import SwitchStatus
from sqlalchemy.exc import StatementError
from sqlalchemy.orm.exc import NoResultFound


def test_initial_switch(transportation_db):
    """Test that a switch is set up properly."""
    check_switch = transportation_db.query(SwitchStatus).filter(SwitchStatus.switch_name == "1a").one()
    assert check_switch.switch_status is True
    assert check_switch.switch_position is True


def test_switch_update(transportation_db):
    """Test that switch updates correctly."""
    set_switch.update_switch(session=transportation_db, sw_name="1a", status=False, position=False)
    get_switch = transportation_db.query(SwitchStatus).filter(SwitchStatus.switch_name == "1a").one()
    assert get_switch.switch_status is False
    assert get_switch.switch_position is False


def test_invalid_name(transportation_db):
    """Test invalid switch name."""
    with pytest.raises(NoResultFound):
        set_switch.update_switch(transportation_db, sw_name="20a", status=False, position=False)


def test_invalid_position(transportation_db):
    """Test invalid switch position."""
    with pytest.raises(StatementError):
        set_switch.update_switch(transportation_db, sw_name="1a", status=True, position="a")


def test_invalid_status(transportation_db):
    """Test invalid switch status."""
    with pytest.raises(StatementError):
        set_switch.update_switch(transportation_db, sw_name="1a", status="a", position=True)