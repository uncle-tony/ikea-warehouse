FROM ubuntu:latest
MAINTAINER g1zm0 german.retamosa@gmail.com
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
COPY ./src /app
COPY ./requirements.txt /app
WORKDIR /app
RUN pwd
RUN ls
RUN pip3 install -r requirements.txt --no-cache-dir
EXPOSE 9000
CMD ["flask","run","--port=9000"]
