import os
import config
import tweepy
import pandas as pd


# Authenticate to Twitter
auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth)

# Create a tweet
api.update_status("Hello guys, it's been a while here. I'm tweeting from #Python. @IlyasRufai" )

# Search term and the date_since date as variables
search_words = "#devops"
date_since = "2022-01-01"

# Collect tweets
tweets = tweepy.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(5)

# Iterate and print tweets
for tweet in tweets:
    print(tweet.text)

# List of tweets
# [tweet.text for tweet in tweets]

new_search = search_words + " -filter:retweets"

users_locs = [[tweet.user.screen_name, tweet.user.location] for tweet in tweets]

# DataFrame for user and location
tweet_text = pd.DataFrame(data=users_locs, 
                    columns=['user', "location"])
tweet_text