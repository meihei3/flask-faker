from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class TransactionNameIndex:
    first: int
    last: int


@dataclass(frozen=True)
class TransactionAddressIndex:
    _format: int
    chome: int
    ban: int
    gou: int
    building_name: int
    building_number: int


__app_dir = Path(__file__).cwd()
zip_code_dir = __app_dir / Path('database/zipcode/docs/zip_code/')
