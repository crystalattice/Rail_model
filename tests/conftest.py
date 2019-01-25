import pytest
import sys
sys.path.extend(["/home/cody/PycharmProjects/Transportation_model"])

from Database import create_database


@pytest.fixture()
def transportation_db(tmpdir):
    create_database
