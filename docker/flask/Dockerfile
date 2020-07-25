FROM python:3.7

ADD requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

WORKDIR /app
CMD ["python", "index.py"]
