import pickle
from pathlib import Path
from typing import Optional
from .models import AddressBook

DEFAULT_FILE = Path("addressbook.pkl")

def save_data(book: AddressBook, filename: Path = DEFAULT_FILE) -> None:
    filename = Path(filename)
    tmp = filename.with_suffix(filename.suffix + ".tmp")
    # Атомічний запис: спочатку у тимчасовий файл, потім rename
    with open(tmp, "wb") as f:
        pickle.dump(book, f, protocol=pickle.HIGHEST_PROTOCOL)
    tmp.replace(filename)

def load_data(filename: Path = DEFAULT_FILE) -> AddressBook:
    filename = Path(filename)
    if not filename.exists():
        return AddressBook()
    with open(filename, "rb") as f:
        data = pickle.load(f)
        # Додатковий запобіжник на випадок пошкодженого вмісту
        if not isinstance(data, AddressBook):
            return AddressBook()
        return data