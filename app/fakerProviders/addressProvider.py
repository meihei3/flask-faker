from faker.providers.address.ja_JP import Provider
from fakerProviders.utils import TransactionAddressIndex, zip_code_dir
from typing import Tuple
from pathlib import PosixPath
import json
import os
import random


class AddressProvider(Provider):
    number_kana = (
        'ｾﾞﾛ', 'ｲﾁ', 'ﾆ', 'ｻﾝ', 'ﾖﾝ', 'ｺﾞ', 'ﾛｸ', 'ﾅﾅ', 'ﾊﾁ', 'ｷｭｳ', 'ｼﾞｭｳ'
    )

    building_names = (
        'ストークマンション', 'ヴェールコート', 'スカイハイツ', 'バーミープレイス', 'オーチャードヒル',
        'ルナコート', 'パールハイツ', 'フォレストメゾン', 'グリーンサイト', 'テラスハウス'
    )

    building_names_kana = (
        'ｽﾄｰｸﾏﾝｼｮﾝ', 'ｳﾞｪｰﾙｺｰﾄ', 'ｽｶｲﾊｲﾂ', 'ﾊﾞｰﾐｰﾌﾟﾚｲｽ', 'ｵｰﾁｬｰﾄﾞﾋﾙ',
        'ﾙﾅｺｰﾄ', 'ﾊﾟｰﾙﾊｲﾂ', 'ﾌｫﾚｽﾄﾒｿﾞﾝ', 'ｸﾞﾘｰﾝｻｲﾄ', 'ﾃﾗｽﾊｳｽ'
    )

    _format_size = 3
    chome_size = 42
    ban_size = 27
    gou_size = 20
    building_names_size = len(Provider.building_names)
    building_number_size = 900

    def __prepare_index(self, index: TransactionAddressIndex) -> Tuple[int]:
        return (
            index._format % self._format_size,
            index.chome % self.chome_size,
            index.ban % self.ban_size,
            index.gou % self.gou_size,
            index.building_name % self.building_names_size,
            index.building_number % self.building_number_size,
        )

    def __get_zip_code_file(self) -> PosixPath:
        _dir = self.random_element(list(zip_code_dir.iterdir()))
        _file = self.random_element(list((zip_code_dir / _dir).iterdir()))
        return zip_code_dir / _dir / _file

    def get_full_address(self, address_format: str, prefecture: str, citie: str, town: str,
                         chome: str, ban: str, gou: str, building_name: str, building_number: str):
        return address_format \
            .replace('{{prefecture}}', prefecture) \
            .replace('{{city}}', citie) \
            .replace('{{town}}', town) \
            .replace('{{chome}}', chome) \
            .replace('{{ban}}', ban) \
            .replace('{{gou}}', gou) \
            .replace('{{building_name}}', building_name) \
            .replace('{{building_number}}', building_number)

    def get_address(self):
        with open(self.__get_zip_code_file()) as f:
            data = json.load(f)
        return self.random_element(data)

    def get_address_format(self, index: TransactionAddressIndex):
        fo, _, _, _, _, _ = self.__prepare_index(index)
        return self.address_formats[fo]

    def indexed_chome(self, index: TransactionAddressIndex):
        _, ch, _, _, _, _ = self.__prepare_index(index)
        return '%d丁目' % ch

    def indexed_chome_kana(self, index: TransactionAddressIndex):
        _, ch, _, _, _, _ = self.__prepare_index(index)
        return '%dﾁｮｳﾒ' % ch

    def indexed_ban(self, index: TransactionAddressIndex):
        _, _, ba, _, _, _ = self.__prepare_index(index)
        return '%d番' % ba

    def indexed_ban_kana(self, index: TransactionAddressIndex):
        _, _, ba, _, _, _ = self.__prepare_index(index)
        return '%dﾊﾞﾝ' % ba

    def indexed_gou(self, index: TransactionAddressIndex):
        _, _, _, go, _, _ = self.__prepare_index(index)
        return '%d号' % go

    def indexed_gou_kana(self, index: TransactionAddressIndex):
        _, _, _, go, _, _ = self.__prepare_index(index)
        return '%dｺﾞｳ' % go

    def indexed_building_name(self, index: TransactionAddressIndex, town_name: str):
        fo, _, _, _, bn, _ = self.__prepare_index(index)
        if fo == 0:
            return ''
        return self.building_names[bn]

    def indexed_building_name_kana(self, index: TransactionAddressIndex, town_name_kana: str):
        fo, _, _, _, bn, _ = self.__prepare_index(index)
        if fo == 0:
            return ''
        return self.building_names_kana[bn]

    def indexed_building_number(self, index: TransactionAddressIndex):
        fo, _, _, _, _, bm = self.__prepare_index(index)
        if fo == 0:
            return ''
        return '{:03}'.format(bm)

    def __prepare_town_name(self, town_name: str):
        return town_name \
            .replace('町', '') \
            .replace('村', '')

    def __prepare_town_name(self, town_name: str):
        return town_name \
            .replace('ﾁｮｳ', '') \
            .replace('ﾑﾗ', '')
