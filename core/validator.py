from .exceptions import InvalidRequest

MAX_KEY_LENGTH = 64
MAX_KEY_VALUE = 256


class Validator:
    """ Main validator for key and value query string params """
    errors = []

    def __init__(self, **kwargs):
        self.key = None
        self.value = None

        if 'key' in kwargs:
            self.key = kwargs['key'] or ''

        if 'value' in kwargs:
            self.value = kwargs['value'] or ''

    def validate(self):
        # todo extract to methods
        if self.key is not None and (len(self.key) == 0 or
                                     len(self.key) > MAX_KEY_LENGTH):
            self.errors.append('Invalid key parameter')

        if self.value is not None and (len(self.value) == 0 or
                                       len(self.value) > MAX_KEY_VALUE):
            self.errors.append('Invalid value parameter')

    def hasErrors(self):
        return len(self.errors) > 0

    def getError(self):
        # get the first error
        return self.errors.pop(0)


def validate(**kwargs):
    validator = Validator(**kwargs)
    validator.validate()

    if validator.hasErrors():
        error = validator.getError()
        raise InvalidRequest(error)
