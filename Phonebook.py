contacts = {}


def add_contact(name, phone, email):
    contacts[phone] = {'name': name, 'phone': phone, 'email': email}
    print(f"Contact {name} added.")


def view_contacts():
    for info in contacts.values():
        print(
            f"Name: {info['name']}, Phone: {info['phone']}, Email: {info['email']}"
        )


def delete_contact(name):
    num = input("Enter the phone number : ")
    if num in contacts and contacts[num]['name'] == name:
        del contacts[num]
        print(f"Contact {name} deleted.")
    else:
        print("Contact not found.")


def update_contact(name):
    num = input("Enter the phone number : ")
    if num in contacts and contacts[num]['name'] == name:
        new_value = input(
            "What do you want to update  (name,phone number or email? ")
        if new_value.lower() == "name":
            new_name = input("What is the new name? ")
            contacts[num]['name'] = new_name
            print(f"Contact {name} updated to {new_name}")
        elif new_value.lower() == "phone number":
            new_num = input("What is the new number? ")
            contacts[new_num] = contacts[num]
            del contacts[num]
            contacts[new_num]['phone'] = new_num
            print(f"Contact number of {name} updated.")
        else:
            new_email = input("What is the new email? ")
            contacts[num]['email'] = new_email
            print(f"Email details of {name} updated.")
    else:
        print("Contact not found.")


def contact_book():
    while True:
        action = input("Choose action: add/view/delete/update/exit: ")
        if action == 'add':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            add_contact(name, phone, email)
        elif action == 'view':
            view_contacts()
        elif action == 'delete':
            name = input("Enter name to delete: ")
            delete_contact(name)
        elif action == 'update':
            name = input("Enter name to update contact details: ")
            update_contact(name)
        elif action == 'exit':
            break
        else:
            print("Invalid action.")


if __name__ == "__main__":
    contact_book()
