FROM python:3.6

RUN apt-get update \
    && apt-get install -y mecab \
    mecab-ipadic \
    libmecab-dev \
    mecab-ipadic-utf8 \
    swig

ADD requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

RUN cp /etc/mecabrc /usr/local/etc/

WORKDIR /app
CMD ["python", "index.py"]
