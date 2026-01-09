contacts = {}
phone_numbers = set()


def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")

    if phone in phone_numbers:
        print("Phone number already exists.")
        return

    contacts[name] = phone
    phone_numbers.add(phone)
    print("Contact added successfully.")


def view_contacts():
    if not contacts:
        print("No contacts available.")
        return

    print("\nContact List")
    print("-" * 30)
    for name, phone in contacts.items():
        print(f"Name: {name} | Phone: {phone}")


def search_contact():
    name = input("Enter name to search: ")

    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Contact not found.")


def delete_contact():
    name = input("Enter contact name to delete: ")

    if name in contacts:
        phone_numbers.remove(contacts[name])
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")


def contact_manager():
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Exiting Contact Manager.")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    contact_manager()