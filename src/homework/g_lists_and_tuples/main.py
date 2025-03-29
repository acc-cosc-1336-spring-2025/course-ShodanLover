def get_lowest_list_value(numbers):
    lowest = numbers[0]
    for num in numbers:
        if num < lowest:
            lowest = num
    return lowest

def get_highest_list_value(numbers):
    highest = numbers[0]
    for num in numbers:
        if num > highest:
            highest = num
    return highest

def main():
    numbers = []
    
    while True:
        print("1- Show the list low/high values")
        print("2- Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            while True:
                num = int(input("Enter a list value: "))
                numbers.append(num)
                
                if len(numbers) >= 3:
                    cont = input("Do you want to enter another value? (yes/no): ")
                    if cont.lower() != "yes":
                        break
            
            print(f"Lowest value: {get_lowest_list_value(numbers)}")
            print(f"Highest value: {get_highest_list_value(numbers)}")
        
        elif choice == "2":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
