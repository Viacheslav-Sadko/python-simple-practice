import json
import os
from ctypes.wintypes import HTASK


class Todo:
    def __init__(self, task, priority):
        self.task = task
        self.priority = priority
        self.completed = False

    def __repr__(self):
        status = "✔️" if self.completed else "❌"
        return f"{self.task} (Priority: {self.priority}) - {status}"

    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        return {"task": self.task, "priority": self.priority, "completed": self.completed}

    @classmethod
    def from_dict(cls, data):
        return cls(data['task'], data['priority'])

def load_task(filename = "task.json"):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            tasks_data = json.load(file)
            return [Todo.from_dict(task) for task in tasks_data]
    return []

def save_tasks(tasks, filename = "task.json"):
    tasks_data = [task.to_dict() for task in tasks]
    with open(filename, 'w') as file:
        json.dump(tasks_data, file, indent=4)

def show_tasks(tasks):
    if tasks:
        print("\nYour Todo list:")
        for idx, task in enumerate(sorted(tasks, key = lambda x: x.priority)):
            print(f"{idx + 1}. {task}")
    else:
        print("No tasks found.")

def add_task(tasks):
    task_description = input("Enter the task descr. : ")
    priority = int(input("Enter the priority (1 to 5): "))
    task = Todo(task_description, priority)
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task_description}' added!")

def mark_task_completed(tasks):
    show_tasks(tasks)
    task_num = int(input("Enter the task number to mark as completed: "))
    if 0 <= task_num < len(tasks):
        tasks[task_num].mark_completed()
        save_tasks(tasks)
        print(f"Task '{tasks[task_num].task}' marked as completed!")
    else:
        print("Invalid task number.")
def main():
    tasks = load_task()
    while True:
        print("\n1. Show tasks\n2. Add task\n3. Mark task completed\n4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("\nInvalid choice. Please, try again.\n")

if __name__=="__main__":
    main()