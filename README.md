# flask-faker
フェイクデータを返すAPI  
データを作成する要素は実際のデータをもとにしていますが、生成されたデータは架空のものとなっています。  

## Endpoints
### Person
ランダムに生成された人の名前を取得する

#### HTTP Request
- `GET http://localhost/person`
- `GET http://localhost/person/<sex>`

#### URL Parameters
|Parameter|Description|
|:-:|:-:|
|sex|Personオブジェクトの性別を指定する(only `female` or `male`)|

#### Query Parameters
|Parameter|Type|Default|Description|
|:-:|:-:|:-:|:-:|
|seed|int|None|ランダムのseed値を固定する|
|count|int|None|生成する数を指定する|

#### Response
```
{
  "name": "山岸 太一",
  "kana_name": "ヤマギシ タイチ",
  "romanized_name": "Yamagishi Taichi",
  "last_name": "山岸",
  "last_kana_name": "ヤマギシ",
  "last_romanized_name": "Yamagishi",
  "first_name": "太一",
  "first_kana_name": "タイチ",
  "first_romanized_name": "Taichi",
  "sex": "male"
}
```

### Address
ランダムに生成された住所データを取得する

#### HTTP Request
- `GET http://localhost/address`

#### Query Parameters
|Parameter|Type|Default|Description|
|:-:|:-:|:-:|:-:|
|seed|int|None|ランダムのseed値を固定する|
|count|int|None|生成する数を指定する|

#### Response
```
{
  "address": "奈良県台東区卯の里18丁目23番14号 ハイツ卯の里608",
  "address_kana": "ナラケンタイトウクウノサト18チョウメ23バン14ゴウ ハイツウノサト608",
  "prefecture": "奈良県",
  "prefecture_kana": "ナラケン",
  "city": "台東区",
  "city_kana": "タイトウク",
  "town": "卯の里",
  "town_kana": "ウノサト",
  "chome": "18丁目",
  "chome_kana": "18チョウメ",
  "ban": "23番",
  "ban_kana": "23バン",
  "gou": "14号",
  "gou_kana": "14ゴウ",
  "building_name": "ハイツ卯の里",
  "building_name_kana": "ハイツウノサト",
  "building_number": "608",
  "zipcode": "366-9558"
}
```