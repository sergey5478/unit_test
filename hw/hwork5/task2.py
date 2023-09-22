"""*Задание 2.
*Ниже список тестовых сценариев. Ваша задача - определить
тип каждого теста (юнит-тест, интеграционный тест, сквозной тест) и
объяснить, почему вы так решили.

1. Проверка того, что функция addContact корректно добавляет новый контакт
в список контактов."""

"""Этот тест является юнит-тестом.
Тест проверяет функциональность конкретного метода add_contact, который, 
по всей видимости, является частью какого-то класса (например, AddressBook).
Поскольку он тестирует отдельный метод, а не взаимодействие между разными 
компонентами или классами, это юнит-тест.
Пример на Python:"""
from notebook import AddressBook, Contact, main


def test_add_contact(self):
    address_book = AddressBook()
    contact = Contact("John Doe", "555-1234", "john@example.com")
    address_book.add_contact(contact)
    len(address_book.contacts) == 1


"""2. Проверка того, что при добавлении контакта через пользовательский 
интерфейс, контакт корректно отображается в списке контактов."""

"""Этот сценарий также представляет собой юнит-тест.
В данном сценарии тестируется корректность отображения контакта в списке 
после его добавления через пользовательский интерфейс. Это не требует 
взаимодействия с другими частями системы или внешних компонентов, поэтому 
тест является юнит-тестом."""

import unittest
from unittest.mock import patch

class TestAddressBook(unittest.TestCase):

    @patch('builtins.input', side_effect=["1", "John Doe", "555-1234", "john@example.com", "5"])
    def test_ui_add_contact(self, mock_input):
        address_book = AddressBook()
        address_book.add_contact(Contact("Jane Doe", "555-5678", "jane@example.com"))
        main()
        self.assertEqual(len(address_book.contacts), 2)
        self.assertEqual(address_book.contacts[0].name, "Jane Doe")
        self.assertEqual(address_book.contacts[1].name, "John Doe")

"""3. Проверка полного цикла работы с контактом: создание контакта, его
редактирование и последующее удаление."""

"""Этот сценарий представляет собой сквозной тест.
В данном сценарии мы проверяем целостность и корректность всего цикла работы 
с контактом — от создания, через редактирование, до удаления. Этот тест 
проверяет, как все эти функции работают вместе, а не отдельно. Поэтому это сквозной тест.
Пример на Python:"""


def test_full_contact_lifecycle(self):
    address_book = AddressBook()
    contact = Contact("John Doe", "555-1234", "john@example.com")
    address_book.add_contact(contact)
    assert len(address_book.contacts) == 1
    assert address_book.contacts[0].name == "John Doe"
    address_book.edit_contact("John Doe", "555-5678", "john_new@example.com")
    edited_contact = address_book.contacts[0]
    assert edited_contact.phone == "555-5678"
    assert edited_contact.email == "john_new@example.com"
    address_book.delete_contact("John Doe")
    assert len(address_book.contacts) == 0
