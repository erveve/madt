FROM quay.io/footloose/ubuntu18.04

RUN sudo apt update

RUN sudo apt-get install -y build-essential \
	       musl-dev \
	       # python3-dev \
	       python3 \
	       # linux-headers \
	       # zeromq-dev \
	       libzmq3-dev \
	       iproute2 \
	       python3-pip \
	       && \
    pip3 install requests pyzmq

ADD ./lib /etc/madt/madt_client

ENV PYTHONPATH=/etc/madt:$PYTHONPATH
