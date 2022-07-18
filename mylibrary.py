"""
All The Cool Functions
"""

__version__ = "0.1.0"


class InvalidKindError(Exception):
    """Raised if the kind is invalid."""
    pass


def get_books(kind=None):
    """
    Return a list of random books as strings.
    :param kind: Optional "kind" of ingredients.
    :type kind: list[str] or None
    :raise mylibrary.InvalidKindError: If the kind is invalid.
    :return: The books list.
    :rtype: list[str]
    """
    return ["harrypotter", "otherbookname", "mybook"]
