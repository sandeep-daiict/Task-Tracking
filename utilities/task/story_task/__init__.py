from task import Task
from state import Status

class Story(Task):
    
    # def set_status(self):
    #     status_fixed = Status("completed", None)
    #     status_progress = Status("in progress", status_fixed)
    #     self.status = Status("open", status_progress)

    def set_task_type(self):
        self.task_type = "story_task"

    def __init__(self, title, creator,  due_date, story_summary, status,  assignee = None):
        self.story_summary = story_summary
        self.set_task_type()
        self.sub_tracks = []
        super().__init__(title, creator, due_date, assignee)
        self.status = status.status

    def add_subtrack(self, sub_track):
        self.sub_tracks.append(sub_track)


    def __str__(self):

        if self.sprint is None:
            return f"   Title => {self.title}\n     Sprint => No Sprint\n Sub Tracks => " + "\n     ".join([st.title for st in self.sub_tracks]) + "\n"
        return f"   Title => {self.title}\n     Sprint => {self.sprint.title}\n Sub Tracks => " + "\n     ".join([st.title for st in self.sub_tracks]) + "\n"
