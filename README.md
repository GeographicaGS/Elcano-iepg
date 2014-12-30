=============
Elcano - IEPG
=============

Web del Índice Elcano de presencia global del Real Instituo Elcano


## About

Este proyecto esta compuesto por dos apliaciones webs, una para el backend y otra para el frontend. Las dos aplicaciones tiene el mismo stack tecnológico, BackboneJS en el cliente y Flask en el servidor.

La aplicación JS se encuentra en el directorio www y los servicios en www-srv.

## Instalación del entorno de desarrollo para servicios

### Dependencias

Estas son las aplicaciones de las que depende Elcano - IEPG:

  - Redis 2.8.19;
  - PostgreSQL 9.1.2;
  - PostGIS 1.5.8 (sobre la PostgreSQL anterior).

Actualmente, dado que los nuevos proyectos en Geographica han comenzado a
utilizar versiones más modernas de PostgreSQL y de PostGIS, estos dos elementos
los utilizamos dockerizados (ver
https://github.com/GeographicaGS/Docker-PostgreSQL-9.1.2-PostGIS-1.5.8).

### Submódulos

Este proyecto usa un par de submodulos. Para ver dónde están:

    git submodule

Para inicializarlos:

    git submodule init
	git submodule update

El submódulo __www-srv/src/flux_lib__ utiliza la branch __elcano-changes__,
release (tag) __v0.2-Elcano__, así que hacer un pull de esta tag.

### Configuración y restauración de la base de datos

Primero, configurar los scripts de base de datos, renombrando el fichero
__00-config.sql.config__ a __00-config.sql__ y rellenando los datos de acceso a
la PostgreSQL. Para restaurar la copia funcional de la base de datos, entrar en
el directorio __database__ y ejecutar el script __01-create_env-dev.sql__:

    psql -h localhost -p 5454 -U postgres postgres -c "\i 01-create_env-dev.sql"
    &> out

para borrar toda la base de datos de desarrollo, utilizar el script
__05-database-drop.sql__:

    psql -h localhost -p 5454 -U postgres postgres -c "\i 05-database-drop.sql"
    &> out

### Entorno de desarrollo de servicios

Primero hemos de instalar el Virtualenv de Python:

- en Mac OSX : 

```$ sudo pip install virtualenv```

- en Ubuntu:

```$ sudo apt-get install python-virtualenv```

Creamos un entorno virtual en el directorio __www-src__:

```$ virtualenv venv```
 
A continuación nos ponemos en el entorno virtual:

```. venv/bin/activate ```

### Librerías de Python

Una vez dentro del entorno virtual instalamos los paquetes necesarios con PIP:

```
pip install Flask
pip install psycopg2
pip install tweepy
pip install python-memcached
pip install redis
pip install numpy
pip install xlsxwriter
pip install xlrd
#only to debug purpose
$ pip install ipdb
```

### Arranque de las APIs

Editamos el fichero de configuración global
```
cp src/common/config_changes.py  src/common/config.py
```

```
$ python src/run_backend.py
```

Si todo ha ido bien debe mostrar:

```
 * Running on http://127.0.0.1:5001/
 * Restarting with reloader
```

Para la subida de ficheros el backend necesita de una serie de carpetas, la ubicación de esta carpetas se especifica en los ficheros de configuración. Tenemos que crearlas y darle permisos de escritura al usuario que lanza el backend.

```
mkdir /Users/alasarr/dev/elcano-iepg/www/cdn/backend/tmp
mkdir /Users/alasarr/dev/elcano-iepg/www/cdn/media
chmod 755 /Users/alasarr/dev/elcano-iepg/www/cdn/backend/tmp
chmod 755 /Users/alasarr/dev/elcano-iepg/www/cdn/media
```

### Twitter y Explora

Por último, para que funcionen ambos servicios, se deben rellenar los datos en
__common/config.py__ de los datos de las claves de Twitter y de Explora.

#### Frontend

Tenemos que crear los ficheros de configuración, estos no están en el trunk.

```
# copiamos el fichero de configuración de la base datos
$ cp src/frontend/config_changes.py src/frontend/config.py
```

Abre el fichero config.py y modificalo con los parámetros adecuados.

Una vez hecho esto ya podemos arrancar el frontend ejecutando:

```
$ python src/run_frontend.py
```

Si todo ha ido bien debe mostrar:

```
 * Running on http://127.0.0.1:5000/
 * Restarting with reloader
```

### Building aplicación JS

La aplicación JS se compila usando node js y las siguientes librerías.

Instala node JS y ejecuta lo siguiente.

```
sudo npm install -g jake
sudo npm install -g uglify-js
sudo npm install -g uglifycss
sudo npm install -g jshint
sudo npm install -g pg
sudo npm install -g less
# necesario para el builder-watcher 
sudo npm install -g node-watch

export NODE_PATH=/usr/local/lib/node_modules
```

Ahora creamos los ficheros de configuración
``` 
# configuración del builder
cp build/config.changes.js build/config.js
# configuración del backend
cp backend/js/config.changes.js backend/js/config.js
# configuración del frontend
cp frontend/js/config.changes.js frontend/js/config.js
```

Una vez hecho esto ejecuta sobre www/src:

```
jake
```

O si quieres hacer el build en modo debug

```
jake debug
```

### Configuración de apache

Las aplicaciones están hechas para correr en el raíz del apache. Por eso hay que crear dos virtualhost.

* Frontend: dev.iepg.es que sirve el directorio cdn/frontend.
* Backend: dev.backend.iepg.es que sirve el directorio cdn/backend.

Para que no haya problemas de cross-origin, tenemos que configurar apache para que haga un proxy al servidor de Flask.

```
###proxy para frontend
ProxyPass /api http://127.0.0.1:5000
###proxy para backend
ProxyPass /api http://127.0.0.1:5001
```

También hay que añadirle algunos alias.

```
Alias /media /Users/alasarr/dev/elcano-iepg/www/cdn/media

# Este solo es necesario si hacemos el build del JS en modo debug
Alias /src /Users/alasarr/dev/elcano-iepg/www/src

```

Si estas en MacOSX aconsejo que uses MAMP que hace esto mucho más fácil.

Para apache os pongo algunos ficheros de configuración.

```
<VirtualHost *:80>
    DocumentRoot "/Users/alasarr/dev/elcano-iepg/cdn/frontend"
    ServerName dev.iepg.es
    ErrorLog "/private/var/log/apache2/dev.iepg.es-error_log"
    CustomLog "/private/var/log/apache2/dev.iepg.es-access_log" common
    ProxyPass /srv http://127.0.0.1:5000/
    ProxyPassReverse /srv http://127.0.0.1:5000
</VirtualHost>

<VirtualHost *:80>
    DocumentRoot "/Users/alasarr/dev/elcano-iepg/cdn/backend"
    ServerName dev.backend.iepg.es
    ErrorLog "/private/var/log/apache2/dev.backend.iepg.es-error_log"
    CustomLog "/private/var/log/apache2/dev.backend.iepg.es-access_log" common
    ProxyPass /srv http://127.0.0.1:5001/
    ProxyPassReverse /srv http://127.0.0.1:5001
</VirtualHost>
```

Si todo a ido bien tendremos el frontend en dev.iepg.es y el backend en dev.backend.iepg.es

## Backend

### API

Aquí las notas principales de la API del backend

#### Configuración

Aquí las notas de la configuración de la API del backend

### JS

Aquí las notas de la aplicación javascript del backend.

#### Configuración

Aquí las notas de la configuración de la aplicación javascript del backend.


## Frontend

### API

Aquí las notas principales de la API.

#### Configuración

Aquí las notas de la configuración de la API.

### WEB

Aquí las notas de la aplicación web.

### Maquetación

En el directorio www/src/frontend/design van las maquetaciones de los ficheros.

La idea es que sobre este directorio se creen los htmls de cada sección, los programadores se encargan de coger estos ficheros y darle vida, una vez que lo hayan procesado, el fichero se mete en la carpeta processed.

####Reglas de maquetación

1) Los ficheros css se crean o se modifican sobre la carpeta www/src/frontend/css.
2) El index.html es el fichero de plantilla, no se le añaden ni librerías ni nuevos estilos.
3) Si se cambia algo en el base.css o reset.css hay que consultarlo con Alberto Asuero.
4) El fichero styles.css tiene los estilos globales de la página.
5) Los estilos propios de una sección van en un fichero aparte.
6) Las imagenes están en el directorio www/cdn/frontend

