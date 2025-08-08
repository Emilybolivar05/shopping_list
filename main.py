shopping_list = []

while True:
    print("\n==== Shopping List Menu ====")
    print("1. Add an item")
    print("2. View shopping list")
    print("3. Remove an item")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        item = input("Enter the item to add: ").strip()
        if item:
            shopping_list.append(item)
            print(f"'{item}' has been added to your list.")
        else:
            print("Please enter a valid item.")

    elif choice == "2":
        if shopping_list:
            print("\nYour Shopping List:")
            for i, item in enumerate(shopping_list, start=1):
                print(f"{i}. {item}")
        else:
            print("Your shopping list is empty.")

    elif choice == "3":
        if shopping_list:
            try:
                number = int(input("Enter the number of the item to remove: "))
                if 1 <= number <= len(shopping_list):
                    removed = shopping_list.pop(number - 1)
                    print(f"'{removed}' has been removed.")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("Your shopping list is empty. Nothing to remove.")

    elif choice == "4":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 4.")