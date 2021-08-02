import json
from typing import Any, Dict, List

import boto3

from src.domain.repository.queue_repository import QueueRepository


class Queue(QueueRepository):
    def __init__(self) -> None:
        self.url = 'http://localhost:4566/000000000000/pismo-queue'
        self.service = boto3.client(service_name='sqs', endpoint_url='http://localhost:4566')

    def get_messages(self, ) -> List[Dict[str, Any]]:
        response = self.service.receive_message(
            QueueUrl=self.url,
            AttributeNames=[
                'SentTimestamp'
            ],
            MaxNumberOfMessages=1,
            MessageAttributeNames=[
                'All'
            ],
            VisibilityTimeout=0,
            WaitTimeSeconds=0
        )
        return response.get('Messages', {})

    def prepare_message(self, response: str) -> Dict[str, Any]:
        response = json.loads(response.get('Body', {}))
        return json.loads(response.get('Message', {}))

    def delete_message(self, receipt_handle) -> bool:
        response = self.service.delete_message(
            QueueUrl=self.url,
            ReceiptHandle=receipt_handle,
        )
        return True if response else False
