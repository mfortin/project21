FROM node:10.13.0-alpine

COPY rtc /rtc
COPY entrypoint.sh /opt/entrypoint.sh
RUN chmod 0755 /opt/entrypoint.sh
WORKDIR /rtc
RUN npm install --production
EXPOSE 9001

ENTRYPOINT ["/opt/entrypoint.sh"]
