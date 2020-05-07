"""
    Classes used to extract and convert data from db object to a dict
"""


class DataExtractor:
    def __init__(self, data):
        self.data = data

    def _get_meta(self, model):
        # todo implement next page url, last page url, first page url
        return {
            'current_page': model.page,
            'pages_count': model.pages,
            'items_count': model.total,
            'items_per_page': model.per_page,
        }

    def transform_single(self):
        return self.data.value


class KeyValueExtractor(DataExtractor):
    """ Extract both keys and values from the data """

    def extract(self, objects):
        return {
            'meta': self._get_meta(objects),
            'data': {doc.key:doc.value for doc in objects.items}
        }


class KeyExtractor(DataExtractor):
    """ Extract only the keys form the data """

    def extract(self, objects):
        return {
            'meta': self._get_meta(objects),
            'data': [doc.key for doc in objects.items]
        }


class ValueExtractor(DataExtractor):
    """ Extract only the values form the data """

    def extract(self, objects):

        return {
            'meta': self._get_meta(objects),
            'data': [doc.value for doc in objects.items]
        }
