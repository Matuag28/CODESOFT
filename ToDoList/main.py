tasks = []


def addTask():
    task = input("Enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")


def listTask():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks):
            print(f" #Tasks #{index}. {task}")


def deleteTask():
    listTask()
    try:
        taskToDelete = int(input("Choose the # of the task you want to delete: "))
        if taskToDelete >= 0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task {taskToDelete} deleted from the list.")
        else:
            print(f"Task # {taskToDelete} is not in the list.")
    except:
        print("Invalid input")


if __name__ == "__main__":
    ### Create a loop to run the app
    print("WElcome to the to do list app :) ")
    while True:
        print("\n")
        print("Please select one of the following options :")
        print("-------------------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List task")
        print("4. Quite")

        choice = input("Enter your choice :")
        if (choice == "1"):
            addTask()
        elif (choice == "2"):
            deleteTask()
        elif (choice == "3"):
            listTask()
        elif (choice == "4"):
            break
        else:
            print("Invalid choice")

        print("Goodbye !!")
