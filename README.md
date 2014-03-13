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






