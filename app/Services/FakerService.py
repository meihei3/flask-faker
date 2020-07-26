from faker import Faker
from services.fakerError import FakerError
from fakerProviders.personProvider import PersonProvider
from fakerProviders.utils import TransactionNameIndex
from collections import namedtuple


DEFAULT_LANG = 'ja_JP'


class FakerService:
    FEMALE = 'female'
    MALE = 'male'
    ALL = 'all'
    PersonFunctions = namedtuple('PersonFunctions', [
        'name', 'kana_name', 'romanized_name',
        'last_name', 'last_kana_name', 'last_romanized_name',
        'first_name', 'first_kana_name', 'first_romanized_name',
        'sex',
    ])

    def __init__(self, seed: str = None, count: str = None):
        self.__error = None
        self.__seed = seed
        self.__count = count

        self.faker = Faker(DEFAULT_LANG)
        self.faker.seed_instance(self.__seed)
        self.faker.add_provider(PersonProvider)

    def execute(self, func: str):
        # 気持ち悪いので将来的には直す
        if func == 'person':
            return self.person()
        elif func == 'person_female':
            return self.person_female()
        elif func == 'person_male':
            return self.person_male()

    @property
    def error(self):
        return self.__error

    def __set_error(self, err):
        self.__error = err

    def person(self):
        if (self.__count is None):
            return self.__generate_person()
        return [self.__generate_person() for _ in range(self.__count)]

    def person_female(self):
        if (self.__count is None):
            return self.__generate_person(self.FEMALE)
        return [self.__generate_person(self.FEMALE) for _ in range(self.__count)]

    def person_male(self):
        if (self.__count is None):
            return self.__generate_person(self.MALE)
        return [self.__generate_person(self.MALE) for _ in range(self.__count)]

    def __generate_person(self, sex: str = ALL):
        index = TransactionNameIndex(self.faker.pyint(), self.faker.pyint())
        caller = self.__generate_person_functions(sex)
        return {
            'name': caller.name(index),
            'kana_name': caller.kana_name(index),
            'romanized_name': caller.romanized_name(index),
            'last_name': caller.last_name(index),
            'last_kana_name': caller.last_kana_name(index),
            'last_romanized_name': caller.last_romanized_name(index),
            'first_name': caller.first_name(index),
            'first_kana_name': caller.first_kana_name(index),
            'first_romanized_name': caller.first_romanized_name(index),
            'sex': caller.sex(index),
        }

    def __generate_person_functions(self, sex: str) -> PersonFunctions:
        if sex == self.ALL:
            return FakerService.PersonFunctions(
                name=self.faker.indexed_name,
                kana_name=self.faker.indexed_kana_name,
                romanized_name=self.faker.indexed_romanized_name,
                last_name=self.faker.indexed_last_name,
                last_kana_name=self.faker.indexed_last_kana_name,
                last_romanized_name=self.faker.indexed_last_romanized_name,
                first_name=self.faker.indexed_first_name,
                first_kana_name=self.faker.indexed_first_kana_name,
                first_romanized_name=self.faker.indexed_first_romanized_name,
                sex=self.faker.indexed_sex,
            )
        elif sex == self.FEMALE:
            return FakerService.PersonFunctions(
                name=self.faker.indexed_name_female,
                kana_name=self.faker.indexed_kana_name_female,
                romanized_name=self.faker.indexed_romanized_name_female,
                last_name=self.faker.indexed_last_name,
                last_kana_name=self.faker.indexed_last_kana_name,
                last_romanized_name=self.faker.indexed_last_romanized_name,
                first_name=self.faker.indexed_first_name_female,
                first_kana_name=self.faker.indexed_first_kana_name_female,
                first_romanized_name=self.faker.indexed_first_romanized_name_female,
                sex=lambda _: self.FEMALE,
            )
        else:
            return FakerService.PersonFunctions(
                name=self.faker.indexed_name_male,
                kana_name=self.faker.indexed_kana_name_male,
                romanized_name=self.faker.indexed_romanized_name_male,
                last_name=self.faker.indexed_last_name,
                last_kana_name=self.faker.indexed_last_kana_name,
                last_romanized_name=self.faker.indexed_last_romanized_name,
                first_name=self.faker.indexed_first_name_male,
                first_kana_name=self.faker.indexed_first_kana_name_male,
                first_romanized_name=self.faker.indexed_first_romanized_name_male,
                sex=lambda _: self.MALE,
            )
