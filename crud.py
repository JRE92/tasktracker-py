import json
import os

def add_task():
    print("Add task")
    task = input("Enter task: ")
    while True:
        status = input("Enter status (todo/done/inprogress): ")
        if status == "todo" or "done" or "inprogress":
            break
        else:
            print("Invalid status")
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
        new_id = max(task["ID"] for task in tasks) + 1
    else:
        tasks = []
        new_id = 1

    new_task = {"ID": new_id, "name": task, "status": status}
    tasks.append(new_task)

    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)
    f.close()
def view_tasks():
    print("View tasks")
    if not os.path.exists("tasks.json"):
        print("No tasks available")
        return
    else:
        with open("tasks.json", "r") as f:
            data = json.load(f)
        while True:
            status = input("Enter status (todo/done/inprogress): ")
            if status == "todo":
                for x in data:
                    if x["status"] == "todo":
                        print(f"ID: {x['ID']}, Task: {x['name']}, Status: {x['status']}")
                break
            if status == "done":
                for x in data:
                    if x["status"] == "done":
                        print(f"ID: {x['ID']}, Task: {x['name']}, Status: {x['status']}")
                break
            if status == "inprogress":
                for x in data:
                    if x["status"] == "inprogress":
                        print(f"ID: {x['ID']}, Task: {x['name']}, Status: {x['status']}")
                break
            else:
                print("Invalid status")            
    f.close()
def update_tasks():
    print("Update tasks")
    if not os.path.exists("tasks.json"):
        print("No tasks available")
        return
    else:
        input_id = int(input("Enter ID: "))
        with open("tasks.json", "r") as f:
            data = json.load(f)
        for x in data:
            if x["ID"] == input_id:
                new_status = input("Enter new status (todo/done/inprogress): ")
                x["status"] = new_status
                with open("tasks.json", "w") as f:
                    json.dump(data, f, indent=4)
                    f.close()
                return  
        print("Invalid ID")
        f.close()
        return
def delete_tasks():
    print("Delete tasks")
    if not os.path.exists("tasks.json"):
        print("No tasks available")
        return
    else:
        input_id = int(input("Enter ID: "))
        with open("tasks.json", "r") as f:
            data = json.load(f)
        for x in data:
            if x["ID"] == input_id:
                data.remove(x)
                with open("tasks.json", "w") as f:
                    json.dump(data, f, indent=4)
                    f.close()
                return
        print("Invalid ID")
        f.close()
        return