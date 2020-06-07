from urllib.parse import quote_plus

import pytest
from fastapi.testclient import TestClient
from pymongo import MongoClient

import main
import settings


@pytest.fixture
def enable_db():
    uri = "mongodb://%s:%s@%s" % (quote_plus(settings.MONGO_USER),
                                  quote_plus(settings.MONGO_PASSWORD),
                                  settings.MONGO_URL)
    client = MongoClient(uri)
    yield client.test
    client.drop_database('test')


@pytest.fixture
def get_client():
    client = TestClient(main.app)
    return client
