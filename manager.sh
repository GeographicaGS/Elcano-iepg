#!/bin/bash

function buildapps(){
  docker-compose -f docker-compose.$1.yml up -d pgsql
  sleep 1
  docker run --rm -it --link elcanoiepg_pgsql_1:${POSTGRES_HOST} -v $(pwd)/www:/app -e "POSTGRES_HOST=${POSTGRES_HOST}" -e "POSTGRES_DB=${POSTGRES_DB}"  -e "POSTGRES_USER=${POSTGRES_USER}" -e "POSTGRES_PASSWORD=${POSTGRES_PASSWORD}" geographica/elcano_iepg_webbuilder
  
}

function build(){

  buildapps $1;
  #docker rm -f tmp_build_db
  docker-compose -f docker-compose.$1.yml build
  docker build -t geographica/elcano_iepg_api www-srv
}

function prerequisites(){
  echo -n "Installing prerequisites..."
  # Fetching submodules
  git submodule init
  git submodule update
  docker build -t geographica/elcano_iepg_webbuilder www

  # Install scripts to upload to amazon s3. If this line fails and you don't want to upload it to Amazon S3/CloudFront just comment it.
  #gem install s3_website
}

source config.env;

case $1 in
  start)
    docker-compose -f docker-compose.$2.yml start
    shift
    ;;
    
  restart)
    docker-compose -f docker-compose.$2.yml stop
    docker-compose -f docker-compose.$2.yml start
    shift # past argument=value
    ;;

  refresh)
    
    prerequisites;
    build $2;
    docker-compose -f docker-compose.$2.yml stop
    docker-compose -f docker-compose.$2.yml rm -f
    docker-compose -f docker-compose.$2.yml up -d

    nginx refresh
    shift
    ;;

  prerequisites)
    prerequisites;
    shift
    ;;

  buildapps)
    prerequisites;
    buildapps $2;
    shift
    ;;
  stop)
    docker-compose -f docker-compose.$2.yml stop
    shift
    ;;
  *)
      echo "Bad parameters"
      exit
    ;;
esac
