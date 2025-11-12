from functools import wraps
from .storage import save_data, DEFAULT_FILE

def autosave(book_attr: str = "book", filename=DEFAULT_FILE):
    """
    Декоратор для команд, які змінюють книгу.
    Очікується, що у функції-обгортці є об'єкт з атрибутом 'book' (або іншим).
    """
    def deco(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            result = func(self, *args, **kwargs)
            save_data(getattr(self, book_attr), filename)
            return result
        return wrapper
    return deco