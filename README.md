# Elcano IEPG

## About

Este proyecto esta compuesto por dos apliaciones webs, una para el backend y otra para el frontend. Las dos aplicaciones tiene el mismo stack tecnológico, BackboneJS en el cliente y Flask en el servidor.

La aplicación JS se encuentra en el directorio www y los servicios en www-srv.

## Install

### Instalamos virtualvenv.

En Mac OSX : 

```$ sudo pip install virtualenv```

En Ubuntu:

```$ sudo apt-get install python-virtualenv```

Sobre el directorio www-srv ejecutamos

```$ virtualenv venv```
 
A continuación nos ponemos en el entorno virtual.

```. venv/bin/activate ```

### Librerías de python

Una vez dentro del entorno virtual instalamos los paquetes necesarios con pip.

```
$ pip install Flask
$ pip install psycopg2
$ pip install ipdb
```


### Arranque de las APIs

Lo primero es crear el fichero de configuración de la base de datos a partir de la plantilla.

```
$ cp src/model/base/PostgreSQL/config_changes.py src/model/base/PostgreSQL/config.py
```

Ahora lo abrimos con cualquier editor de texto y lo modificamos con nuestros parámetros.

#### Backend

Tenemos que crear los ficheros de configuración, estos no están en el trunk.

```
# copiamos el fichero de configuración de la base datos
$ cp src/backend/config_changes.py src/backend/config.py
```

Abre el fichero config.py y modificalo con los parámetros adecuados.

Una vez hecho esto ya podemos arrancar el backend ejecutando:

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
sudo npm install -g uglifyjs
sudo npm install -g uglifycss
sudo npm install -g jshint
sudo npm install -g pg
sudo npm install -g less

export NODE_PATH=/usr/local/lib/node_modules
```

Una vez hecho esto ejecuta sobre www/src:

```jake```

O si quieres hacer el build en modo debug

```jake debug```


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

#### Configuración

Aquí las notas de la configuración de la web.


## Building






