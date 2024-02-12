# 14.Write a menu driven program to implement Add, Delete, Append, View and Quit operation on list.

myList = [22, 7, 16, 11, 21]

while True:
    print("The list 'myList' has the following elements:", myList)
    print("1. Add an element")
    print("2. Delete an element")
    print("3. Append elements")
    print("4. View the list")
    print("5. Quit")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        element = int(input("Enter the element to be inserted: "))
        pos = int(input("Enter the position: "))
        myList.insert(pos, element)
        print("The element has been inserted\n")

    elif choice == 2:
        element = int(input("\nEnter the element to be deleted: "))
        if element in myList:
            myList.remove(element)
            print("\nThe element", element, "has been deleted\n")
        else:
            print("\nElement", element, "is not present in the list")

    elif choice == 3:
        newList = eval(input("Enter the elements separated by commas: "))
        myList.extend(list(newList))
        print("The list has been appended\n")

    elif choice == 4:
        print("\nThe list is:", myList)

    elif choice == 5:
        break

    else:
        print("Choice is not valid")

    print("\nPress Enter to continue.")
    input()
