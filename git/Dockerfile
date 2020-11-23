FROM ubuntu
WORKDIR /git
ADD . /git
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y git
RUN apt-get install -y xterm
CMD python3 listener.py