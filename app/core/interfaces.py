from typing import Protocol, List
from uuid import UUID
from schemas import TaskModel, TaskOut, MessageModel, UserDataModel

class TaskRepositoryProtocol(Protocol):
    """
    Interface for task persistence operations.
    
    Any class that implement this protocol must define 
    the methods 'save', 'get_by_id' and 'list_all'.
    
    Methods:
        save(task_date: TaskModel) -> TaskOut
            
            persists a new task.
            
        get_by_id(id: int) -> TaskOut
            
            Retrieves a task by it ID.
    """
    
    def save(self, task_date: TaskModel) -> TaskOut: ...

    def get_by_id(self, id: UUID) -> TaskOut: ...
    
    def list_all(self) -> List[TaskOut]: ...
 
class NotifierProtocol(Protocol):
    """
    Interface for send notification to users.
    
    Any class that implement this protocol must define
    the method 'send'.
    
    Methods:
        send(message: MessageModel) -> MessageModel
            
            This send a notication or notifications with a predetermined message.
    """
    
    def send(self, message: MessageModel, user_data: UserDataModel) -> MessageModel: ...