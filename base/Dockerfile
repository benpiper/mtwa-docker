FROM alpine
LABEL maintainer="ben@benpiper.com"
LABEL Description="Base image for the multi-tier web app. This is used to build the web and application tier images."

ENV APPSERVER=appserver.company.com \
    DBSERVER=dbserver.company.com

# Install Apache and Python and create directory structures
RUN apk add --update apache2 py-pip openrc\
 && pip install pymysql \
 && mkdir /etc/mtwa \
 && mkdir /var/www/localhost/htdocs/appdemo

# Copy config files
COPY mtwa.conf /etc/mtwa/
COPY html/* /var/www/localhost/htdocs/appdemo/
COPY scripts/* /var/www/localhost/htdocs/appdemo/
COPY entrypoint.sh /sbin/entrypoint.sh
RUN chmod 755 /sbin/entrypoint.sh

# Copy configuration files when using this as a base for the web and app tier images
ONBUILD COPY 000-default.conf /etc/apache2/sites-enabled/
ONBUILD COPY ports.conf /etc/apache2/
ONBUILD RUN chmod o+x /var/www/localhost/htdocs/appdemo/*