def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter the item to add: ").strip().capitalize()  # Capitalize the first letter of the item
            if item:
                shopping_list.append(item) # Add item to the list
                print(f"'{item}' has been added to your shopping list.")
            else:
                print("Item name cannot be empty.")

        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter the item to remove: ").strip().capitalize()
            if item in shopping_list:
                shopping_list.remove(item) # Remove item from the list
                print(f"'{item}' has been removed from your shopping list.")
            else:
                print(f"'{item}' not found in the shopping list.")

        elif choice == '3':
            # Display the shopping list
            if len(shopping_list) == 0:
                print("Your shopping list is empty.")
            else:
                print("\nCurrent Shopping List:")
                i = 1  # Start counting from 1
                for item in shopping_list:
                    print(str(i) + ". " + item)
                    i += 1
                    
        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()