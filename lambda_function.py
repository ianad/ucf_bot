import tweepy
import json
from datetime import date

from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
	
def get_last_loss():
	last_loss = date(2016,12,17)
	return(last_loss)
	
def daily_tweet():
	today = date.today()
	last_loss = get_last_loss()
	delta = today - last_loss
	tweet_content = str(delta.days)+' days ago'
	return(tweet_content)

def lambda_handler(event,context):
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
	api = tweepy.API(auth)
	tweet_content = daily_tweet()
	api.update_status(tweet_content)
	return(tweet_content)