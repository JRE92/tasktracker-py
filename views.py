from tabulate import tabulate

def print_menu():
    data = [[1, "Add task"],
            [2, "View tasks"],
            [3, "Update tasks"],
            [4, "Delete tasks"],
            [0, "Exit"]]
    headers = ["MENU", "OPTIONS"]
    print("-----------------")
    print(tabulate(data, headers=headers, tablefmt="simple"))
    print("-----------------")

def show_tasks(data):
    print("-----------------")
    print(tabulate(data, headers="keys", tablefmt="simple"))
    print("-----------------")