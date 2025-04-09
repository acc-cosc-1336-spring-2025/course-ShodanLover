from dictionary import add_inventory, remove_inventory_widget

def main():
    inventory = {}
    while True:
        print("\nInventory Menu")
        print("1-Add or Update Item")
        print("2-Delete Item")
        print("3-Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            item_name = input("Enter widget name: ")
            try:
                quantity = int(input("Enter quantity: "))
                add_inventory(inventory, item_name, quantity)
                print(str(quantity) + " of " + item_name + " added/updated.")
            except ValueError:
                print("Invalid quantity.")
        elif choice == '2':
            item_name = input("Enter widget name to delete: ")
            result = remove_inventory_widget(inventory, item_name)
            print(result)
        elif choice == '3':
            print("Exiting.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()