FROM python:3.4.3

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y supervisor

RUN rm -rf /etc/supervisor/* && \
    ln -s /code/deployment/supervisord.conf /etc/supervisord.conf && \
    mkdir -p /var/log/supervisord && \
    mkdir /code

WORKDIR /code

ADD requirements.txt /code/

RUN pip install -r requirements.txt

RUN groupadd -r user -g 1000
RUN useradd -u 1000 -r -g user -d /code -s /bin/bash -c "Docker Image User" user
RUN chown -R user:user /code

COPY . /code/
