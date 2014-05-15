# coding=UTF8

"""

Helpers for the frontend.

"""
from common.config import frontend as configFrontend
from common.const import frontend as constFrontend
import tweepy


def authorHelper(authorData, lang):
    """Gets the data of an author and returns a comprehensive analysis of them."""
    author = dict()
    author["id_author"]=authorData["id_author"]
    author["id_document"]=authorData["id_document"]

    if authorData["twitter_user"]:
        try:
            author["twitter_user"]=authorData["twitter_user"]
            t=twitterGetUserInfo(authorData["twitter_user"])
            author["name"]=t.name
            author["position"]=t.description if t.description!="" else None
            author["image"]=t.profile_image_url_https.replace("_normal","_bigger")
        except:
            return (cons.errors["-4"])
    else:
        author["twitter_user"]=None
        author["name"]=authorData["name"]
        author["position"]=authorData["position_"+lang]
        author["image"]="default"

    return author


def coalesce(matrix):
    """Coalesces a matrix to the first element not None."""
    for i in matrix:
        if i!=None:
            return i
    
    return None


"""
Twitter helper.

To check the return of a model execute __getstate__.
For example: twitter.helper.getUserInfo("alasarr").__getstate__()
"""
auth = tweepy.OAuthHandler(configFrontend["twitter_api_key"], configFrontend["twitter_api_secret"])
auth.set_access_token(configFrontend["twitter_token"], configFrontend["twitter_token_secret"] )

def twitterGetLatestTweets():
    """Get tweets."""
    api = tweepy.API(auth)
    return api.user_timeline(count=cons.maxTweets,screen_name="rielcano")


def twitterGetUserInfo(screen_name):
    """Get tweets."""
    try:
        api = tweepy.API(auth)
        return api.get_user(screen_name=screen_name)
    except tweepy.error.TweepError:
        return None
