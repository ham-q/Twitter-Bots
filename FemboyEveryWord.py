import tweepy
import requests
import random
import urllib.request
from time import sleep
import os

auth = tweepy.OAuthHandler("consumer_key", "consumer_secret")
auth.set_access_token("access_token", "access_token_secret")

word_url = "https://www.mit.edu/~ecprice/wordlist.10000"
response = urllib.request.urlopen(word_url)
long_txt = response.read().decode()
words = long_txt.splitlines()
random.shuffle(words)

api = tweepy.API(auth)

while True:
    word = words.pop()
    a = api.update_status("Femboy " + word)
    try:
        user = "femboy"+word
        femboy = api.get_user(user)
        api.update_status("There is a @"+user+" :3", a.id)
    except:
        api.update_status("There is no user called @"+user, a.id)
    sleep(7200)