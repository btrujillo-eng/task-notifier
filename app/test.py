from services.notifier import WhatsappNotifier, SMSNotifier, EmailNotifier, LogNotifier
from services.task_service import TaskNotificationService
from schemas import UserDataModel, ContactInfoModel

contact_info = ContactInfoModel(email="trujillobrayan@ejemplo.com",phone_number="3238891686")
    

user_data = UserDataModel(user_name="Bryan", contact_info=contact_info)

service = TaskNotificationService(
    whatsapp=WhatsappNotifier(),
    sms=SMSNotifier(),
    email=EmailNotifier(),
    log=LogNotifier())

import asyncio

async def main():
    await service.notify_for_priority("high", "Haz tu tarea kbron no mmes", user_data=user_data)

if __name__ == "__main__":
    asyncio.run(main())