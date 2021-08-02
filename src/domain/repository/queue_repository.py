from abc import ABC, abstractmethod
from typing import Dict, Any


class QueueRepository(ABC):

    @abstractmethod
    def get_messages(self, ) -> Dict[str, Any]:
        pass

    @abstractmethod
    def prepare_message(self, response: str) -> Dict[str, Any]:
        pass

    @abstractmethod
    def delete_message(self, ):
        pass