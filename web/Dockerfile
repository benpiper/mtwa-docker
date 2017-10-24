FROM benpiper/mtwa:base
LABEL maintainer="ben@benpiper.com"
LABEL Description="Web tier image for the multi-tier web app."

RUN service apache2 restart

EXPOSE 80/tcp
# Start apache server
CMD /usr/sbin/apache2ctl -D FOREGROUND
