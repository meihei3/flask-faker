from faker.providers.person.ja_JP import Provider
from fakerProviders.utils import TransactionNameIndex
from typing import Tuple


"""
person.ja_JP.Providerの強化版
indexアクセス出来るようにしている
"""


class PersonProvider(Provider):
    # link: http://dic.nicovideo.jp/a/日本人の名前一覧
    # link: http://www.meijiyasuda.co.jp/enjoy/ranking/
    first_names_female = (
        '明美', 'あすか', '香織', '加奈', 'くみ子', 'さゆり', '知実', '千代',
        '直子', '七夏', '花子', '春香', '真綾', '舞', '美加子', '幹',
        '桃子', '結衣', '裕美子', '陽子', '里佳',
    )

    # link: http://dic.nicovideo.jp/a/日本人の名前一覧
    # link: http://www.meijiyasuda.co.jp/enjoy/ranking/
    first_names_male = (
        '晃', '篤司', '治', '和也', '京助', '健一', '修平', '翔太',
        '淳', '聡太郎', '太一', '太郎', '拓真', '翼', '智也', '直樹',
        '直人', '英樹', '浩', '学', '充', '稔', '裕樹', '裕太',
        '康弘', '陽一', '洋介', '亮介', '涼平', '零',
    )

    # link: https://dic.nicovideo.jp/a/日本の苗字(名字)の一覧
    last_names = (
        '青田', '青山', '石田', '井高', '伊藤', '井上', '宇野', '江古田',
        '大垣', '加藤', '加納', '喜嶋', '木村', '桐山', '工藤', '小泉',
        '小林', '近藤', '斉藤', '坂本', '佐々木', '佐藤', '笹田', '鈴木',
        '杉山', '高橋', '田中', '田辺', '津田', '中島', '中村', '渚',
        '中津川', '西之園', '野村', '原田', '浜田', '廣川', '藤本', '松本',
        '三宅', '宮沢', '村山', '山岸', '山口', '山田', '山本', '吉田',
        '吉本', '若松', '渡辺',
    )

    first_kana_names_female = (
        'アケミ', 'アスカ', 'カオリ', 'カナ',
        'クミコ', 'サユリ', 'サトミ', 'チヨ',
        'ナオコ', 'ナナミ', 'ハナコ', 'ハルカ',
        'マアヤ', 'マイ', 'ミカコ', 'ミキ',
        'モモコ', 'ユイ', 'ユミコ', 'ヨウコ',
        'リカ',
    )

    first_kana_names_male = (
        'アキラ', 'アツシ', 'オサム', 'カズヤ',
        'キョウスケ', 'ケンイチ', 'シュウヘイ', 'ショウタ',
        'ジュン', 'ソウタロウ', 'タイチ', 'タロウ',
        'タクマ', 'ツバサ', 'トモヤ', 'ナオキ',
        'ナオト', 'ヒデキ', 'ヒロシ', 'マナブ',
        'ミツル', 'ミノル', 'ユウキ', 'ユウタ',
        'ヤスヒロ', 'ヨウイチ', 'ヨウスケ', 'リョウスケ',
        'リョウヘイ', 'レイ',
    )

    last_kana_names = (
        'アオタ', 'アオヤマ', 'イシダ', 'イダカ',
        'イトウ', 'イノウエ', 'ウノ', 'エコダ',
        'オオガキ', 'カトウ', 'カノウ', 'キジマ',
        'キムラ', 'キリヤマ', 'クドウ', 'コイズミ',
        'コバヤシ', 'コンドウ', 'サイトウ', 'サカモト',
        'ササキ', 'サトウ', 'ササダ', 'スズキ',
        'スギヤマ', 'タカハシ', 'タナカ', 'タナベ',
        'ツダ', 'ナカジマ', 'ナカムラ', 'ナギサ',
        'ナカツガワ', 'ニシノソノ', 'ノムラ', 'ハラダ',
        'ハマダ', 'ヒロカワ', 'フジモト', 'マツモト',
        'ミヤケ', 'ミヤザワ', 'ムラヤマ', 'ヤマギシ',
        'ヤマグチ', 'ヤマダ', 'ヤマモト', 'ヨシダ',
        'ヨシモト', 'ワカマツ', 'ワタナベ',
    )

    first_romanized_names_female = (
        'Akemi', 'Asuka', 'Kaori', 'Kana',
        'Kumiko', 'Sayuri', 'Satomi', 'Chiyo',
        'Naoko', 'Nanami', 'Hanako', 'Haruka',
        'Maaya', 'Mai', 'Mikako', 'Miki',
        'Momoko', 'Yui', 'Yumiko', 'Yoko',
        'Rika',
    )

    first_romanized_names_male = (
        'Akira', 'Atsushi', 'Osamu', 'Kazuya',
        'Kyosuke', 'Kenichi', 'Shohei', 'Shota',
        'Jun', 'Sotaro', 'Taichi', 'Taro',
        'Takuma', 'Tsubasa', 'Tomoya', 'Naoki',
        'Naoto', 'Hideki', 'Hiroshi', 'Manabu',
        'Mituru', 'Minoru', 'Yuki', 'Yuta',
        'Yasuhiro', 'Yoichi', 'Yosuke', 'Ryosuke',
        'Ryohei', 'Rei',
    )

    last_romanized_names = (
        'Aota', 'Aoyama', 'Ishida', 'Idaka',
        'Ito', 'Inoue', 'Uno', 'Ekoda',
        'Ogaki', 'Kato', 'Kano', 'Kijima',
        'Kimura', 'Kiriyama', 'Kudo', 'Koizumi',
        'Kobayashi', 'Kondo', 'Saito', 'Sakamoto',
        'Sasaki', 'Sato', 'Sasada', 'Suzuki',
        'Sugiyama', 'Takahashi', 'Tanaka', 'Tanabe',
        'Tsuda', 'Nakajima', 'Nakamura', 'Nagisa',
        'Nakatsugawa', 'Nishinosono', 'Nomura', 'Harada',
        'Hamada', 'Hirokawa', 'Fujimoto', 'Matsumoto',
        'Miyake', 'Miyagawa', 'Murayama', 'Yamagishi',
        'Yamaguchi', 'Yamada', 'Yamamoto', 'Yoshida',
        'Yoshimoto', 'Wakamatsu', 'Watanabe',
    )

    first_names = first_names_female + first_names_male
    first_kana_names = first_kana_names_female + first_kana_names_male
    first_romanized_names = first_romanized_names_female + first_romanized_names_male
    first_names_female_size = len(first_names_female)
    first_names_male_size = len(first_names_male)
    first_names_size = first_names_female_size + first_names_male_size
    last_names_size = len(last_names)

    def __prepare_index(self, index: TransactionNameIndex) -> Tuple[int, int]:
        return index.first % self.first_names_size, index.last % self.last_names_size

    def __prepare_index_female(self, index: TransactionNameIndex) -> Tuple[int, int]:
        return index.first % self.first_names_female_size, index.last % self.last_names_size

    def __prepare_index_male(self, index: TransactionNameIndex) -> Tuple[int, int]:
        return index.first % self.first_names_male_size, index.last % self.last_names_size

    def indexed_name(self, index: TransactionNameIndex) -> str:
        fi, li = self.__prepare_index(index)
        return "%s %s" % (
            self.last_names[li], self.first_names[fi]
        )

    def indexed_name_female(self, index: TransactionNameIndex) -> str:
        fi, li = self.__prepare_index_female(index)
        return "%s %s" % (
            self.last_names[li], self.first_names_female[fi]
        )

    def indexed_name_male(self, index: TransactionNameIndex) -> str:
        fi, li = self.__prepare_index_male(index)
        return "%s %s" % (
            self.last_names[li], self.first_names_male[fi]
        )

    def indexed_kana_name(self, index: TransactionNameIndex) -> str:
        fi, li = self.__prepare_index(index)
        return "%s %s" % (
            self.last_kana_names[li], self.first_kana_names[fi]
        )

    def indexed_kana_name_female(self, index: TransactionNameIndex) -> str:
        fi, li = self.__prepare_index_female(index)
        return "%s %s" % (
            self.last_kana_names[li], self.first_kana_names_female[fi]
        )

    def indexed_kana_name_male(self, index: TransactionNameIndex) -> str:
        fi, li = self.__prepare_index_male(index)
        return "%s %s" % (
            self.last_kana_names[li], self.first_kana_names_male[fi]
        )

    def indexed_romanized_name(self, index: TransactionNameIndex) -> str:
        fi, li = self.__prepare_index(index)
        return "%s %s" % (
            self.last_romanized_names[li], self.first_romanized_names[fi]
        )

    def indexed_romanized_name_female(self, index: TransactionNameIndex) -> str:
        fi, li = self.__prepare_index_female(index)
        return "%s %s" % (
            self.last_romanized_names[li], self.first_romanized_names_female[fi]
        )

    def indexed_romanized_name_male(self, index: TransactionNameIndex) -> str:
        fi, li = self.__prepare_index_male(index)
        return "%s %s" % (
            self.last_romanized_names[li], self.first_romanized_names_male[fi]
        )

    def indexed_first_name(self, index: TransactionNameIndex) -> str:
        fi, _ = self.__prepare_index(index)
        return self.first_names[fi]

    def indexed_first_name_female(self, index: TransactionNameIndex) -> str:
        fi, _ = self.__prepare_index_female(index)
        return self.first_names_female[fi]

    def indexed_first_name_male(self, index: TransactionNameIndex) -> str:
        fi, _ = self.__prepare_index_male(index)
        return self.first_names_male[fi]

    def indexed_first_kana_name(self, index: TransactionNameIndex) -> str:
        fi, _ = self.__prepare_index(index)
        return self.first_kana_names[fi]

    def indexed_first_kana_name_female(self, index: TransactionNameIndex) -> str:
        fi, _ = self.__prepare_index_female(index)
        return self.first_kana_names_female[fi]

    def indexed_first_kana_name_male(self, index: TransactionNameIndex) -> str:
        fi, _ = self.__prepare_index_male(index)
        return self.first_kana_names_male[fi]

    def indexed_first_romanized_name(self, index: TransactionNameIndex) -> str:
        fi, _ = self.__prepare_index(index)
        return self.first_romanized_names[fi]

    def indexed_first_romanized_name_female(self, index: TransactionNameIndex) -> str:
        fi, _ = self.__prepare_index_female(index)
        return self.first_romanized_names_female[fi]

    def indexed_first_romanized_name_male(self, index: TransactionNameIndex) -> str:
        fi, _ = self.__prepare_index_male(index)
        return self.first_romanized_names_male[fi]

    def indexed_last_name(self, index: TransactionNameIndex) -> str:
        _, li = self.__prepare_index(index)
        return self.last_names[li]

    def indexed_last_kana_name(self, index: TransactionNameIndex) -> str:
        _, li = self.__prepare_index(index)
        return self.last_kana_names[li]

    def indexed_last_romanized_name(self, index: TransactionNameIndex) -> str:
        _, li = self.__prepare_index(index)
        return self.last_romanized_names[li]

    def indexed_sex(self, index: TransactionNameIndex) -> str:
        fi, _ = self.__prepare_index(index)
        return 'female' if fi < self.first_names_female_size else 'male'
