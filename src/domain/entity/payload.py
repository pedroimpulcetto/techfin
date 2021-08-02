from uuid import UUID, uuid4

from pydantic import BaseModel, Field, constr, StrictFloat, StrictInt, validator

from .empty_string_validator import assert_string_is_not_empty

class Payload(BaseModel):
    uuid: UUID = Field(default_factory=uuid4)
    producer: constr(min_length=1, strict=True)
    code: StrictInt
    name: constr(min_length=1, strict=True)
    amount: StrictFloat
    receipt_handle: str

    _non_empty_validator = validator(
        'producer', 'name', allow_reuse=True
    )(assert_string_is_not_empty)