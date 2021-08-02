
from abc import ABC, abstractmethod

class EventRepository(ABC):

    @abstractmethod
    def get_messages(self, ):
        pass

    @abstractmethod
    def save_message(self, producer: str, code: int, name: str, amount: float) -> bool:
        pass

    @abstractmethod
    def delete_message(self, ) -> bool:
        pass
