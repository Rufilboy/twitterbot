import os
import config
import tweepy
import pandas


# Authenticate to Twitter
auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth)

# Create a tweet
api.update_status("Hello guys, it's been a while here.")

# Search term and the date_since date as variables
search_words = "#devops"
date_since = "2022-01-01"