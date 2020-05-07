from .db import db


class KeyValueModel(db.Document):
    key = db.StringField(required=True, unique=True, max_length=64)
    value = db.StringField(required=True, max_length=256)
