FROM python:3.9

WORKDIR /usr/app

COPY . .

RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
RUN pip install -e .
RUN pip install uwsgi gevent

CMD uwsgi --ini uwsgi.ini --enable-threads