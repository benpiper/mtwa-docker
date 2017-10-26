FROM benpiper/mtwa:testbase
LABEL maintainer="ben@benpiper.com"
LABEL Description="App tier image for the multi-tier web app."

RUN rc-service apache2 restart

EXPOSE 8080/tcp
# Start apache server
ENTRYPOINT ["/sbin/entrypoint.sh"]