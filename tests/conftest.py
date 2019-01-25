import pytest
import sys
sys.path.extend(["/home/cody/PycharmProjects/Transportation_model"])

from Database import create_database, set_orders


@pytest.fixture()
def transportation_db(tmpdir):
    db_file = tmpdir.join("temp_train.db")
    sess = create_database.create_db(db_file)
    create_database.initial_db_fill(sess)

    yield

    set_orders.close_session(sess)
