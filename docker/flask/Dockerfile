FROM python:3.6

RUN apt-get update \
    && apt-get install -y mecab \
    mecab-ipadic \
    libmecab-dev \
    mecab-ipadic-utf8 \
    swig

RUN pip install mecab-python3 flask faker
