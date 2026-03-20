from enum import Enum
from schemas import PriorityTask
from core.exceptions import PriorityTaskError

def get_priority(priority: Enum | str) -> PriorityTask:
    if isinstance(priority, str):
        try:
            return PriorityTask(priority.strip().lower())
        except ValueError:
            raise PriorityTaskError(priority)
    return priority
    