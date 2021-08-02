from pytest import raises

from pydantic import ValidationError


def test_Payload_attribute_producer_is_a_valid_string(payload_factory):
    payload_factory(producer='one')

    with raises(ValidationError):
        payload_factory(producer=' ')
    with raises(ValidationError):
        payload_factory(producer='')
    with raises(ValidationError):
        payload_factory(producer=1)
    with raises(ValidationError):
        payload_factory(producer=1.0)
    with raises(ValidationError):
        payload_factory(producer=None)
    with raises(ValidationError):
        payload_factory(producer={})
    with raises(ValidationError):
        payload_factory(producer=[])


def test_Payload_attribute_code_is_a_valid_int(payload_factory):
    payload_factory(code=1)

    with raises(ValidationError):
        payload_factory(code='01')
    with raises(ValidationError):
        payload_factory(code=' ')
    with raises(ValidationError):
        payload_factory(code='')
    with raises(ValidationError):
        payload_factory(code=1.0)
    with raises(ValidationError):
        payload_factory(code=None)
    with raises(ValidationError):
        payload_factory(code={})
    with raises(ValidationError):
        payload_factory(code=[])


def test_Payload_attribute_name_is_a_valid_string(payload_factory):
    payload_factory(name='pedro')

    with raises(ValidationError):
        payload_factory(name=' ')
    with raises(ValidationError):
        payload_factory(name='')
    with raises(ValidationError):
        payload_factory(name=1)
    with raises(ValidationError):
        payload_factory(name=1.0)
    with raises(ValidationError):
        payload_factory(name=None)
    with raises(ValidationError):
        payload_factory(name={})
    with raises(ValidationError):
        payload_factory(name=[])


def test_Payload_attribute_amount_is_a_valid_float(payload_factory):
    payload_factory(amount=100.0)

    with raises(ValidationError):
        payload_factory(amount=' ')
    with raises(ValidationError):
        payload_factory(amount='')
    with raises(ValidationError):
        payload_factory(amount=1)
    with raises(ValidationError):
        payload_factory(amount='100.0')
    with raises(ValidationError):
        payload_factory(amount=None)
    with raises(ValidationError):
        payload_factory(amount={})
    with raises(ValidationError):
        payload_factory(amount=[])