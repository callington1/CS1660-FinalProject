FROM ubuntu
WORKDIR /spyder
ADD . /spyder
RUN apt-get update
RUN apt-get install -y xterm
RUN apt-get install -y python3
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get install -y spyder
CMD python3 listener.py