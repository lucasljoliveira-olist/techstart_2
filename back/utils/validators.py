from typing import Type


def validate_type(value: object, type: Type, key: str):
    if not isinstance(value, type):
            raise TypeError(f"{key.capitalize()} must be {type}.")


def validate_greater_than(value: float, key: str, min_value: float):
    if value < min_value:
        raise ValueError(f"Value can't be lower than {min_value}.")


def validate_lenght(value: object, max_len: int, key: str):
    if len(value) > max_len:
        raise ValueError(f"{key.capitalize()} can't be greater than {max_len} characters.")


def validate_not_empty(value: str, key: str):
    if not value.strip():
        raise ValueError(f"{key.capitalize()} can't be empty.")
