import pytest

from database import create_database

import set_train_orders


@pytest.fixture()
def transportation_db(tmpdir):
    db_file = tmpdir.join("temp_train.db")
    sess = create_database.create_db(db_file)
    create_database.initial_db_fill(sess)

    yield sess

    set_train_orders.close_session(sess)
