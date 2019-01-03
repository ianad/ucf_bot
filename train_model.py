import markovify
import tweepy
import config
from random import randint

auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

tweets=[]
for tweet in tweepy.Cursor(api.search,q='ucf football',since='2017-01-01',lang='en').items(50000):
    if not tweet.retweeted and 'RT @' not in tweet.text:
        tweets.append(tweet.text)
corpus = '\n'.join(tweets)
model = markovify.NewlineText(corpus)

def chickencase(text):
    if text is None:
        return(None)
    new_characters = []
    for character in text:
        if bool(randint(0,1)):
            new_characters.append(character.upper())
        else: new_characters.append(character.lower())
    new_text = ''.join(new_characters)
    return(new_text)

print(chickencase(model.make_short_sentence(200, tries=100)))