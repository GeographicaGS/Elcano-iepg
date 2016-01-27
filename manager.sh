#!/bin/bash

function buildapps(){
  cd www/src;
  r=`jake`

  if [ $? -eq 0 ]; then
    echo "OK"
  else
    echo "FAIL"
  fi
  cd ../..;
}

function build(){
  buildapps;
  docker-compose -f docker-compose.$1.yml build
  docker build -t geographica/elcano_iepg_api www-srv
}

function prerequisites(){
  echo -n "Installing prerequisites..."
  # Fetching submodules
  git submodule init
  git submodule update

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
    docker-compose -f docker-compose.$2.yml up pgsql
    build $2;
    docker-compose -f docker-compose.$2.yml stop
    docker-compose -f docker-compose.$2.yml rm -f
    docker-compose -f docker-compose.$2.yml up -d

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
    ;;
    *)
      echo "Bad parameters"
      exit
    ;;
esac
