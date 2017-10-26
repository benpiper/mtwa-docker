FROM benpiper/mtwa:testbase
LABEL maintainer="ben@benpiper.com"
LABEL Description="Web tier image for the multi-tier web app."

RUN rc-service apache2 restart

EXPOSE 80/tcp
# Start apache server
ENTRYPOINT ["/sbin/entrypoint.sh"]