

from src.domain.repository.event_repository import EventRepository


class EventProcessor():
    def __init__(self, event_repository: EventRepository) -> None:
        self.event_repository = event_repository

    def execute(self, ):
        messages = self.event_repository.get_messages()
        if not messages:
            return []

        for message in messages:
            message_saved =  self.event_repository.save_message(message.producer, message.code, message.name, message.amount)
            if message_saved:
                deleted_message = self.event_repository.delete_message(message.receipt_handle)
            return message
        return messages
