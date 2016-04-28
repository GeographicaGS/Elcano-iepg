# coding=UTF8

"""
Configuration
"""

import os

basePath = "/usr/src/app/"

backend = {
    "tmpFolder": "/tmp",
    "mediaFolder": "/media"
}

# Force to set a secret KEY
SECRET_KEY = os.environ["API_SECRET_KEY"]

frontend = {
    "twitter_api_key": os.environ.get("TWITTER_API_KEY",None),
    "twitter_api_secret": os.environ.get("TWITTER_API_SECRET",None),
    "twitter_token": os.environ.get("TWITTER_TOKEN",None),
    "twitter_token_secret": os.environ.get("TWITTER_TOKEN_SECRET",None),
    "mediaFolder": basePath + "www/cdn/media"
}

PostgreSqlConfig = {
    "host": os.environ.get("POSTGRES_HOST","pgsql"),
    "user": os.environ.get("POSTGRES_USER","elcano_iepg"),
    "passwd": os.environ.get("POSTGRES_PASSWORD","elcano_iepg"),
    "db": os.environ.get("POSTGRES_DB","elcano_iepg"),
    "port": os.environ.get("POSTGRES_PORT",5432)
}

RedisConfig = {
    "host": os.environ.get("REDISCFG_HOST","redis"),
    "port": os.environ.get("REDISCFG_PORT",6379)
}


# Seeds for clustering quotes. Min 3
quotesClustersSeeds = 15
