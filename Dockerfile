FROM python:3.7

RUN mkdir -p /deploy/app

COPY requirements.txt /deploy/
RUN python3 -m ensurepip \
  && pip install --upgrade pip \
  && pip install -r /deploy/requirements.txt

WORKDIR /deploy

COPY . /deploy

ARG SERVE_PORT
ARG ENVIRONMENT

ENV SERVE_PORT $SERVE_PORT
ENV ENVIRONMENT $ENVIRONMENT

CMD gunicorn --config gunicorn.cfg -b 0.0.0.0:$SERVE_PORT 'app:create_app()'
