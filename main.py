import tweepy
import time
from secret import *
from twitch import TwitchHelix

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

twitch_client = TwitchHelix(client_id=TWITCH_ID)
live = False
while True:
    try:
        stream = twitch_client.get_streams(user_logins=USER_LOGIN)
        if not stream:
            if live == True:
                # delete tweet
                last_tweets = api.user_timeline(id=api, count=10)
                for tweet in last_tweets:
                    if "live auf @TwitchDE" in str(tweet.text):
                        tweet.destroy()
                        break
                live = False

        else:
            if live == False:
                game_id = stream[0]["game_id"]
                game = twitch_client.get_games(game_ids=game_id)
                game_name = game[0]["name"]

                # post tweet
                api.update_status(f"Ich bin jetzt mit {game_name} live auf @TwitchDE! {TWITCH_URL}")
                live = True
    except:
        print("Failed")
        pass
    time.sleep(15)