from flask_mongoengine import MongoEngine
from core.exceptions import NoItemFound
from .extractors import DataExtractor, KeyExtractor, \
    KeyValueExtractor, ValueExtractor

db = MongoEngine()


def init_db(app):
    db.init_app(app)


# main model registered in the database
from .models import KeyValueModel


class DatabaseStorage:
    def set(self, key, value):
        pair = KeyValueModel(key=key)
        pair.update(value=value, upsert=True)

    def get(self, key):
        kv = self._get_single_data_or_404(key)

        extractor = DataExtractor(kv)
        return extractor.transform_single()

    def _get_data_or_404(self, page, per_page):
        try:
            data = KeyValueModel.objects.paginate(page, per_page)
        except:
            raise NoItemFound

        return data

    def _get_single_data_or_404(self, key):
        try:
            kv = KeyValueModel.objects.get_or_404(key=key)
        except:
            raise NoItemFound

        return kv

    def get_all(self, page, per_page):
        data = self._get_data_or_404(page, per_page)
        extractor = KeyValueExtractor(data)
        return extractor.extract(data)

    def get_all_values(self, page, per_page):
        data = self._get_data_or_404(page, per_page)
        extractor = ValueExtractor(data)
        return extractor.extract(data)

    def get_all_keys(self, page, per_page):
        data = self._get_data_or_404(page, per_page)
        extractor = KeyExtractor(data)
        return extractor.extract(data)

    def remove(self, key):
        kv = self._get_single_data_or_404(key)
        kv.delete()

    def remove_all(self):
        KeyValueModel.objects.delete()
