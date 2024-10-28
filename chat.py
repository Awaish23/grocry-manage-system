# Define an empty list to store items
items = []

# Function to display the list
def display_items():
    if items:
        print("\nCurrent Items in the List:")
        for i, item in enumerate(items, start=1):
            print(f"{i}. {item}")
    else:
        print("\nThe list is empty.")

# Function to add an item to the list
def add_item():
    item = input("\nEnter the item to add: ")
    items.append(item)
    print(f"'{item}' has been added to the list.")

# Function to delete an item from the list
def delete_item():
    display_items()
    if items:
        try:
            item_index = int(input("\nEnter the item number to delete: ")) -1

            if 0 <= item_index < len(items):
                removed_item = items.pop(item_index)
                print(f"'{removed_item}' has been deleted from the list.")
            else:
                print("Invalid item number.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("No items to delete.")

# Main program loop
def menu():
    while True:
        print("\nOptions:")
        print("1. Display List")
        print("2. Add Item")
        print("3. Delete Item")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ")

        if choice == '1':
            display_items()
        elif choice == '2':
            add_item()
        elif choice == '3':
            delete_item()
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# Run the menu
if __name__ == "__main__":
    menu()
