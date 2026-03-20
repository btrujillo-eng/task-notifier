from pydantic import BaseModel, Field, EmailStr
from enum import Enum
from uuid import UUID, uuid4 

class PriorityTask(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
   
class TaskModel(BaseModel):
    title : str = Field(min_length=3, max_length=100)
    priority : PriorityTask
    user_id : UUID
    
class TaskOut(TaskModel):
    task_id : UUID = Field(default_factory=uuid4)
    
    class Config:
        from_attributes = True

class MessageModel(BaseModel):
    message: str = Field(min_length=10, max_length=150)
    
class ContactInfoModel(BaseModel):
    email : EmailStr
    phone_number : str = Field(min_length=10, max_length=10, pattern=r"^\d+$")
    
class UserDataModel(BaseModel):
    user_name : str
    contact_info : ContactInfoModel