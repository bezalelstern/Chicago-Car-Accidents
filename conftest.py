import pytest
from  pymongo import MongoClient
from pymongo.collection import Collection

@pytest.fixture()
def init_db():
    client = MongoClient('mongodb://localhost:27017/')
    test_db = client['test_db']
    yield test_db
    client.drop_database('test_db')
    client.close()

@pytest.fixture()
def users_db(init_db):
    return init_db['users']

def test_users_db(users_db: Collection):
    users_db.insert_one({'name': 'John Doe'})
    users_db.insert_one({'name': 'John Doe2'})
    users_db.insert_one({'name': 'John Doe3'})
    user = users_db.find_one({'name': 'John Doe'})
    assert user
    assert users_db.count_documents({}) == 3