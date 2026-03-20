from core import NotifierProtocol
from schemas import MessageModel, UserDataModel

class WhatsappNotifier(NotifierProtocol):
    async def send(self, message: MessageModel, user_data: UserDataModel) -> MessageModel:
        phone_number = user_data.contact_info.phone_number
        print(f"[WhatsApp] send to {phone_number}: {message.message}")
        return message.message
    
class SMSNotifier(NotifierProtocol):
    async def send(self, message: MessageModel, user_data: UserDataModel) -> MessageModel:
        phone_number = user_data.contact_info.phone_number
        print(f"[SMS] send to {phone_number}: {message.message}")
        return message
    
class EmailNotifier(NotifierProtocol):
    async def send(self, message: MessageModel, user_data: UserDataModel) -> MessageModel:
        email = user_data.contact_info.email
        print(f"[Email] send to {email}: {message}")
        return message.message
    
class LogNotifier(NotifierProtocol):
    async def send(self, message: MessageModel, user_data: UserDataModel) -> MessageModel:
        user_name = user_data.user_name
        phone_number = user_data.contact_info.phone_number
        print(f"[Log] to {user_name} with phone number {phone_number}")
        return message.message