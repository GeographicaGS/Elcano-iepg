#FROM node:0.10.41

#COPY . /app

#WORKDIR /app/src

#ENV NODE_PATH /usr/local/lib/node_modules
#RUN npm install -g jake jshint uglify-js uglifycss pg less@1.6.0

#CMD [ "jake" ]

# Docker Hub: https://hub.docker.com/_/node/
FROM node:5.10.1-onbuild

COPY src /usr/src/app
COPY cdn /usr/src/cdn

RUN npm install -g nodemon jake

#CMD [ "jake" ]