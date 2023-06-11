FROM ubuntu:latest

RUN apt-get update -y
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN pip3 install --upgrade pip

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 3001

RUN groupadd -r mumble && useradd -r -g mumble mumble
RUN chsh -s /usr/sbin/nologin root
RUN su - mumble

CMD python3 main.py