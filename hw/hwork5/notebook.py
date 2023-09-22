import json


class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def edit_contact(self, name, new_phone, new_email):
        for contact in self.contacts:
            if contact.name == name:
                contact.phone = new_phone
                contact.email = new_email
                return
        print("Контакт не найден.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                return
        print("Контакт не найден.")

    def list_contacts(self):
        for contact in self.contacts:
            print(f"Имя: {contact.name}, Телефон: {contact.phone}, Email: {contact.email}")

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            data = [{'name': contact.name, 'phone': contact.phone, 'email': contact.email} for contact in self.contacts]
            json.dump(data, file)

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.contacts = [Contact(item['name'], item['phone'], item['email']) for item in data]
        except FileNotFoundError:
            print("Файл не найден. Создана новая адресная книга.")


def main():
    address_book = AddressBook()
    address_book.load_from_file('contacts.json')

    while True:
        print("\nВыберите действие:")
        print("1. Добавить контакт")
        print("2. Редактировать контакт")
        print("3. Удалить контакт")
        print("4. Показать все контакты")
        print("5. Сохранить и выйти")

        choice = input("Ваш выбор: ")

        if choice == "1":
            name = input("Введите имя: ")
            phone = input("Введите номер телефона: ")
            email = input("Введите адрес электронной почты: ")
            new_contact = Contact(name, phone, email)
            address_book.add_contact(new_contact)
            print("Контакт добавлен!")
        elif choice == "2":
            name = input("Введите имя контакта, который нужно отредактировать: ")
            new_phone = input("Введите новый номер телефона: ")
            new_email = input("Введите новый адрес электронной почты: ")
            address_book.edit_contact(name, new_phone, new_email)
        elif choice == "3":
            name = input("Введите имя контакта, который нужно удалить: ")
            address_book.delete_contact(name)
        elif choice == "4":
            address_book.list_contacts()
        elif choice == "5":
            address_book.save_to_file('contacts.json')
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите от 1 до 5.")


if __name__ == "__main__":
    main()
