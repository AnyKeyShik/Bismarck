FROM python:3.8

COPY . /Bismarck
WORKDIR /Bismarck

RUN apt-get update; apt-get install --no-install-recommends -y gcc
RUN pip3 install -r requirements.txt

ENV BISMARCK_HOME /Bismarck
ENV BISMARCK_LOGLEVEL WARNING
RUN mkdir /Bismarck/logs

CMD python ./run.py --deploy
