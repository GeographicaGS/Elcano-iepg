# coding=UTF8

"""
Configuration
"""

basePath = "/Users/alasarr/dev/elcano-iepg/"

backend = {
    "tmpFolder": basePath + "www/cdn/backend/tmp",
    "mediaFolder": basePath + "www/cdn/medina"
}

MemcachedConfig = {
    "enabled": False,
    "host": "###",
    "port": "###",
    "expiration": 30
}

explora = {
    "SECRET_KEY": "###"
}

frontend = {
    "twitter_api_key": "###",
    "twitter_api_secret": "###",
    "twitter_token": "###",
    "twitter_token_secret": "###",
    "mediaFolder": "###"
}

PostgreSqlConfig = {
    "host": "###",
    "user": "###",
    "passwd": "###",
    "db": "###",
    "port": ###
}

# Seeds for clustering quotes. Min 3
quotesClustersSeeds = 6
