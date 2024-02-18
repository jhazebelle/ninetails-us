
# Defining Functions

def add_contact(address_book, info):
    address_book.append(info)
    print(f"{info} added to the address book.")


def remove_contact(address_book, info):
    if info in address_book:
        address_book.remove(info)
        print(f"{info} removed from the address book.")


def view_contacts(address_book):
    print("Address Book:")
    for info in address_book:
        print('-', info)


def clear_contacts(address_book):
    address_book.clear()
    print("Address book cleared.")




def main():
    address_book = []

    while True:

        print("\n1. Add Contact")
        print("2. Remove Contact")
        print("3. View Contacts")
        print("4. Clear Contacts")
        print("5. Exit")


        choice = input("Choose an action: ")

        if choice == "1":
            info = input("Enter the name.phonenumber to add: ")
            add_contact(address_book, info)
        elif choice == "2":
            info = input("Enter the name.phonenumber to remove: ")
            remove_contact(address_book, info)
        elif choice == "3":
            view_contacts(address_book)
        elif choice == "4":
            clear_contacts(address_book)
        elif choice == "5":
            print ("Exiting address book")
            break 

        else:
            print("Invalid option. Please try choosing a number from the list of choices.")


if __name__ == "__main__":
    main()