####Build
Dentro de la carpeta build.js hay un fichero <b>build.js</b> que se encarga de hacer el build. Lo que hace este fichero es coger todos los css que estan en la variable deps.css, hacerle el procesado de less y dejarlo en el fichero main.css que es el que cargan las plantillas.

El fichero <b>builder-watcher.js</b> detecta cuando editamos un fichero dentro de la carpeta www/src/frontend/css y ejecuta un build.

#### Configuración de apache

Para que todo funcione hay que poner el root de apache apuntando a www/src/frontend/design y configurar el Alias para las imágenes como se muestra a continuación.

Al virtual host debemos de ponerle
```
Alias /img /Users/alasarr/dev/elcano-iepg/www/cdn/frontend/img
```

#### Configuración

Aquí las notas de la configuración de la web.


# Checklist de entorno de desarrollo

## Arranque

Hay que seguir los siguientes pasos: 

- arrancar PostgreSQL 9.1.2 / PostGIS 1.5.3 (posiblemente dockerizada):

        pg_ctl-9.1.2-1.5.3 -D . start

- arrancar Redis:

        redis-server redis-2.8.14.conf &

- activar el entorno virtual en __www-src__:

        . venv/bin/activate

- activar servicios Flask:

        src/run_backend.py (port 5000)
	    src/run_explora.py (port 5002)
        src/run_frontend.py (port 5001)

## Parada

Pasos: 

- parar PostgreSQL (posiblemente dockerizada):

        pg_ctl-9.1.2-1.5.3 -D . stop

- parar Redis:

        redis-cli shutdown save

# Carga de datos en Redis

La aplicación funciona cargando datos desde la PostgreSQL en una Redis. Para refrescar los datos Redis desde la PostgreSQL, utilizar el script _www-srv/src/datacache.py_.
