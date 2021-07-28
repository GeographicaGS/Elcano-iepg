# Deploy instructions

Before to start deploying to Staging you need to change code, prepare data files and sql scripts.


# STAGING (Lincoln Server)

pre-step: make a database backup

0. sudo git pull origin staging
1. Database scripts: psql -h localhost -U elcano_iepg_admin -d elcano_iepg < run_update.sql
2. cd www-srv/src
3. python flux_updatefromcalculatedxlsx.py calculus2020.xlsx 15 141 12 28
4. python updatecache.py
5. Add new year. Open with vim this files and add year:
  - explora/js/config.js
  - frontend/js/config.js
6. docker stop cadvisor-monitor && ./manager.sh refresh staging && docker start cadvisor-monitor

# PROD (Olivia Server)

WARNING: not dockerized environment :-)

pre-step: make a database backup:
pg_dump -h localhost -U elcano_iepg_admin -d elcano_iepg > elcanoiepg_<fill with year month and day>_dump.sql

0. sudo git pull origin master
1. Database scripts: psql -h localhost -U elcano_iepg_admin -d elcano_iepg < run_update.sql
2. cd www-srv/ && . venv/bin/activate
3. cd src && python flux_updatefromcalculatedxlsx.py calculus2020.xlsx 15 141 12 28
4. python updatecache.py
5. deactivate
6. Add new year. Open with vim this files and add year located at www/src folder:
  - explora/js/config.js
  - frontend/js/config.js
6. Change PROD configs:
  - cp www-srv/src/common/config_PROD.py www-srv/src/common/config.py
  - cp www-srv/src/frontend/downloads_PROD.py www-srv/src/frontend/downloads.py
  - cp www/src/build/config_PROD.js www/src/build/config.js
7. cd www/src
8. jake
9. sudo service uwsgi restart
10. sudo service nginx restart
