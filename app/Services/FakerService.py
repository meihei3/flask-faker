from faker import Faker
from faker.config import AVAILABLE_LOCALES
from services.fakerError import FakerError
from fakerProviders.personProvider import PersonProvider
from fakerProviders.utils import TransactionNameIndex


DEFAULT_LANG = 'ja_JP'


class FakerService:
    LANG = 'lang'
    SEED = 'seed'
    COUNT = 'count'

    def __init__(self, lang=DEFAULT_LANG, seed=None, count=None):
        self.__error = None
        self.__lang = lang
        self.__seed = seed
        self.__count = count
        self.__validate(lang=lang, seed=seed, count=count)

        self.faker = Faker()
        self.faker.seed_instance(self.__seed)
        self.faker.add_provider(PersonProvider)

    def execute(self, func):
        if func == 'person':
            return self.person()

    @property
    def error(self):
        return self.__error

    def __set_error(self, err):
        self.__error = err

    def person(self):
        name = self.faker.last_name()
        return self.__generate_person(name)

    def __generate_person(self, name: list):
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

    def __validate(self, **kwargs):
        for key, val in kwargs.items():
            if key == self.LANG:
                self.__validation_lang(val)
            elif key == self.SEED:
                self.__validation_seed(val)
            elif key == self.COUNT:
                self.__validation_count(val)

    def __validation_lang(self, value):
        if value not in AVAILABLE_LOCALES:
            self.__lang = DEFAULT_LANG

    def __validation_seed(self, value):
        if not self.__is_none_or_int(value):
            self.__seed = None

    def __validation_count(self, value):
        if not self.__is_none_or_int(value):
            self.__count = None

    def __is_none_or_int(self, value):
        return value is None or isinstance(value, int)
