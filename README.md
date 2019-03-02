# TwitterTwitchBot

#### What is that for?
That's a small script which can be used to post a tweet on your Twitter account when you're going live on Twitch and deletes this post when you're offline.

#### How to use?
1. Install Python 3.6.x.
2. ``pip install tweepy python-twitch-client`` to install requirements.
3. Replace the stuff in ``secret.py`` to your own stuff.
4. Change string in line 32 to whatever you want to be posted. (optional)
5. Change string in line 20. (required if line 32 was changed)
6. Run ``main.py``.