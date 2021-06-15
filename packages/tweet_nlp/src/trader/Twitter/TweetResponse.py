import numpy as np 

"""
Wraps the data sent back with a tweet and gives helper methods
to help with parsing the data
"""
class TweetResponse:

    data = []   # array of Tweet objects
    metadata = None
    
    tweets = []  #

    errorMsg = ""
    errors = ""

    
    def __init__(self, response):
        if ('data' not in response.keys()):
            self.errorMsg = "Error: Got no response data from twitter"
            self.errors = response['errors']
            return
        else:
            self.data = response['data']
        
        #self.filter_to_english()
        self.isolate_tweet_text()
        

    def isolate_tweet_text(self):
        if len(self.tweets == 0):
            return 
        isolate_tweets = np.vectorize(lambda obj: obj['text'])
        self.tweet_text = isolate_tweets(np.array(self.tweets))

    def filter_to_english(self):
        pass


    
        
    
