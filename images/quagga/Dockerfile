FROM quay.io/footloose/ubuntu18.04

RUN apt-get update
RUN apt-get install -y quagga

RUN touch /etc/quagga/zebra.conf
RUN touch /etc/quagga/ripd.conf
RUN touch /etc/quagga/vtysh.conf
RUN touch /etc/quagga/start.sh
RUN chmod +x /etc/quagga/start.sh


RUN sudo chown quagga:quagga /etc/quagga/zebra.conf && sudo chmod 640 /etc/quagga/zebra.conf
RUN sudo chown quagga:quagga /etc/quagga/ripd.conf && sudo chmod 640 /etc/quagga/ripd.conf
RUN sudo chown quagga:quaggavty /etc/quagga/vtysh.conf && sudo chmod 660 /etc/quagga/vtysh.conf

RUN	mkdir /var/log/quagga && \
	chown -R quagga:quagga /var/log/quagga && \
	mkdir /var/log/zebra && \
	touch /var/log/zebra/zebra.log && \
	touch /var/log/zebra/ripd.log && \
	chown -R quagga:quagga /var/log/zebra

RUN echo "net.ipv4.conf.all.forwarding=1" | sudo tee -a /etc/sysctl.conf
RUN echo "net.ipv4.conf.default.forwarding=1" | sudo tee -a /etc/sysctl.conf
RUN sed 's/#net.ipv6.conf.all.forwarding=1/net.ipv6.conf.all.forwarding=1/g' /etc/sysctl.conf | sudo tee /etc/sysctl.conf
RUN echo "net.ipv6.conf.default.forwarding=1" | sudo tee -a /etc/sysctl.conf
RUN sudo sysctl -p

RUN echo "net.ipv4.conf.all.mc_forwarding=1" | sudo tee -a /etc/sysctl.conf
RUN echo "net.ipv4.conf.default.mc_forwarding=1" | sudo tee -a /etc/sysctl.conf
RUN sudo sysctl -p
