from task import Task
from state import Status

class Bug(Task):

    # def set_status(self):
    #     status_fixed = Status("fixed", None)
    #     status_progress = Status("progress", status_fixed)
    #
    #     self.status = Status("open", status_progress)

    def set_task_type(self):
        self.task_type = "bug_task"

    def __init__(self, title, creator, due_date, severity, status, assignee = None):
        self.severity = severity
        self.set_task_type()
        super().__init__(title, creator, due_date, assignee)
        self.status = status.status




