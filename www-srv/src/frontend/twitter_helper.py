# coding=UTF8

"""

Twitter helper.

"""
from config import cfgFrontend


auth = tweepy.OAuthHandler(cfgFrontend["twitter_api_key"], cfgFrontend["twitter_api_secret"])
auth.set_access_token(cfgFrontend["twitter_token"], cfgFrontend["twitter_token_secret"] )

def getLatestTweets():
    """Get tweets."""
    api = tweepy.API(auth)
    return api.user_timeline(count=5,screen_name="rielcano")

