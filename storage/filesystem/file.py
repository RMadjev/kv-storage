def init_file():
    open('storage/kv.txt', 'w+')


class FileStorage():

    def __init__(self):
        self.filename = 'storage/kv.txt'

    def set_key(self, key, value):
        raise NotImplementedError

    def get_key(self, key):
        raise NotImplementedError

    def get_all(self):
        raise NotImplementedError

    def remove_key(self, key):
        raise NotImplementedError

    def remove_all(self, key):
        raise NotImplementedError
