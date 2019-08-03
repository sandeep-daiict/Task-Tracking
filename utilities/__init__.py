from enum import Enum
from state import Status
from task import Task


class Impact(Enum):
    LOW = 'Low'
    MEDIUM = 'Medium'
    High = 'High'


class Severity(Enum):
    P0 = 'P0'
    P1 = 'P1'
    P2 = 'P2'


class SubTrack(Task):
    def __init__(self, title, status):
        self.title = title
        self.status = status
        super().__init__(title, "", None)

    def set_task_type(self):
        pass

    def add_to_sprint(self, sprint_name):
        pass
    

    def __str__(self):
        return f'SubTrack Title => {self.title}, Status = {self.status}'

    def __repr__(self):
        return f'SubTrack Title => {self.title}, Status = {self.status}'



class StatusManager:


    def change_status(self, current_status, status):
        if current_status.next is not None and current_status.next.name == status:
            return current_status.next
        raise Exception(f"{status} can't be set as next status")


class BugStatus(StatusManager):
    
    def __init__(self):
        status_fixed = Status("fixed", None)
        status_progress = Status("progress", status_fixed)

        self.status = Status("open", status_progress)

    
class FeatureStatus(StatusManager):

    def __init__(self):
        status_deployed = Status("deployed", None)
        status_testing = Status("testing", status_deployed)
        status_progress = Status("in progress", status_testing)
        self.status = Status("open", status_progress)


class StoryStatus(StatusManager):
    
    def __init__(self):
        status_fixed = Status("completed", None)
        status_progress = Status("in progress", status_fixed)
        self.status = Status("open", status_progress)