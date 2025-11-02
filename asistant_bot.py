from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value: str):
        self._validate(value)
        super().__init__(value)

    @staticmethod
    def _validate(value: str):
        if not isinstance(value, str):
            raise ValueError("Phone must be a string of 10 digits")
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Phone must contain exactly 10 digits")

    @property
    def value(self) -> str:
        return self._value

    @value.setter
    def value(self, new_value: str):
        self._validate(new_value)
        self._value = new_value


class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones: list[Phone] = []

    def add_phone(self, phone: str):
        """Додає новий номер (рядок з 10 цифр) до списку телефонів."""
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str):
        """Видаляє перший збіг номера phone, якщо він існує."""
        ph = self.find_phone(phone)
        if ph:
            self.phones.remove(ph)

    def edit_phone(self, old_phone: str, new_phone: str):
        """
        Замінює перший збіг old_phone на new_phone (валідація у Phone.value)
        """
        ph = self.find_phone(old_phone)
        if ph:
            ph.value = new_phone

    def find_phone(self, phone: str) -> Phone | None:
        """Повертає об'єкт Phone або None, якщо не знайдено."""
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        phones = "; ".join(p.value for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones}"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        """Додає запис за ім’ям як ключем."""
        self.data[record.name.value] = record

    def find(self, name: str) -> Record | None:
        """Знаходить запис за ім’ям або повертає None."""
        return self.data.get(name)

    def delete(self, name: str):
        """Видаляє запис за ім’ям, якщо існує."""
        self.data.pop(name, None)
