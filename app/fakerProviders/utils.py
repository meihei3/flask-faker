from dataclasses import dataclass


@dataclass(frozen=True)
class TransactionNameIndex:
    first: int
    last: int
