FROM node:0.10.41

RUN mkdir -p /app/src
WORKDIR /app/src

ENV NODE_PATH /usr/local/lib/node_modules
RUN npm install -g jake jshint uglify-js uglifycss pg less@1.6.0

CMD [ "jake" ]