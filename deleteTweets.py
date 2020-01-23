import twitter
import sys

api = twitter.Api(consumer_key='',
                  consumer_secret='',
                  access_token_key='',
                  access_token_secret='')

filepath = sys.argv[1]
with open(filepath) as tweets:
    tweetID = tweets.readline()
    while tweetID:
        print(tweetID)
        try:
            api.DestroyStatus(tweetID.rstrip())
        except:
            print('No such tweet')
        tweetID = tweets.readline()
