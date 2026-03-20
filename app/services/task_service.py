from schemas import MessageModel, UserDataModel, PriorityTask
from core import get_priority, NotifierProtocol, PriorityTaskNotFoundError

from enum import Enum

class TaskNotificationService:
    """
    This is a to-do notification service.
    
    This service sends notifications according to the notification priority.
    
    Methods:
        notify_for_priority(notification_priority: Enum | str, message: str, user_data: UserDataModel)
            
            This method sends notifications according to the notification priority.
            
                The notification priority could be 'high', 'medium', 'low'.
    """
    
    def __init__(self, whatsapp: NotifierProtocol, sms: NotifierProtocol,
            email: NotifierProtocol, log: NotifierProtocol
            ):
        self.strategies = {
            PriorityTask.HIGH: [whatsapp, email, sms],
            PriorityTask.MEDIUM: [email, sms],
            PriorityTask.LOW: [log]
        }
        
    async def notify_for_priority(
        self, notification_priority: Enum | str, message: str, user_data: UserDataModel
        ):
        
        message_obj = MessageModel(message=message)
        priority = get_priority(notification_priority)
        notifiers = self.strategies.get(notification_priority)
        
        if not notifiers:
            raise PriorityTaskNotFoundError(notification_priority)
        
        import asyncio
        taks = [n.send(message_obj, user_data) for n in notifiers]
        await asyncio.gather(**taks)
        
        
        
