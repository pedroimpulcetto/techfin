from pytest import fixture

from src.domain.repository.queue_repository import QueueRepository
from src.domain.entity import Payload

@fixture
def mockQueue(mocker):
    queue = mocker.Mock(QueueRepository)
    queue.get_messages.return_value = []
    queue.prepare_message.return_value = {}
    queue.delete_message.return_value = True
    return queue

@fixture
def payload_factory(payload_data):
    return _factory(cls=Payload, data=payload_data)

@fixture
def payload_data():
    return {
        'uuid': 'ea4c0c90-2c4f-41cb-bd35-5d3e3400cf64',
        'producer': 'one',
        'code': 1,
        'name': 'pedro',
        'amount': 100.0,
    }

def _factory(*, cls,  data={}):
    def _create_object(*, remove_field=None, **kwargs):
        fields = data.copy()
        fields.update(kwargs)
        if remove_field is not None:
           fields.pop(remove_field)
        return cls(**fields)
    return _create_object