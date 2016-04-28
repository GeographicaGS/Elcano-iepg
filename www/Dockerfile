# Docker Hub: https://hub.docker.com/_/node/
FROM node:5.10.1

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY src /usr/src/app
COPY cdn /usr/src/cdn
RUN npm install && npm install -g nodemon jake

CMD [ "npm", "start" ]
