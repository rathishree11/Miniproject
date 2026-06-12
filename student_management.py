students = {}
while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        name = input("Enter student name: ")
        mark = input("Enter mark: ")
        students[name] = mark
    elif choice == "2":
        for name, mark in students.items():
            print(name, "-", mark)
    elif choice == "3":
        break
    else:
        print("Invalid Choice")
