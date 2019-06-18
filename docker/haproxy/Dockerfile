FROM haproxy:1.7
# Create a system group and user to be used by HAProxy.
RUN groupadd haproxy && useradd -g haproxy haproxy
RUN mkdir -p /run/haproxy/
RUN mkdir -p /var/lib/haproxy/
RUN mkdir -p /dev/log/ 
COPY haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg
