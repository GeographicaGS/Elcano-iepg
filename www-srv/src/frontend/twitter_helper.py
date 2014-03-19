# coding=UTF8

"""

Twitter helper.

To check the return of a model execute __getstate__.
For example: twitter.helper.getUserInfo("alasarr").__getstate__()

"""
from config import cfgFrontend

import tweepy

auth = tweepy.OAuthHandler(cfgFrontend["twitter_api_key"], cfgFrontend["twitter_api_secret"])
auth.set_access_token(cfgFrontend["twitter_token"], cfgFrontend["twitter_token_secret"] )

def getLatestTweets():
    """Get tweets."""
    api = tweepy.API(auth)
    return api.user_timeline(count=5,screen_name="rielcano")

def getUserInfo(screen_name):
    """Get tweets."""
    try:
        api = tweepy.API(auth)
        return api.get_user(screen_name=screen_name)
    except tweepy.error.TweepError:
        return None

