from crud import *
def print_menu():
    print("1. Add task")
    print("2. View tasks")
    print("3. Update tasks")
    print("4. Delete tasks")
    print("5. Exit")
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_tasks()
        elif choice == "4":
            delete_tasks()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice")
print_menu()