
# 15.	Write a menu driven program to show Union, Intersect, Difference, Symmetric difference operations on set.
def main():
    set1 = set(map(int, input("Enter elements of Set 1 separated by space: ").split()))
    set2 = set(map(int, input("Enter elements of Set 2 separated by space: ").split()))

    while True:
        print("\nSet Operations Menu:")
        print("1. Union")
        print("2. Intersection")
        print("3. Difference (Set 1 - Set 2)")
        print("4. Symmetric Difference")
        print("5. Exit")

        choice = int(input("Enter your choice (1-5): "))

        if choice == 1:
            result = set1.union(set2)
            operation = "Union"
        elif choice == 2:
            result = set1.intersection(set2)
            operation = "Intersection"
        elif choice == 3:
            result = set1.difference(set2)
            operation = "Difference (Set 1 - Set 2)"
        elif choice == 4:
            result = set1.symmetric_difference(set2)
            operation = "Symmetric Difference"
        elif choice == 5:
            print("Exiting program")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
            continue

        print(f"Result of {operation}: {result}")

if __name__ == "__main__":
    main()
