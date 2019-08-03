from abc import ABC, abstractmethod


class Task(ABC):
    def __init__(self, title, creator,  due_date, assignee = None):
        self.title = title
        self.creator = creator
        self.assignee = assignee
        self.due_date = due_date
        self.sprint = None

    def is_completed(self):
        return self.status.next_status is None

    @abstractmethod
    def set_task_type(self):
        pass

    def change_status(self, status):
        if self.is_completed():
            raise Exception(f"{self.title} is already completed")
        if self.status.next_status.name == status:
            self.status = self.status.next_status
            return 
        raise Exception(f"{status} can't be set as next status")

    def change_assignee(self, assignee):
        self.assignee = assignee

    def is_overdue(self, current_date):
        if current_date > self.due_date:
            return True
        return False

    def add_to_sprint(self, sprint_name):
        self.sprint = sprint_name

    def __str__(self):
        if self.sprint is None:
            return f"   Title => {self.title}\n    Sprint => No Sprint" + "\n"
        return f"   Title => {self.title}\n    Sprint => {self.sprint.title}"+ "\n"

    def __repr__(self):
        if self.sprint is None:
            return f"   Title => {self.title}\n    Sprint => No Sprint"+ "\n"
        return f"   Title => {self.title}\n    Sprint => {self.sprint.title}"+ "\n"
