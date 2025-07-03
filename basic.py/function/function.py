contacts = {}

def add_contact(name, phone):
    contacts[name] = phone
    print(f"Contact {name} added.")

# delete a contact 
def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"contact {name} deleted.")
    else:
        print("contact not found.")


def search_contact(name):
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Contact not found.")

def display_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
def exit_contact_book():
    print("Exiting Contact Book.")
    exit()

def contact_book():
    while True:
        print("\n1. add contact \n2. delete contact \n3. search contact \n4. display contacts \n5. exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            add_contact(name, phone) 
        elif choice == "2":
            name = input("Enter name to search: ")
            search_contact(name)
        elif choice == "3":
            display_contacts()
        elif choice == "4":
            display_contacts = input("Do you want to display all contacts? (yes/no): ")
            if display_contacts.lower() == "yes":
                display_contacts()
            else:
                print("skipping display of contacts.")
        elif choice == "5":
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice. Please try again.")

contact_book()