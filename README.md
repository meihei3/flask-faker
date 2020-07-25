# flask-faker

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