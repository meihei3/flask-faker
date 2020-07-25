from faker import Faker
from faker.config import AVAILABLE_LOCALES
from services.fakerError import FakerError
from fakerProviders.personProvider import PersonProvider
from fakerProviders.utils import TransactionNameIndex


class FakerService:
    SEED = 'seed'
    COUNT = 'count'

    def __init__(self, seed: str = None, count: str = None):
        self.__error = None
        self.__seed = seed
        self.__count = count

        self.faker = Faker()
        self.faker.seed_instance(self.__seed)
        self.faker.add_provider(PersonProvider)

    def execute(self, func: str):
        # 気持ち悪いので将来的には直す
        if func == 'person':
            return self.person()

    @property
    def error(self):
        return self.__error

    def __set_error(self, err):
        self.__error = err

    def person(self):
        if (self.__count is None):
            return self.__generate_person()
        return [self.__generate_person() for _ in range(self.__count)]

    def __generate_person(self):
        index = TransactionNameIndex(self.faker.pyint(), self.faker.pyint())
        return {
            'name': self.faker.indexed_name(index),
            'kana_name': self.faker.indexed_kana_name(index),
            'last_name': self.faker.indexed_last_name(index),
            'last_kana_name': self.faker.indexed_last_kana_name(index),
            'last_romanized_name': self.faker.indexed_last_romanized_name(index),
            'first_name': self.faker.indexed_first_name(index),
            'first_kana_name': self.faker.indexed_first_kana_name(index),
            'first_romanized_name': self.faker.indexed_first_romanized_name(index),
            'sex': self.faker.indexed_sex(index),
        }
