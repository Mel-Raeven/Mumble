FROM ubuntu:latest

RUN apt-get update -y
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN pip3 install --upgrade pip

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 3001

CMD python3 main.py