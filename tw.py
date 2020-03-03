import requests, json
from counter import compareDB

def getBearer():
    authURL = "https://api.twitter.com/oauth2/token"
    consumerKey = 'consumer key'
    consumerSecret = 'consumer secret'
    data = {'grant_type': 'client_credentials'}
    response = requests.post(authURL, data=data, auth=(consumerKey, consumerSecret))

    def makeToken(response):
        tokenType = json.loads(response.text)['token_type']
        accessToken = json.loads(response.text)['access_token']
        token = tokenType + ' ' + accessToken
        return token

    return makeToken(response)

def getLatestTweet(user):
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=" + user + "&count=1&exclude_replies=true&include_rts=false"
    headers = {
        'Authorization': getBearer()
    }
    response = requests.request("GET", url, headers=headers)
    return response.text

def stringByUser(str, user):
    tweet = getLatestTweet(user)
    tweet = json.loads(tweet)[0]['text']
    find = str in getLatestTweet(user)
    return find

def stringByUserWithID(str, user):
    tweetObj = getLatestTweet(user)
    tweet = json.loads(tweetObj)[0]['text']
    tweetID = json.loads(tweetObj)[0]['id']
    compareDB(tweetID)
    return tweetID, tweet

#print(stringByUser('Vegan', 'isitvegan'))