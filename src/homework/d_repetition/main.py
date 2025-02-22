import repetition

def main():
    while True:
        print("\nHomework 3 Menu")
        print("1-Factorial")
        print("2-Sum odd numbers")
        print("3-Exit")
        
        choice = input("Select an option: ")

        if choice == "1":
            while True:
                num = int(input("Enter a number (1-9): "))
                if 1 <= num < 10:
                    print(f"Factorial of {num} is {repetition.get_factorial(num)}")
                    break
                print("Invalid input. Try again.")

        elif choice == "2":
            while True:
                num = int(input("Enter a number (1-99): "))
                if 1 <= num < 100:
                    print(f"Sum of odd numbers up to {num} is {repetition.sum_odd_numbers(num)}")
                    break
                print("Invalid input. Try again.")

        elif choice == "3":
            exit_choice = input("Are you sure you want to exit? (yes/no): ").strip().lower()
            if exit_choice == "yes":
                break

if __name__ == "__main__":
    main()
