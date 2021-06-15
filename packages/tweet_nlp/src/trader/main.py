import os
from Twitter import TwitterController, TweetResponse, Tweet
import sys 

if __name__ == "__main__":
    t = TwitterController(bearer=os.environ.get("BEARER_TOKEN"))
    query = "ESPO"
    maximum = 100
    response = t.search_tweets(query, maximum)


    if (response.errorMsg):
        print(response.errorMsg)
        print(response.errors)

        sys.exit()
    

    tweets = response.tweets

    rt_count = 0
    for tweet in tweets:
        if tweet.find('RT ') == 0:
            print('got rt')
            print(tweet.encode('utf8'))
            rt_count += 1

    # Parse the usernames out of the tweets
    print(rt_count)

    # Discard RT's (not enough info)