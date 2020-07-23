from flask import Flask
import MeCab

app = Flask(__name__)
mecab = MeCab.Tagger()


@app.route('/')
def hello():
    name = "こんにちは世界。"
    return mecab.parse(name)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
