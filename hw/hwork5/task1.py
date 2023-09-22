"""*Задание 1.
*Представьте, что вы работаете над разработкой простого
приложения для записной книжки, которое позволяет пользователям добавлять,
редактировать и удалять контакты.
Ваша задача - придумать как можно больше различных тестов (юнит-тесты,
интеграционные тесты, сквозные тесты) для этого приложения. Напишите название
каждого теста, его тип и краткое описание того, что этот тест проверяет."""

import json

from notebook import AddressBook, Contact


def test_add_contact(self):
    """Тип: Юнит-тест
    Описание: Проверяет, что метод add_contact корректно добавляет
    контакт в адресную книгу."""
    address_book = AddressBook()
    contact = Contact("John Doe", "555-1234", "john@example.com")
    address_book.add_contact(contact)
    assert len(address_book.contacts) == 1


def test_edit_contact(self):
    """Тип: Юнит-тест
    Описание: Проверяет, что метод edit_contact правильно редактирует контакт."""
    address_book = AddressBook()
    contact = Contact("John Doe", "555-1234", "john@example.com")
    address_book.add_contact(contact)
    address_book.edit_contact("John Doe", "555-5678", "john_new@example.com")
    edited_contact = address_book.contacts[0]
    assert edited_contact.phone == "555-5678"
    assert edited_contact.email == "john_new@example.com"


def test_delete_contact(self):
    """Тип: Юнит-тест
    Описание: Проверяет, что метод delete_contact удаляет контакт."""
    address_book = AddressBook()
    contact = Contact("John Doe", "555-1234", "john@example.com")
    address_book.add_contact(contact)
    address_book.delete_contact("John Doe")
    assert len(address_book.contacts) == 0


def test_load_from_file(self):
    """Тип: Интеграционный тест
    Описание: Проверяет, что адресная книга правильно загружает контакты из файла."""
    address_book = AddressBook()
    address_book.load_from_file('contacts.json')
    assert len(address_book.contacts) == 2


def test_save_to_file():
    """Тип: Интеграционный тест
    Описание: Проверяет, что адресная книга правильно сохраняет контакты в файл."""
    address_book = AddressBook()
    contact1 = Contact("John Doe", "555-1234", "john@example.com")
    contact2 = Contact("Jane Doe", "555-5678", "jane@example.com")
    address_book.add_contact(contact1)
    address_book.add_contact(contact2)
    address_book.save_to_file('test_save_contacts.json')
    with open('test_save_contacts.json', 'r') as file:
        data = json.load(file)
        assert len(data) == 2

test_save_to_file()
def test_add_edit_delete_contact(self):
    """Тип: Сквозной тест
    Описание: Сочетание последовательности действий: добавление, редактирование
    и удаление контакта. Проверяет, что все операции работают вместе корректно."""
    address_book = AddressBook()
    contact = Contact("John Doe", "555-1234", "john@example.com")
    address_book.add_contact(contact)
    address_book.edit_contact("John Doe", "555-5678", "john_new@example.com")
    address_book.delete_contact("John Doe")
    assert len(address_book.contacts) == 0


def test_add_edit_delete_multiple_contacts(self):
    """Тип: Сквозной тест
    Описание: Добавление нескольких контактов, их редактирование и удаление.
    Проверяет, что приложение правильно обрабатывает множество контактов."""
    address_book = AddressBook()
    contact1 = Contact("John Doe", "555-1234", "john@example.com")
    contact2 = Contact("Jane Doe", "555-5678", "jane@example.com")
    address_book.add_contact(contact1)
    address_book.add_contact(contact2)
    address_book.edit_contact("John Doe", "555-5678", "john_new@example.com")
    address_book.delete_contact("Jane Doe")
    assert len(address_book.contacts) == 1


def test_load_from_empty_file(self):
    """Тип: Сквозной тест
    Описание: Проверяет, что приложение корректно обрабатывает ситуацию,
    когда файл с контактами пустой или отсутствует."""
    address_book = AddressBook()
    address_book.load_from_file('empty_contacts.json')
    assert len(address_book.contacts) == 0
