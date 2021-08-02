
import logging
from typing import Any, Dict, List

from src.domain.entity.payload import Payload
from src.infrastructure.queue import Queue
from src.adapter.parser import Parser
from src.domain.repository.event_repository import EventRepository

class EventRepositoryMemory(EventRepository):

    def __init__(self, parser: Parser, queue: Queue) -> None:
        self.parser = parser
        self.queue = queue
    
    def get_messages(self, ):
        messages = self.queue.get_messages()
        return self.__deserializer_message(messages)

    def __deserializer_message(self, messages: List[Dict[str, Any]]) -> List[Payload]:
        parsed_list_messages = []
        for message in messages:
            try:
                message = self.queue.prepare_message(message)
                parsed_message = self.parser.parse(message)
                parsed_list_messages.append(parsed_message)
            except Exception as ex:
                logging.exception(msg=str(ex))
                continue

        return parsed_list_messages

    def save_message(self, producer: str, code: int, name: str, amount: float) -> bool:
        pass

    def delete_message(self, message):
        return self.queue.delete_message(message)