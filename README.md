=============
Elcano - IEPG
=============

The Elcano [Global Presence Index](http://www.globalpresence.realinstitutoelcano.org) is an annual measurement of the projection in the world of 90 countries based on three dimensions: Economic, Military, Soft.

This is a project from [Elcano Royal Institute](http://www.realinstitutoelcano.org) of strategic and international studies and [Geographica](https://geographica.gs). 

# Tech overview 
This project is a web platform composed by 3 APIs developed in Python (Flask) at the server side. At the client side, it uses an HTML application who uses [Backbone JS](http://backbonejs.org).

To deploy and develop it uses [Docker](https://www.docker.com).

# How to prepare the environment

Install [Docker](https://docs.docker.com/engine/installation) 1.8+ and [docker-compose](https://docs.docker.com/compose/install/) 1.5.2+.

Create the data containers. Please, make your self a favor and don't use local volumes.
```
docker create --name elcano_iepg_pgdata -v /data debian /bin/true
docker create --name elcano_iepg_redisdata -v /data debian /bin/true
docker create --name elcano_iepg_mediadata -v /media debian /bin/true
```

Create the config file using the sample and add your own data.
```
cp config.sample.env config.env
```

Set the environment variables 
```
source config.env
```

Import the database
```
docker-compose -f docker-compose.dev.yml up -d pgsql
docker exec elcanoiepg_pgsql_1 psql -U postgres -c  "CREATE USER $POSTGRES_USER with password '$POSTGRES_PASSWORD'"
docker exec elcanoiepg_pgsql_1 psql -U postgres -c  "CREATE DATABASE $POSTGRES_DB with owner $POSTGRES_USER"
docker exec -i elcanoiepg_pgsql_1 psql -U postgres -d $POSTGRES_DB < <dumpfile.sql>
```

Build the image for API.
```
docker build -t geographica/elcano_iepg_api www-srv
```

Set your local domain. add to /etc/hosts
```
echo 127.0.0.1 'dev.elcano-iepg.geographica.gs dev.explora.elcano-iepg.geographica.gs dev.backend.elcano-iepg.geographica.gs' >> /etc/hosts

If you run on OSX:
echo $(docker-machine ip default) 'dev.elcano-iepg.geographica.gs dev.explora.elcano-iepg.geographica.gs dev.backend.elcano-iepg.geographica.gs' >> /etc/hosts
```

Start
```
docker-compose -f docker-compose.dev up
```

Propagate the data from Postgres to REDIS.

```
docker exec elcanoiepg_api_backend_1 python updatecache.py 
```

Prepare clients. TODO: we need to use the latest version of [Sting](https://github.com/GeographicaGS/Sting) to be able to read data of environment values (config.env) inside config.js files.
```
cp www/src/explora/js/config.changes.js www/src/explora/js/config.js
cp www/src/frontend/js/config.changes.js www/src/frontend/js/config.js
cp www/src/backend/js/config.changes.js www/src/backend/js/config.js
```

Create the image of the web builder
```
docker build -t geographica/elcano_iepg_webbuilder www
```

# Dev environment
To start the application, once you've installed everything. Just type.
```
source config.env
docker-compose -f docker-compose.dev up
```

# Scripts

Update the whole platform from XLSX. From the input file www-srv/src/data_calculus/year2015.xlsx it updates de PostgreSQL and REDIS. It also makes a backup of the iepg_data schema of PostgreSQL.
```
docker exec elcanoiepg_api_backend_1 python flux_updatewholeapp.py 
```

RUN calculus engine XLSX to XLSX. From www-srv/src/data_calculus/year2015.xlsx, it generates the engine output at www-srv/src/data_calculus/calculus2015.xlsx.
```
docker exec elcanoiepg_api_backend_1 python flux_xlsxtoxlsx.py 
```

Update REDIS from PostgreSQL
```
docker exec elcanoiepg_api_backend_1 python updatecache.py 
```

UPDATE population and GDP
```
docker exec elcanoiepg_api_backend_1 bash -c "cd scripts && python pop_gdp.py" > gdp2015.sql
docker exec -i elcanoiepg_pgsql_1 psql -U postgres -d elcano_iepg < gdp2015.sql
docker exec elcanoiepg_api_backend_1 python updatecache.py 
```

# Get latest database
SSH to production server and execute

```
sudo su
source config.env
docker exec elcanoiepg_pgsql_1 pg_dump $POSTGRES_DB -U postgres > $POSTGRES_DB.sql
```

At the client:
```
source config.env
scp <user>@<server>:/<path>$POSTGRES_DB.sql .
docker-compose -f docker-compose.dev.yml up -d pgsql
docker exec elcanoiepg_pgsql_1 psql -U postgres -c  "DROP DATABASE $POSTGRES_DB"
docker exec elcanoiepg_pgsql_1 psql -U postgres -c  "CREATE DATABASE $POSTGRES_DB with owner $POSTGRES_USER"
docker exec -i elcanoiepg_pgsql_1 psql -U postgres -d $POSTGRES_DB < $POSTGRES_DB.sql

```

# Manager.sh
At production and staging we use manager.sh to start, stop and refresh the servers.

###Refresh
It recreates the container, it's mandatory if you're uploading a new version.
```
./manager.sh refresh <environment>

# Staging example
./manager.sh refresh staging
```

###Restart
It restarts the containers.
```
./manager.sh restart <environment>
```

###Buildapps
It compiles the frontend apps using the geographica/elcano_iepg_webbuilder container
```
./manager.sh buildapps <environment>
```

