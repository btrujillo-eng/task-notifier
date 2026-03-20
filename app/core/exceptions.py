from uuid import UUID
from enum import Enum
from schemas import PriorityTask

class TaskNotFoundError(Exception):
    def __init__(self, task_id: UUID):
        self.task_id = task_id
        super().__init__(f"Task with id {task_id} not found")
        
class PriorityTaskError(Exception):
    def __init__(self, priority_task : PriorityTask):
        self.priority_task = priority_task
        super().__init__(f"The priority task {self.priority_task} not found")
        
class PriorityTaskNotFoundError(Exception):
    def __init__(self, notification_priority: Enum| str):
        super().__init__(f"The notification priority of type {notification_priority} not found")