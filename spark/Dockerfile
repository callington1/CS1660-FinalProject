FROM epahomov/docker-spark
WORKDIR /spark
ADD . /spark
RUN apt-get update
RUN apt-get install -y xterm
CMD python listener.py