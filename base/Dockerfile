FROM debian
LABEL maintainer="ben@benpiper.com"
LABEL Description="Base image for the multi-tier web app. This is used to build the web and application tier images."

# Install Apache and Python and create directory structures
RUN apt-get update \
 && apt-get install apache2 python-pip -y \
 && apt-get clean \
 && pip install pymysql \
 && a2dismod mpm_event \
 && a2enmod mpm_prefork cgi \
 && service apache2 restart \
 && mkdir /etc/mtwa \
 && mkdir /var/www/html/appdemo

# Copy config files
COPY mtwa.conf /etc/mtwa/
COPY html/* /var/www/html/appdemo/
COPY scripts/* /var/www/html/appdemo/

# Copy configuration files when using this as a base for the web and app tier images
ONBUILD COPY 000-default.conf /etc/apache2/sites-enabled/
ONBUILD COPY ports.conf /etc/apache2/