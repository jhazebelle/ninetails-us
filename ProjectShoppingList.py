### SHOPPING LIST MANAGER ###


#Features:
#Add items: Users can add items to their shopping list.
#Remove items: Users can remove items from their shopping list.
#View list: Users can view their current shopping list.
#Clear list: Users can clear the entire shopping list.
#Save and load list: Option to save the shopping list to a file and load it back later.
#Check items off: Users can mark items as purchased.

def add_item(shopping_list, item):
    shopping_list.append(item)
    print(f"{item} added to the shopping list.")
# line12: def = defines a function, add_item = the function named, shopping_list and item = parameters
# line13: in the shopping_list, append = add, (item) name of the item you are adding
# line14: a message is displayed stating the item was added to the shopping list using f-string formatting
    

def remove_item(shopping_list, item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed from the shopping list.")
    else:
        print(f"{item} is not in the shopping list.")
# line20: a function named remove_item is defined, with parameters shopping_list and item
# line21: the chosen item is checked if it exists in the shopping list
# line22: in the shopping list, remove_item = remove, (item) item stated to be removed from the list
# line23: a confirming message is displayed stating item was removed from the list
# line24: if the item does not exist in the list, the next line is executed
# line25: a message is displayed confirming the item is not in the list 


def view_list(shopping_list):
    print("Shopping List:")
    for item in shopping_list:
        print("-", item)
# line34: a function named view_list is defined, with the parameter 'shopping_list' 
# line35: prints a title of "Shopping List" above the list
# line36: this line goes through each item in the list
# line37: each item is then printed to screen with a'-' to organize the list into bullet points


def clear_list(shopping_list):
    shopping_list.clear()
    print("Shopping list cleared.")
# line44: a function named clear_list is defined, with the parameter 'shopping_list' 
# line45: this takes all items in the list and clears it
# line46: a message is then printed to screen showing that the list is cleared

def main():
    shopping_list = []

    while True:
# line51: this line defines the main function, which is the entry point of the program
# line52: a container is created under the name shopping_list
# line54: this is an infinite loop, leading the user to the main page until the user chooses '5'

        print("\n1. Add item")
        print("2. Remove item")
        print("3. View list")
        print("4. Clear list")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            item = input("Enter the item to add: ")
            add_item(shopping_list, item)
        elif choice == "2":
            item = input("Enter the item to remove: ")
            remove_item(shopping_list, item)
        elif choice == "3":
            view_list(shopping_list)
        elif choice == "4":
            clear_list(shopping_list)
        elif choice == "5":
            print("Exiting...")
            break #exits the while True loop, which will then display the menu continuously until the user
                    #chooses '5'
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
# line83: this checks if the script is being executed as the main program
    #__name__ is a variable that holds the name of the current module
    # when the script is executed, '__name__' for that script is "__main__" if it is the entry point
    # of the program, or the script being directly executed
# line84: this line calls the main function or the main home page, 
    # main() is inside line83 so it's only executed if the script is being run directly,
    # calling main() starts the execution of the program by using the main() function which has the
    # main logic of the program