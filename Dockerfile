FROM python:3.8-alpine

COPY requirements.txt /
COPY main.py /
COPY .env /

RUN pip install -r requirements.txt

CMD [ "python", "-u", "./main.py" ]
