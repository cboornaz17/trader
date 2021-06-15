import pymongo

client = pymongo.MongoClient("mongodb://mongoadmin:secret@localhost:27017/admin")

tweet_db = client['trader']
tweet_collection = tweet_db['historical_tweets']

sample_data = {'ticker': 'tweeeet1', 'ticker2': 'tweeeet3'}

tweet_collection.insert_one(sample_data)


print(tweet_collection.find_one())