""" Get all historic tweets from user. """

import GetOldTweets3 as got

from config import *

tweetCriteria = got.manager.TweetCriteria().setUsername(USER).setMaxTweets(NUM_TWEETS)

tweets = got.manager.TweetManager.getTweets(tweetCriteria)

for t in tweets:
    print(t.text)
