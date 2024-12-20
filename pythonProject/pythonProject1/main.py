class Task:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __init__(self):
        status = "Completed" if self.completed else "Not Completed"
        return f"Task: {self.title}\nDescription: {self.description}\nDeadline: {self.deadline}\nStatus: {status}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, deadline):
        task = Task(title, description, deadline)
        self.tasks.append(task)
        print(f"Task '{title}' added.")

    def remove_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print(f"Task '{title}' removed.")
                return
        print(f"Task '{title}' not found.")

    def mark_task_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_completed()
                print(f"Task '{title}' marked as completed.")
                return
        print(f"Task '{title}' not found.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                print(task)
                print("-" * 20)


manager = TaskManager()
manager.add_task("Write Code", "Write the code for TaskManager", "2024-12-25")
manager.add_task("Test Code", "Test the TaskManager functionality", "2024-12-26")
manager.list_tasks()
manager.mark_task_completed("Write Code")
manager.list_tasks()
manager.remove_task("Test Code")
manager.list_tasks()
