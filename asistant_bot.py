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
        digits = "".join(ch for ch in value if ch.isdigit())
        if len(digits) != 10 or not digits.isdigit():
            raise ValueError("Phone must contain exactly 10 digits")

    @property
    def value(self) -> str:
        return self._value

    @value.setter
    def value(self, new_value: str):
        self._validate(new_value)
        self._value = "".join(ch for ch in new_value if ch.isdigit())


class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones: list[Phone] = []

    def add_phone(self, phone: str):
        """Додає телефон (рядок) до списку телефонів."""
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str):
        """Видаляє телефон, що дорівнює значенню phone."""
        norm = Phone(phone).value
        self.phones = [p for p in self.phones if p.value != norm]

    def edit_phone(self, old_phone: str, new_phone: str):
        """Заміна першої появи old_phone на new_phone."""
        old_norm = Phone(old_phone).value
        new_obj = Phone(new_phone)
        for i, p in enumerate(self.phones):
            if p.value == old_norm:
                self.phones[i] = new_obj
                return
        # якщо не знайдено — нічого не робимо

    def find_phone(self, phone: str) -> str | None:
        """Повертає телефон (рядок) або None, якщо не знайдено."""
        norm = Phone(phone).value
        for p in self.phones:
            if p.value == norm:
                return p.value
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


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
