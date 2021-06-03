import tweepy
import time

from tweepy import api

api_key = "vV93qzYOJ6yYAyu50CP2fH4HA"
api_secret_key = "o04X3VgkSxP6mMK1WMeaUVA1lCkwEZGpQnotWf9uayyPLpgOoE"
access_key ="1400462491310649347-m4tBUKnwQR3Zl1JlF97OA06T665zUl"
access_secret = "ItlbEdlcBgz0hus0ibMa3zozADVuFanLB4hAOQNfsOMIo"

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_key, access_secret)

twitter_API = tweepy.API(auth)



twitter_API.update_status("Hello")