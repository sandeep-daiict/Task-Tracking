from task import Task
from state import Status

class Feature(Task):
    # def set_status(self):
    #     status_deployed = Status("deployed", None)
    #     status_testing = Status("testing", status_deployed)
    #     status_progress = Status("in progress", status_testing)
    #     self.status = Status("open", status_progress)
    
    
    def set_task_type(self):
        self.task_type = "feature_task"
        
    def __init__(self, title, creator, due_date, summary, impact, status, assignee = None):
        self.summary = summary
        self.impact = impact
        self.set_task_type()
        super().__init__(title, creator, due_date, assignee)
        self.status = status.status
        

            
