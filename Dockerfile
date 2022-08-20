FROM python:3.9


WORKDIR /usr/app

COPY . .

RUN apt-get update && apt-get -y install cron
COPY crontab /etc/cron.d/crontab
RUN chmod 0644 /etc/cron.d/crontab
RUN /usr/bin/crontab /etc/cron.d/crontab

RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
RUN pip install -e .
RUN pip install uwsgi gevent

CMD uwsgi --ini uwsgi.ini