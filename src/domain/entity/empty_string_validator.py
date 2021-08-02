def assert_string_is_not_empty(cls, s: str, field) -> str:
    s = s.strip()
    if len(s) == 0:
        raise ValueError(f'{field.name.capitalize()} should not empty!')
    return s
