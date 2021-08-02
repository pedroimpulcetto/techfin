

from typing import Dict, Any

from src.domain.entity import Payload


class Parser():
    def __init__(self, ) -> None:
        self.__message_data = {}

    def parse(self, message: Dict[str, Any]) -> Payload:
        try:
            return self.__parse_and_create_payload(message)
        except ValueError as ex:
            raise ex
    
    def __parse_and_create_payload(self, message):
        self.__parse_message(message)
        return self.__create_payload()

    def __parse_message(self, message: Dict[str, Any]):
        self.__message_data['producer'] = str(message.get('producer', None))
        self.__message_data['code'] = int(message.get('code', None))
        self.__message_data['name'] = str(message.get('name', None))
        self.__message_data['amount'] = float(message.get('amount', None))
        self.__message_data['receipt_handle'] = str(message.get('receipt_handle', ''))

    def __create_payload(self, ) -> Payload:
        return Payload(**self.__message_data)