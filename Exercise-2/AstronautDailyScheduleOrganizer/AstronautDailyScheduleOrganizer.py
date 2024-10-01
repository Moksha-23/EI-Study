from datetime import datetime

class Task:
    def __init__(self, description, start_time, end_time, priority):
        self.description = description
        self.start_time = datetime.strptime(start_time, '%H:%M')
        self.end_time = datetime.strptime(end_time, '%H:%M')
        self.priority = priority
        self.completed = False
    
    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.start_time.strftime('%H:%M')} - {self.end_time.strftime('%H:%M')}: {self.description} [{self.priority}] ({status})"
    
    def mark_as_completed(self):
        self.completed = True
class TaskFactory:
    @staticmethod
    def create_task(description, start_time, end_time, priority):
        return Task(description, start_time, end_time, priority)
class ScheduleManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ScheduleManager, cls).__new__(cls)
            cls._instance.tasks = []
        return cls._instance

    def add_task(self, task):
        if self._check_task_conflict(task):
            print(f"Error: Task conflicts with an existing task.")
        else:
            self.tasks.append(task)
            print(f"Task '{task.description}' added successfully.")

    def _check_task_conflict(self, new_task):
        for task in self.tasks:
            if (task.start_time < new_task.end_time and new_task.start_time < task.end_time):
                print(f"Conflict with task: {task}")
                return True
        return False

    def remove_task(self, description):
        task_to_remove = next((task for task in self.tasks if task.description == description), None)
        if task_to_remove:
            self.tasks.remove(task_to_remove)
            print(f"Task '{description}' removed successfully.")
        else:
            print("Error: Task not found.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks scheduled for the day.")
            return
        self.tasks.sort(key=lambda x: x.start_time)
        for task in self.tasks:
            print(task)

    def view_tasks_by_priority(self, priority):
        priority_tasks = [task for task in self.tasks if task.priority == priority]
        if not priority_tasks:
            print(f"No tasks with priority '{priority}'.")
            return
        priority_tasks.sort(key=lambda x: x.start_time)
        for task in priority_tasks:
            print(task)
    
    def mark_task_as_completed(self, description):
        task_to_complete = next((task for task in self.tasks if task.description == description), None)
        if task_to_complete:
            task_to_complete.mark_as_completed()
            print(f"Task '{description}' marked as completed.")
        else:
            print(f"Error: Task '{description}' not found.")
#Example usage
if __name__ == "__main__":
    schedule_manager = ScheduleManager()
    task1 = TaskFactory.create_task("Morning Exercise", "07:00", "08:00", "High")
    schedule_manager.add_task(task1)
    task2 = TaskFactory.create_task("Team Meeting", "09:00", "10:00", "Medium")
    schedule_manager.add_task(task2)
    schedule_manager.view_tasks()
    schedule_manager.remove_task("Morning Exercise")
    task3 = TaskFactory.create_task("Training Session", "09:30", "10:30", "High")
    schedule_manager.add_task(task3)  
    schedule_manager.view_tasks()
    schedule_manager.mark_task_as_completed("Team Meeting")
    schedule_manager.view_tasks_by_priority("High")
