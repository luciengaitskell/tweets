import GetOldTweets3 as got

tweetCriteria = got.manager.TweetCriteria().setUsername("lzdarkmatter").setMaxTweets(2)
tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]
print(tweet.text)
