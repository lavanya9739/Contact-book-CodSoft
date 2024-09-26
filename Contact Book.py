contacts = {}

def add_contact():
    name = input("Enter your contact name: ")
    phone = input("Enter your phone number: ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")
    contacts[name] = {"phone": phone, "email": email, "address": address}
    print(f"Contact {name} added successfully.")

def view_contacts():
    if contacts:
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}")
    else:
        print("No contacts found.")

def search_contact():
    search = input("Search by name or phone number: ")
    for name, details in contacts.items():
        if search == name or search == details['phone']:
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
            return
    print("Contact not found.")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        address = input("Enter new address: ")
        contacts[name] = {"phone": phone, "email": email, "address": address}
        print(f"Contact {name} updated successfully.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\n1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
