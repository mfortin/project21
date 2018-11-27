FROM node:10.13.0-alpine

COPY rtc /rtc
WORKDIR /rtc
RUN npm install --production

CMD ["node","server.js"]

