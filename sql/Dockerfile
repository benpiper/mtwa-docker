FROM mysql

LABEL maintainer="ben@benpiper.com"
LABEL Description="SQL database"

ENV MYSQL_RANDOM_ROOT_PASSWORD=yes

COPY *.sql /docker-entrypoint-initdb.d/
