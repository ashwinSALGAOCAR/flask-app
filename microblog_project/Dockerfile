FROM python:3.6-alpine

RUN adduser -D user

WORKDIR /home/user

COPY flask_app-req.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn pymysql

COPY app app
COPY migrations migrations
COPY microblog.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP microblog.py

RUN chown -R user:user ./
USER user

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
