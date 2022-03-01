import twitter
import sys

api = twitter.Api(consumer_key='96526cf1-7d50-4785-92cc-fe7b4efc1b6f',
                  consumer_secret='3a5e85f5-d6cc-4f1b-b14f-f68e9eb8bbbd',
                  access_token_key='af442c1a-6666-4da4-a7af-d97998846a62',
                  access_token_secret='57fa0e14-2559-45f7-aded-1e86b74ab1d3')

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
