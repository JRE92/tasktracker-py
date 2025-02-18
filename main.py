from crud import *
from views import *

def main():
    print_menu()
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            task = input("Enter task: ")
            status = input("Enter status (todo/done/inprogress): ")
            add_task(task, status)
        elif choice == "2":
            status = input("Enter status (todo/done/inprogress): ")
            data = view_tasks(status)
            show_tasks(data)
        elif choice == "3":
            input_id = int(input("Enter ID: "))
            new_status = input("Enter new status (todo/done/inprogress): ")
            update_tasks(input_id, new_status)
        elif choice == "4":
            input_id = int(input("Enter ID: "))
            delete_tasks(input_id)
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":  
    main()  # Call the main function    