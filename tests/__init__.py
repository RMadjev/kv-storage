import unittest

from app import app
from storage import get_storage
from storage.database.db import db


class BaseCase(unittest.TestCase):
    example_key = 'myKey'
    example_key_2 = 'myKey2'
    example_value = 'myValue'
    example_value_2 = 'myValue2'
    example_not_used_key = 'myUnusedKey'

    def setUp(self):
        self.app = app.test_client()
        self.client = app.test_client(self)
        self.storage = get_storage(app.config['STORAGE'])
        self.db = db.get_db()

    def tearDown(self):
        # cleanup
        for collection in self.db.list_collection_names():
            self.db.drop_collection(collection)
