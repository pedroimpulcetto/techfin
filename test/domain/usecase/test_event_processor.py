
from src.infrastructure.queue import Queue
from src.domain.repository.queue_repository import QueueRepository
from src.domain.entity.payload import Payload
from src.adapter.parser import Parser
from src.domain.usecase.event_processor import EventProcessor
from src.infrastructure.event import EventRepositoryMemory

def test_should_receive_a_message_of_type_payload_entity(mockQueue):
    parser = Parser()
    receiver = EventRepositoryMemory(parser, mockQueue)
    event_processor = EventProcessor(receiver)
    message = event_processor.execute()
    assert message == []