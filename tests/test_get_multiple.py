import unittest

from tests import BaseCase


class TestGetMultipleMethods(BaseCase):
    """ Test methods that make actions on single pair"""

    def setUp(self):
        super().setUp()
        self.storage.set(self.example_key, self.example_value)
        self.storage.set(self.example_key_2, self.example_value_2)

    def test_should_be_able_to_get_new_pair(self):
        response = self.client.get('/getAll'.format(self.example_key),
                                   content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['data'][self.example_key],
                         self.example_value)
        self.assertEqual(response.json['data'][self.example_key_2],
                         self.example_value_2)

    def test_should_return_empty_list_when_no_pairs_are_stored(self):
        # remove all data from the db
        self.storage.remove_all()

        response = self.client.get('/getAll',
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['data'], {})

    def test_should_be_able_to_get_values_only(self):
        response = self.client.get('/getValues',
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['data'], [
            self.example_value,
            self.example_value_2,
        ])

    def test_should_be_able_to_get_keys_only(self):
        response = self.client.get('/getKeys',
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['data'], [
            self.example_key,
            self.example_key_2
        ])

    def test_wrong_pagination_leads_to_404_for_get_all(self):
        response = self.client.get('/getAll?page=1000',
                                   content_type='application/json')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['error'], 'No pairs stored')

    def test_wrong_pagination_leads_to_404_for_get_keys(self):
        response = self.client.get('/getKeys?page=1000',
                                   content_type='application/json')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['error'], 'No keys stored')

    def test_wrong_pagination_leads_to_404_for_get_values(self):
        response = self.client.get('/getValues?page=1000',
                                   content_type='application/json')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['error'], 'No values stored')


if __name__ == '__main__':
    unittest.main()
