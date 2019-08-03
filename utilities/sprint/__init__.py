from datetime import datetime
class Sprint:
    
    def __init__(self, title):
        self.title = title
        self.tasks = {}
        
    def add_task(self, task):
        if task.title in self.tasks:
            raise Exception(f"{task.title} already added to sprint")
        task.sprint = self
        self.tasks[task.title] = task
        
    def remove_task(self, task):
        if task.title not in self.tasks:
            raise Exception(f"{task.title} not added to sprint")
        task.sprint = None
        del self.tasks[task.title]
    
    def display_sprint(self):
        print(self.title + ":")
        delayed_tasks = []
        other_tasks = []
        for task in self.tasks.values():
            if task.is_overdue(datetime.now()):
                delayed_tasks.append(task.title)
            else:
                other_tasks.append(task.title)
        
        print("on track tasks :\n")
        print("\n".join(other_tasks))
        print("Delayed tasks :\n")
        print("\n".join(delayed_tasks))
        
    
    