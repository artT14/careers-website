# syntax=docker/dockerfile:1

FROM python:3.10

WORKDIR /python-docker

COPY . .

RUN pip install -r ./requirements.txt

RUN python ./scripts/createdb.py

EXPOSE 5000

CMD [ "python", "app.py"]