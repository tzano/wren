# FROM rasa/rasa_nlu:latest-full
FROM python:3.6.5

# update and install packages
RUN apt-get update && apt-get install -y git && \
    apt-get install -y build-essential && apt-get install -y default-jre

# RUN pip install pip --upgrade
RUN apt-get install -y --no-install-recommends build-essential gcc libffi-dev

# working directory
RUN mkdir /app
WORKDIR /app

# install requirements
COPY requirements.txt ./
RUN pip install -r requirements.txt --upgrade

# get spacy data
#RUN python -m spacy link en_core_web_md en
#RUN python -m spacy download en

# Port
EXPOSE 5000

# run Rasa server
# CMD ["python", "-m", "rasa_nlu.server", "-c", "config/nlu_config.json", "--path", "/app/"]
