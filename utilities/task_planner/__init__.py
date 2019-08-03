from task.bug_task import Bug
from task.feature_task import Feature
from task.story_task import Story
from utilities import SubTrack
from enum import Enum
from datetime import datetime
from sprint import Sprint
from utilities import BugStatus, FeatureStatus, StoryStatus
class TaskPlanner:
    
    def __init__(self):
        self.tasks = {} # title to task mapping
        self.sprints = {} # sprint name to list of tasks title mapping
        self.user_tasks = {}
        
    def create_task(self, task_type, assignee, title, creator, due_date,
                    feature_summary, severity,
                    story_summary, impact):

        task = self.tasks.get(title, None)
        if task is not None:
            raise Exception(f"{title} task already added")

        if task_type == 'bug_task':
            status = BugStatus()
            task = Bug(title, creator,  due_date, severity, status,assignee)
        
        if task_type == 'feature_task':
            status = FeatureStatus()
            task = Feature(title,  creator,  due_date, feature_summary, impact, status, assignee)
            
        if task_type == 'story_task':
            status = StoryStatus()
            task = Story(title,  creator,  due_date, story_summary, status, assignee)

        self.tasks[title] = task
        if assignee is not None:
            tasks = self.user_tasks.get(assignee, [])
            tasks.append(task)
            self.user_tasks[assignee] = tasks
        
    
    def create_sub_task(self, title_subtask, title_task):
        task = self.tasks.get(title_task, None)
        if task is None:
            raise Exception(f"{title_task} not present")
        
        if task.task_type != 'story_task':
            raise Exception(f"{title_task} is not story_task")
        
        if task.is_completed():
            raise Exception(f"{title_task} is completed")
        status = StoryStatus()
        sub_task = SubTrack(title_subtask, status)
        task.add_subtrack(sub_task)
        

    
    def change_status_task(self, title_task, new_status):
        task = self.tasks.get(title_task, None)
        if task is None:
            raise Exception(f"{title_task} not present")

        task.change_status(new_status)


    
    def change_assignee_task(self, title_task, assignee):
        task = self.tasks.get(title_task, None)
        if task is None:
            raise Exception(f"{title_task} not present")
        task.assignee = assignee

    
    def display_tasks_user_type(self, assigned_user, task_type):
        user_tasks = self.user_tasks.get(assigned_user, [])
        delayed_tasks = []
        other_tasks = []
        for task in user_tasks:
            if task_type is not None and task.task_type != task_type:
                continue

            if task.is_overdue(datetime.now()):
                delayed_tasks.append(task.title)
            else:
                other_tasks.append(task.title)
        print(f"Tasks for user {assigned_user} for type {task_type}")
        print("on track tasks :")
        print("\n".join(other_tasks))
        print("Delayed tasks :")
        print("\n".join(delayed_tasks))

    def display_tasks_user_all(self, assigned_user):
        user_tasks = self.user_tasks.get(assigned_user, [])
        tasks_map = {}
        for task in user_tasks:
            tasks = tasks_map.get(task.task_type, [])
            tasks.append(task)
            tasks_map[task.task_type] = tasks

        print(f"user=>{assigned_user}")
        for key, value in tasks_map.items():
            print(f"task_type: {key}")
            for ts in value:
                print(str(ts))

    
    def create_sprint(self, sprint_name):
        if sprint_name in self.sprints:
            raise Exception(f'{sprint_name} already exsists')
        sprint = Sprint(sprint_name)
        self.sprints[sprint_name] = sprint

    def delete_sprint(self, sprint_name):
        if sprint_name not in self.sprints:
            raise Exception(f'{sprint_name} does not exsists')
        sprint = self.sprints[sprint_name]
        for task_title in sprint.tasks:
            task = self.tasks.get(task_title)
            task.sprint = None

        self.sprints[sprint_name] = None

    def add_task_to_sprint(self, title_task, sprint_name):
        task = self.tasks.get(title_task, None)
        if task is None:
            raise Exception(f"{title_task} not present")
        if sprint_name not in self.sprints:
            raise Exception(f'{sprint_name} does not exsists')
            
        sprint = self.sprints[sprint_name]
        sprint.add_task(task)
    
    def remove_task_from_sprint(self, title_task, sprint_name):
        task = self.tasks.get(title_task, None)
        if task is None:
            raise Exception(f"{title_task} not present")
        if sprint_name not in self.sprints:
            raise Exception(f'{sprint_name} does not exsists')
        task.sprint = None
        sprint = self.sprints[sprint_name]
        sprint.remove_task(task)
        
    
    def display_sprint(self, sprint_name):
        if sprint_name not in self.sprints:
            raise Exception(f'{sprint_name} does not exsists')

        sprint = self.sprints[sprint_name]
        if sprint is None:
            raise Exception(f'{sprint_name} does not exsists')
        sprint.display_sprint()

    def is_completed_task(self, title_task):
        task = self.tasks.get(title_task, None)
        if task is None:
            raise Exception(f"{title_task} not present")

        print(task.is_completed())

