from strings import get_hamming_distance, get_dna_complement


def main():
    while True:
        print("\nMenu:")
        print("1 - Hamming Distance")
        print("2 - DNA Complement")
        print("3 - Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            dna1 = input("Enter the first DNA string: ").strip()
            dna2 = input("Enter the second DNA string: ").strip()
            
            if len(dna1) != len(dna2):
                print("Error: DNA strings must be of equal length.")
            else:
                print(f"Hamming Distance: {get_hamming_distance(dna1, dna2)}")

        elif choice == "2":
            dna = input("Enter a DNA string: ").strip()
            print(f"DNA Complement: {get_dna_complement(dna)}")

        elif choice == "3":
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
