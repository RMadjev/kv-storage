import unittest

from tests import BaseCase


class TestSetMethod(BaseCase):
    """ Test methods that make actions on single pair"""

    def test_should_be_able_to_set_new_pair(self):
        response = self.client.get('/set?k={0}&v={1}'.format(
            self.example_key,
            self.example_value),
            content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'OK')
        # assert that value is stored in the db
        self.assertEqual(self.example_value,
                         self.storage.get(self.example_key))

    def test_should_fail_if_value_is_not_set(self):
        response = self.client.get('/set?k={0}'.format(self.example_key),
                                   content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], 'Invalid value parameter')

    def test_should_fail_if_key_is_not_set(self):
        response = self.client.get('/set?v={0}'.format(self.example_value),
                                   content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], 'Invalid key parameter')


if __name__ == '__main__':
    unittest.main()
