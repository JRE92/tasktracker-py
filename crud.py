import json
import os

def add_task(task, status):
    print("Add task")
    while True:
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
def view_tasks(status):
    data = []
    if not os.path.exists("tasks.json"):
        print("No tasks available")
        return
    else:
        with open("tasks.json", "r") as f:
            file = json.load(f)
        while True:
            if status == "todo":
                for x in file:
                    if x["status"] == "todo":
                        data.append(x)
                break
            if status == "done":
                for x in file:
                    if x["status"] == "done":
                        data.append(x)
                break
            if status == "inprogress":
                for x in file:
                    if x["status"] == "inprogress":
                        data.append(x)
                break
            else:
                print("Invalid status")            
    f.close()
    return data
def update_tasks(input_id, new_status):
    print("Update tasks")
    if not os.path.exists("tasks.json"):
        print("No tasks available")
        return
    else:
        with open("tasks.json", "r") as f:
            data = json.load(f)
        for x in data:
            if x["ID"] == input_id:
                x["status"] = new_status
                with open("tasks.json", "w") as f:
                    json.dump(data, f, indent=4)
                    f.close()
                return  
        print("Invalid ID")
        f.close()
        return
def delete_tasks(input_id):
    print("Delete tasks")
    if not os.path.exists("tasks.json"):
        print("No tasks available")
        return
    else:
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