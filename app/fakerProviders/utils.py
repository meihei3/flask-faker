from dataclasses import dataclass


@dataclass(frozen=True)
class TransactionNameIndex:
    first: int
    last: int


@dataclass(frozen=True)
class TransactionAddressIndex:
    _format: int
    prefecture: int
    city: int
    town: int
    chome: int
    ban: int
    gou: int
    building_name: int
    building_number: int
