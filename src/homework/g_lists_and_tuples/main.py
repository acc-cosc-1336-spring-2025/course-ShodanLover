from dictionary import get_p_distance_matrix

def display_matrix(matrix):
    for row in matrix:
        print(' '.join(f"{val:.5f}" for val in row))

def main():
    while True:
        print("\n1 - Get p distance matrix\n2 - Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            n = int(input("Enter number of sequences (max 10): "))
            sequences = []
            for i in range(n):
                seq = input(f"Enter DNA sequence {i+1}: ").strip().upper()
                sequences.append(list(seq))
            matrix = get_p_distance_matrix(sequences)
            print("\nP Distance Matrix:")
            display_matrix(matrix)
        elif choice == "2":
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
