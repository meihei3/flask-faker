from faker.providers.address.ja_JP import Provider
from fakerProviders.utils import TransactionAddressIndex
from typing import Tuple

class AddressProvider(Provider):
    prefectures_kana = (
        'ホッカイドウ', 'アオモリケン', 'イワテケン', 'ミヤギケン', 'アキタケン', 'ヤマガタケン',
        'フクシマケン', 'イバラキケン', 'トチギケン', 'グンマケン', 'サイタマケン', 'チバケン',
        'トウキョウト', 'カナガワケン', 'ニイガタケン', 'トヤマケン', 'イシカワケン', 'フクイケン',
        'ヤマナシケン', 'ナガノケン', 'ギフケン', 'シズオカケン', 'アイチケン', 'ミエケン',
        'シガケン', 'キョウトフ', 'オオサカフ', 'ヒョウゴケン', 'ナラケン', 'ワカヤマケン',
        'トットリケン', 'シマネケン', 'オカヤマケン', 'ヒロシマケン', 'ヤマグチケン', 'トクシマケン',
        'カガワケン', 'エヒメケン', 'コウチケン', 'フクオカケン', 'サガケン', 'ナガサキケン',
        'クマモトケン', 'オオイタケン', 'ミヤザキケン', 'カゴシマケン', 'オキナワケン',
    )

    cities_kana = (
        'ヤチヨシ', 'アビコシ', 'カモガワシ', 'カマガヤシ',
        'キミツシ', 'フッツシ', 'ウラヤスシ', 'ヨツカイドウシ',
        'ソデガウラシ', 'ヤチマタシ', 'インザイシ', 'シロイシ',
        'トミサトシ', 'ミナミボウソウシ', 'ソウサシ', 'カトリシ',
        'サンムシ', 'イスミシ', 'オオアミシラサトシ', 'インバグンシスイマチ',
        'インバグンインバムラ', 'インバグンモトノムラ', 'インバグンサカエマチ', 'カンドリグンカンザキチョウ',
        'カンドリグンタコマチ', 'カンドリグントウノショウマチ', 'サンブグンクジュウクリマチ', 'サンブグンシバヤママチ',
        'サンブグンヨコシバヒカリマチ', 'チョウセイグンイチノミヤチョウ', 'チョウセイグンムツザワマチ', 'チョウセイグンチョウセイムラ',
        'チョウセイグンシラコチョウ', 'チョウセイグンナガエチョウ', 'チョウセイグンチョウナンマチ', 'イスミグンオオタキマチ',
        'イスミグンオンジュクマチ', 'アワグンキョナンマチ', 'チヨダク', 'チュウオウク',
        'ミナトク', 'シンジュクク', 'ブンキョウク', 'タイトウク',
        'スミダク', 'カンドンク', 'シナガワク', 'メグロク',
        'オオタク', 'セタガヤク', 'シブヤク', 'ナカノク',
        'スギナミク', 'トシマク', 'キタク', 'アラカワク',
        'イタバシク', 'ネリマク', 'アダチク', 'カツシカク',
        'エドガワク', 'ハチオウジシ', 'タチカワシ', 'ムサシノシ',
        'ミタカシ', 'オウメシ', 'フチュウシ', 'アキシマシ',
        'チョウフシ', 'マチダシ', 'コガネイシ', 'コダイラシ',
        'ヒノシ', 'ヒガシムラヤマシ', 'コクブンジシ', 'クニタチシ',
        'フッサシ', 'コマエシ', 'ヒガシヤマトシ', 'キヨセシ',
        'ヒガシクルメシ', 'ムサシムラヤマシ', 'タマシ', 'イナギシ',
        'ハムラシ', 'アキルノシ', 'ニシトウキョウシ', 'ニシタマグンミズホチョウ',
        'ニシタマグンヒノデチョウ', 'ニシタマグンヒノハラムラ', 'ニシタマグンオクタママチ', 'オオシママチ',
        'トシマムラ', 'ニイジマムラ', 'コウヅシマムラ', 'ミヤケジマミヤケムラ',
        'ミクラジマムラ', 'ハチジョウジマハチジョウマチ', 'アオガシマムラ', 'オガサワラムラ',
        'ヨコハマシツルミク', 'ヨコハマシカナガワク', 'ヨコハマシニシク', 'ヨコハマシナカク',
        'ヨコハマシミナミク', 'ヨコハマシホドガヤク', 'ヨコハマシイソゴク', 'ヨコハマシカナザワク',
        'ヨコハマシコウホクク', 'ヨコハマシトツカク', 'ヨコハマシコウナンク', 'ヨコハマシアサヒク',
        'ヨコハマシミドリク', 'ヨコハマシセヤク', 'ヨコハマシサカエク', 'ヨコハマシイズミク',
        'ヨコハマシアオバク', 'ヨコハマシツヅキク', 'カワサキシカワサキク', 'カワサキシサイワイク',
        'カワサキシナカハラク', 'カワサキシタカツク', 'カワサキシタマク', 'カワサキシミヤマエク'
    )

    towns_kana = (
        'タンゼ', 'チュウグウシ', 'チョオカ', 'トウワチョウ', 'トコロノ', 'ツチザワ',
        'トッコザワ', 'トドロキ', 'ドロブ', 'ナカオコロガワ', 'ナガハタ', 'ナカハツイシマチ',
        'ナカミヨリ', 'ニシオコロガワ', 'ニシカワ', 'ニッコウ', 'ヒガシミシマ', 'ヒガシヤマトマチ',
        'ガマヌマ', 'フタツムロ', 'ホウキョウ', 'ホソダケ', 'マエヤロク', 'マエヤロクミナミチョウ',
        'マツウラチョウ', 'ミナミアカダ', 'ミナミゴウヤ', 'ミハラチョウ', 'ムクリヤ', 'アツシ',
        'モムラ', 'ヤツボ', 'ヤマナカシンデン', 'ユセイ', 'ユグウ', 'ユタカマチ',
        'ユモトシオバラ', 'ヨコバヤシ', 'ヨンクチョウ', 'ワタナベ', 'ウジイエ', 'ウジイエシンデン',
        'ウノサト', 'オイレ', 'オオナカ', 'オシアゲ', 'カキノキザワ', 'カキノキザワシンデン',
        'カジガサワ', 'カミコウヤ', 'カミヨシバ', 'コダチ', 'ゴンゲンドウ', 'サッテ',
        'シモウワダ', 'シモヨシバ', 'シンメイウチ', 'ソトゴウマ', 'チヅカ', 'テンジンジマ',
        'トシマ', 'ナカカワサキ', 'チョウマ', 'ニシセキヤド', 'ハナジマ', 'ヒラスカ',
        'ホソノ', 'マツイシ', 'オオタガヤ', 'カミヒロヤ', 'ゴミガヤ', 'スネオリ',
        'スネオリチョウ', 'ツルガオカ', 'ハネオリチョウ', 'フジカネ', 'クダンミナミ', 'コウキョガイエン',
        'コウジマチ', 'サルガクチョウ', 'ソトカンダ', 'ニシカンダ', 'ハヤブサチョウ', 'ヒガシカミダ',
        'ヒトツバシ', 'ヒビヤコウエン', 'ヒラカワチョウ', 'マルノウチ', 'マルノウチジェーアールタワー', 'ヨンバンチョウ',
        'ロクバンチョウ', 'アカシマチ', 'カチドキ', 'キョウバシ', 'ツキシマ', 'キタアオヤマ',
        'コウナン', 'シバウラ', 'シバコウエン', 'シバダイモン', 'ハッキン', 'シロカネダイ',
        'ダイバ', 'タカナワ', 'トラノモン', 'トラノモントラノモンヒルズモリタワー', 'ダイキョウチョウ', 'タカダノババ',
        'タンスマチ', 'ツクドチョウ', 'ツクドハチマンチョウ', 'トツカチョウ', 'トミヒサチョウ', 'トヤマ',
        'アキハバラ', 'アサクサ', 'アサクサバシ', 'イケノハタ', 'イマド', 'イリヤ',
        'ウエノコウエン', 'ウエノサクラギ', 'カミナリモン', 'キタウエノ', 'クラマエ', 'チヅカ',
        'タイトウ', 'トリコシ', 'ニシアサクサ', 'ニホンヅツミ', 'ハシバ', 'ハナカワド',
        'ヒガシアサクサ', 'ヒガシウエノ', 'マツガヤ', 'ミスジ', 'ミノワ', 'モトアサクサ',
        'リュウセン', 'アズマバシ'
    )

    number_kana = (
        'ゼロ', 'イチ', '二', 'サン', 'ヨン', 'ゴ', 'ロク', 'ナナ', 'ハチ', 'キュウ', 'ジュウ'
    )

    _format_size = 3
    prefectures_size = len(Provider.prefectures)
    cities_size = len(Provider.cities)
    towns_size = len(Provider.towns)
    chome_size = 42
    ban_size = 27
    gou_size = 20
    building_names_size = len(Provider.building_names)
    building_number_size = 900

    def __prepare_index(self, index: TransactionAddressIndex) -> Tuple[int]:
        return (
            index._format % self._format_size,
            index.prefecture % self.prefectures_size,
            index.city % self.cities_size,
            index.town % self.towns_size,
            index.chome % self.chome_size,
            index.ban % self.ban_size,
            index.gou % self.gou_size,
            index.building_name % self.building_names_size,
            index.building_number % self.building_number_size,
        )

    def indexed_address(self, index: TransactionAddressIndex):
        fo, pr, ci, tw, ch, ba, go, bn, bm = self.__prepare_index(index)
        return self.address_formats[fo] \
            .replace('{{prefecture}}', self.prefectures[pr]) \
            .replace('{{city}}', self.cities[ci]) \
            .replace('{{town}}', self.towns[tw]) \
            .replace('{{chome}}', '%d丁目' % ch) \
            .replace('{{ban}}', '%d番' % ba) \
            .replace('{{gou}}', '%d号' % go) \
            .replace('{{building_name}}', self.building_names[bn]) \
            .replace('{{building_number}}', '{:03}'.format(bm))

    def indexed_address_kana(self, index: TransactionAddressIndex):
        fo, pr, ci, tw, ch, ba, go, bn, bm = self.__prepare_index(index)
        return self.address_formats[fo] \
            .replace('{{prefecture}}', self.prefectures_kana[pr]) \
            .replace('{{city}}', self.cities_kana[ci]) \
            .replace('{{town}}', self.towns_kana[tw]) \
            .replace('{{chome}}', '%dチョウメ' % ch) \
            .replace('{{ban}}', '%dバン' % ba) \
            .replace('{{gou}}', '%dゴウ' % go) \
            .replace('{{building_name}}', self.building_names[bn]) \
            .replace('{{building_number}}', '{:03}'.format(bm))

    def indexed_prefecture(self, index: TransactionAddressIndex):
        _, i, _, _, _, _, _, _, _ = self.__prepare_index(index)
        return self.prefectures[i]

    def indexed_prefecture_kana(self, index: TransactionAddressIndex):
        _, i, _, _, _, _, _, _, _ = self.__prepare_index(index)
        return self.prefectures_kana[i]

    def indexed_city(self, index: TransactionAddressIndex):
        _, _, i, _, _, _, _, _, _ = self.__prepare_index(index)
        return self.cities[i]

    def indexed_city_kana(self, index: TransactionAddressIndex):
        _, _, i, _, _, _, _, _, _ = self.__prepare_index(index)
        return self.cities_kana[i]

    def indexed_town(self, index: TransactionAddressIndex):
        _, _, _, i, _, _, _, _, _ = self.__prepare_index(index)
        return self.towns[i]

    def indexed_town_kana(self, index: TransactionAddressIndex):
        _, _, _, i, _, _, _, _, _ = self.__prepare_index(index)
        return self.towns_kana[i]

    def indexed_chome(self, index: TransactionAddressIndex):
        _, _, _, _, ch, _, _, _, _ = self.__prepare_index(index)
        return '%d丁目' % ch

    def indexed_chome_kana(self, index: TransactionAddressIndex):
        _, _, _, _, ch, _, _, _, _ = self.__prepare_index(index)
        return '%dチョウメ' % ch

    def indexed_ban(self, index: TransactionAddressIndex):
        _, _, _, _, _, ba, _, _, _ = self.__prepare_index(index)
        return '%d番' % ba

    def indexed_ban_kana(self, index: TransactionAddressIndex):
        _, _, _, _, _, ba, _, _, _ = self.__prepare_index(index)
        return '%dバン' % ba

    def indexed_gou(self, index: TransactionAddressIndex):
        _, _, _, _, _, _, go, _, _ = self.__prepare_index(index)
        return '%d号' % go

    def indexed_gou_kana(self, index: TransactionAddressIndex):
        _, _, _, _, _, _, go, _, _ = self.__prepare_index(index)
        return '%dゴウ' % go

    def indexed_building_name(self, index: TransactionAddressIndex):
        fo, _, _, tw, _, _, _, bn, _ = self.__prepare_index(index)
        if fo == 1:
            return self.towns[tw] + self.building_names[bn]
        elif fo == 2:
            return self.building_names[bn] + self.towns[tw]
        return ''

    def indexed_building_name_kana(self, index: TransactionAddressIndex):
        fo, _, _, tw, _, _, _, bn, _ = self.__prepare_index(index)
        if fo == 1:
            return self.towns_kana[tw] + self.building_names[bn]
        elif fo == 2:
            return self.building_names[bn] + self.towns_kana[tw]
        return ''

    def indexed_building_number(self, index: TransactionAddressIndex):
        fo, _, _, _, _, _, _, _, bm = self.__prepare_index(index)
        if fo == 0:
            return ''
        return '{:03}'.format(bm)
