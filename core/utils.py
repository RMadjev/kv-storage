DEFAULT_PAGE = 1
DEFAULT_PER_PAGE = 10
MAX_PER_PAGE = 1000


def get_pagination(arguments):
    """ Get pagination properties from the request arguments """
    page = arguments.get('page', default=DEFAULT_PAGE, type=int)
    per_page = arguments.get('per_page', default=DEFAULT_PER_PAGE, type=int)

    if per_page > MAX_PER_PAGE:
        per_page = MAX_PER_PAGE

    return (page, per_page)
