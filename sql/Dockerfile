FROM mysql
LABEL maintainer="ben@benpiper.com"
LABEL Description="SQL server for the multi-tier web app."

ENV MYSQL_ROOT_PASSWORD="Password1"

COPY create_db_table.sql /tmp/create_db_table.sql

# Install Apache and Python and create directory structures
RUN /bin/bash -c "/usr/bin/mysqld_safe --skip-grant-tables &" && \
sleep 5 && \
mysql -u root -e "CREATE DATABASE appdemo" && \
mysql -u root -p Password1 appdemo < /tmp/create_db_table.sql
