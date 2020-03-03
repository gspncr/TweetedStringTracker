from tinydb import TinyDB, Query, where
from tinydb.operations import increment
import json

db = TinyDB('db.json')
User = Query()

#Start the DB with this counter, before we started counting
def startDB():
    if db.search(User.tweetedTimes.exists()):
        pass
        #print("records reloaded")
    else:
        db.insert({'tweetedTimes': 240})
        print("inserting record with 12")

def compareDB(tweetID):
    if db.search(User.id == tweetID):
        return True
    else:
        db.insert({'id':tweetID})
        db.update(increment('tweetedTimes'), where('tweetedTimes').exists())
        return False

def tweetCount():
    count = db.search(User.tweetedTimes)
    return count[0]['tweetedTimes']

startDB()