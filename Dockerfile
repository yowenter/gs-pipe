FROM daocloud.io/python:3.6-alpine


RUN apk add --update supervisor python-dev build-base redis libffi-dev openssl-dev gcc \
    linux-headers musl-dev


COPY ./requirements.txt /usr/src/
RUN pip install -r /usr/src/requirements.txt


COPY gs_pipe /usr/src/gs_pipe
COPY redis.conf /etc/redis.conf


COPY supervisord.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/supervisord.sh

EXPOSE 5000

CMD ["sh", "/usr/local/bin/supervisord.sh"]