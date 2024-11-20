FROM python:3.10

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONPATH /x   

COPY requirements.txt /app/requirements.txt

# RUN apt-get update && \
#     apt-get --yes install gcc python3-dev libpq-dev && \
#     apt-get autoclean && apt-get autoremove && \
#     apt-get clean

RUN pip install -r requirements.txt

COPY . /app