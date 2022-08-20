FROM python:3.9

COPY . .

WORKDIR /app

RUN apt-get update && apt-get -y install cron vim
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
RUN pip install -e .
RUN pip install uwsgi gevent

CMD uwsgi --ini uwsgi.ini