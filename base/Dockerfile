FROM debian:stable-slim
LABEL maintainer="ben@benpiper.com"
LABEL Description="Base image for the multi-tier web app. This is used to build the web and application tier images."

ENV APPSERVER="http://myAppTierLoadBalancer.us-east-1.elb.amazonaws.com:8080" \
    DBSERVER="172.31.101.99"
#    SETCOOKIE=yes

# Install Apache and Python and create directory structures
RUN apt-get update \
 && apt-get install apache2 python-pip -y \
 && apt-get clean \
 && pip install pymysql \
 && a2dismod mpm_event \
 && a2enmod mpm_prefork cgi \
 && a2enmod ssl \
 && service apache2 restart \
 && mkdir /etc/mtwa \
 && mkdir /var/www/html/appdemo

# Copy config files
COPY mtwa.conf /etc/mtwa/
COPY html/* /var/www/html/appdemo/
COPY scripts/* /var/www/html/appdemo/
COPY entrypoint.sh /sbin/entrypoint.sh
RUN chmod 755 /sbin/entrypoint.sh \
 && mkdir /etc/apache2/ssl
COPY apache.* /etc/apache2/ssl/


# Copy configuration files when using this as a base for the web and app tier images
ONBUILD COPY 000-default.conf /etc/apache2/sites-enabled/
ONBUILD COPY ports.conf /etc/apache2/
ONBUILD RUN chmod o+x /var/www/html/appdemo/*