class TaskType(Enum):
    BUG_TYPE = "bug_task"
    FEATURE_TYPE = "feature_task"
    STORY_TYPE = "story_task"


if __name__ == '__main__':

    task_planner = TaskPlanner()
    task_planner.create_task(TaskType.BUG_TYPE.value,"sandeep", "bug_1", "rajat",
                             datetime(2019,5,19), "testing", "P0", "test", "low")

    task_planner.create_task(TaskType.STORY_TYPE.value, "sandeep", "story_1", "rajat",
                             datetime(2019, 7, 19), "testing", "P1", "test story", "high")

    task_planner.create_task(TaskType.STORY_TYPE.value, "sandeep", "story_4", "rajat",
                             datetime(2019, 10, 19), "testing", "P0", "check module", "high")

    task_planner.create_task(TaskType.FEATURE_TYPE.value, "sandeep", "feature_1", "rajat",
                             datetime(2019, 11, 19), "testing", "P1", "ch", "low")

    task_planner.create_task(TaskType.STORY_TYPE.value, "rahul", "story_2", "rajat",
                             datetime(2019, 8, 19), "testing", "P1", "test", "medium")

    task_planner.create_task(TaskType.FEATURE_TYPE.value, "rahul", "feature_2", "rajat",
                             datetime(2019, 6, 19), "testing", "P1", "test", "high")
    
    task_planner.create_task(TaskType.FEATURE_TYPE.value, "rahul", "feature_3", "rajat",
                             datetime(2019, 8, 19), "testing", "P2", "check low", "")

    task_planner.create_task(TaskType.STORY_TYPE.value, "kuldeep", "story_3", "rajat",
                             datetime(2019, 8, 19), "testing", "P2", "check", "high")

    print("\n###(1)####\n")
    task_planner.display_tasks_user_type("sandeep", TaskType.STORY_TYPE.value)
    print("\n####(2)###\n")
    task_planner.display_tasks_user_all("sandeep")

    try:
        task_planner.create_sprint("sprint_1")
        task_planner.create_sprint("sprint_2")
        task_planner.create_sprint("sprint_1")
    except Exception as e:
        print("\n###(3)####\n")
        print(str(e))

    task_planner.add_task_to_sprint("story_1", "sprint_1")
    task_planner.add_task_to_sprint("story_2", "sprint_1")
    task_planner.add_task_to_sprint("feature_1", "sprint_1")
    task_planner.add_task_to_sprint("feature_2", "sprint_1")
    task_planner.add_task_to_sprint("bug_1", "sprint_2")

    try:
        task_planner.create_sub_task("subtask1", "story_1")
        task_planner.create_sub_task("subtask2", "story_1")
        task_planner.create_sub_task("subtask3", "story_1")
        task_planner.create_sub_task("subtask4", "bug_1")
    except Exception as e:
        print("\n####(4)###\n")
        print(str(e))
        pass

    print("\n###(5)####\n")
    task_planner.display_sprint("sprint_1")
    print("\n###(6)####\n")
    task_planner.display_sprint("sprint_2")

    print("\n####(7)###\n")
    task_planner.display_tasks_user_all("sandeep")

    print("\n####(8)###\n")
    try:
        task_planner.change_status_task("bug_1", "open")
    except Exception as e:
        print("\n####(9)###\n")
        print(str(e))
    try:
        task_planner.change_status_task("bug_1", "progress")
        task_planner.change_status_task("bug_1", "fixed")
        task_planner.change_status_task("bug_1", "open")
    except Exception as e:
        print("\n###(10)####\n")
        print(str(e))

    print("\n####(11)###\n")
    task_planner.display_tasks_user_type("kuldeep", TaskType.STORY_TYPE.value)

    task_planner.is_completed_task("bug_1")
    task_planner.is_completed_task("feature_1")


    task_planner.delete_sprint("sprint_2")
    try:
        task_planner.display_sprint("sprint_2")
    except Exception as e:
        print("\n###(12)####\n")
        print(str(e))

    task_planner.remove_task_from_sprint("feature_2", "sprint_1")
    print("\n###(13)####\n")
    task_planner.display_sprint("sprint_1")