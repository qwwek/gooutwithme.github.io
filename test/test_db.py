import pytest
import mongomock
from src import db


@pytest.fixture(scope='module')
def mongo_client():
    client = mongomock.MongoClient()
    db.client = client
    db.db = client[db.db_name]
    yield client


def test_save_doc(mongo_client):
    doc = {"name": "test"}
    db.save_doc('test_collection', doc)
    result = db.db['test_collection'].find_one({"name": "test"})
    assert result is not None
    assert result['name'] == "test"


def test_get_data(mongo_client):
    query = {"name": "test"}
    result = db.get_data('test_collection', query)
    assert result is not None
    assert result['name'] == "test"


def test_del_doc(mongo_client):
    query = {"name": "test"}
    db.del_doc('test_collection', query)
    result = db.get_data('test_collection', query)
    assert result is None
