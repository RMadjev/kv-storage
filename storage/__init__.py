"""
This module inits the configured storage
    db - use mongodb as storage engine
    file - use the filesystem as storage engine
"""
from .database.db import init_db, DatabaseStorage
from .filesystem.file import init_file, FileStorage


def register_storage(app):
    config_storage = app.config['STORAGE']
    if config_storage == 'db':
        init_db(app)
    elif config_storage == 'file':
        init_file()


def get_storage(config_storage):
    if config_storage == 'db':
        return DatabaseStorage()
    elif config_storage == 'file':
        return FileStorage()
