from collections import UserDict
from datetime import date
from typing import List, Optional
import copy

class Phone(str):
    pass

class Name(str):
    pass

class Birthday:
    def __init__(self, year: int, month: int, day: int):
        self.value = date(year, month, day)

    def __repr__(self):
        return f"Birthday({self.value.isoformat()})"

class Record:
    def __init__(self, name: Name, phones: Optional[List[Phone]] = None, birthday: Optional[Birthday] = None):
        self.name = name
        self.phones = phones or []
        self.birthday = birthday

    def add_phone(self, phone: Phone):
        self.phones.append(phone)

    def remove_phone(self, phone: Phone):
        self.phones = [p for p in self.phones if p != phone]

    def __repr__(self):
        return f"Record(name={self.name!r}, phones={self.phones!r}, birthday={self.birthday!r})"

    # Приклад підтримки копіювання: глибока копія запису
    def copy(self):
        return copy.deepcopy(self)

class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name] = record

    def find(self, name: str) -> Optional[Record]:
        return self.data.get(name)

    def delete(self, name: str) -> bool:
        return self.data.pop(name, None) is not None

    # Повернемо глибоку копію книги (для безпечних маніпуляцій)
    def clone(self):
        return copy.deepcopy(self)