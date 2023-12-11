FROM python:3.10.13

WORKDIR /backend

ADD requirements.txt .
RUN pip install -r requirements.txt

RUN apt-get update && apt-get install
RUN apt-get install postgresql-client -y


COPY . .

COPY ./bin/start.sh /
RUN chmod +x /start.sh

EXPOSE 8000

ENTRYPOINT ["/start.sh"]