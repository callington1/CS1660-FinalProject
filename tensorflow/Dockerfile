FROM tensorflow/tensorflow
WORKDIR /tensorflow
ADD . /tensorflow
RUN apt-get update
RUN apt-get install -y xterm
CMD python listener.py