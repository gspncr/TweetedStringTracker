from tw import stringByUserWithID
from counter import tweetCount
from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def home():
    stringByUserWithID('Vegan', 'isitvegan')
    count = tweetCount()
    count = str(count)
    return json.dumps({"count":count})
    
if __name__ == "__main__":
    app.run(debug=True)