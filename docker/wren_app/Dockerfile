FROM python:3.6.5

RUN apt-get update && apt-get install -y git && \
    apt-get install -y build-essential && apt-get install -y default-jre

RUN pip install --upgrade pip

RUN mkdir /usr/src/app


WORKDIR /usr/src/app


RUN ls

COPY requirements.txt ./

RUN pip install -r requirements.txt --upgrade

EXPOSE 5001
