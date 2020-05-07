import unittest

from tests import BaseCase


class TestGetMethods(BaseCase):
    """ Test methods that make actions on single pair"""

    def setUp(self):
        super().setUp()
        self.storage.set(self.example_key, self.example_value)

    def test_should_be_able_to_get_new_pair(self):
        response = self.client.get('/get?k={0}'.format(self.example_key),
                                   content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json[self.example_key], self.example_value)

    def test_should_fail_if_key_is_not_set(self):
        response = self.client.get('/get', content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], 'Invalid key parameter')

    def test_should_get_404_if_key_is_not_set(self):
        response = self.client.get(
            '/get?k={0}'.format(self.example_not_used_key),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['error'],
                         "No value stored for key: {0}".format(
                             self.example_not_used_key
                         ))

    def test_should_be_able_to_check_if_key_exists(self):
        response = self.client.get('/is?k={0}'.format(self.example_key),
                                   content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], True)

    def test_should_return_false_if_key_doesnt_exists(self):
        response = self.client.get('/is?k={0}'.
                                   format(self.example_not_used_key),
                                   content_type='application/json')

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['message'], False)

    def test_should_fail_if_key_is_not_set_while_checking_for_existence(self):
        response = self.client.get('/is', content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], 'Invalid key parameter')


if __name__ == '__main__':
    unittest.main()
