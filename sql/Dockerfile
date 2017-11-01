FROM mysql
LABEL maintainer="ben@benpiper.com"
LABEL Description="SQL server for the multi-tier web app."

ENV MYSQL_ROOT_PASSWORD="Password1"

COPY create_db_table.sql /tmp/create_db_table.sql

RUN /usr/local/bin/docker-entrypoint.sh && \
 mysql -u root -pPassword1 appdemo < /tmp/create_db_table.sql
