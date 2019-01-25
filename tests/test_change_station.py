from Database.create_database import Base, FutureStatus
from Database import create_database, set_orders


def test_engine_sta3(tmpdir):
    db_file = tmpdir.join("temp_train.db")
    sess = create_database.create_db(db_file)
    create_database.initial_db_fill(sess)

    set_orders.create_orders(vehicle="Engine", destination="Station 3", cargo="N/A", turbo=False, session=sess)

    orders = sess.query(FutureStatus).one()
    assert orders.who == "Engine"
    assert orders.where == "Station 3"

    set_orders.close_session(sess)
