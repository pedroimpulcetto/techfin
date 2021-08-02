import time
from src.infrastructure.event import EventRepositoryMemory
from src.adapter.parser import Parser
from src.infrastructure.queue import Queue
from src.domain.usecase.event_processor import EventProcessor


def handler(event, context):
    queue = Queue()
    parser = Parser()
    repository = EventRepositoryMemory(parser, queue)
    message = EventProcessor(repository).execute()
    return message
