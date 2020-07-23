from faker import Faker
from faker.config import AVAILABLE_LOCALES
from Services.FakerError import FakerError
from faker.providers.person.ja_JP import Provider
DEFAULT_LANG = 'ja_JP'


class FakerService:
    LANG = 'lang'
    SEED = 'seed'

    def __init__(self, lang=DEFAULT_LANG, seed=None):
        print(Provider.first_names_male)
        self.__error = None
        self.validate(lang=lang, seed=seed)

        if (self.error is None):
            self.faker = Faker(lang)
            self.faker.seed_instance(seed)

    def execute(self):
        raise NotImplementedError

    def validate(self, **kwargs):
        for key, item in kwargs.items():
            if (key == self.LANG):
                self.__validate_lang(item)
            elif (key == self.SEED):
                self.__validation_seed(item)

    def __validate_lang(self, value):
        if (value not in AVAILABLE_LOCALES):
            self.__set_error(FakerError.NOT_SUPPORTED_LANG)

    def __validation_seed(self, value):
        if (value is not None and not isinstance(value, int)):
            self.__set_error(FakerError.NOT_INTEGER_TYPE)

    def __set_error(self, err):
        self.__error = err

    @property
    def error(self):
        return self.__error
