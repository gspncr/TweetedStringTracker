from tw import stringByUserWithID
from counter import tweetCount
from flask import Flask
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/fetchTweets")
@cross_origin()
def home():
    stringByUserWithID('Vegan', 'isitvegan')
    count = tweetCount()
    count = str(count)
    return json.dumps({"count":count})
    
if __name__ == "__main__":
    app.run(
        debug=True
    )