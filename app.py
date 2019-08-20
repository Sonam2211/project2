from flask import Flask, request, Response
from flask import render_template, jsonify

from tweepy import Stream, API
import tweepy
from tweepy import OAuthHandler
from config import CONSUMER_KEY, CONSUMER_SECRET
from config import ACCESS_TOKEN, ACCESS_TOKEN_SECRET

NUM_TWEETS = 10

# OAuth process
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = API(auth, wait_on_rate_limit=True)
api.verify_credentials()
print("Authentication OK")

# create application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tweets/', methods=['GET'])
def tweets():
    source = request.args.get('source')
    print(source)

    texts = []
    db = set()
    counter = 0
    for tweet in tweepy.Cursor(api.search, q="#" + source[1:]).items():
        # let's ignore the retweets
        if tweet.text.startswith("RT @"):
            continue

        # check if we have already added this tweet
        if tweet.text not in db:
            db.add(tweet.text)
            texts.append(tweet.text)
            if counter >= NUM_TWEETS:
                # we got the required number of tweets, let's exit
                break
            else:
                counter += 1
    
    cloudtext = "".join(texts).strip()
    cloudtext = " ".join(cloudtext.splitlines())
    return render_template('tweets.html', title="Displaying WordCloud for: " + source, texts=texts, cloudtext=cloudtext)


if __name__ == "__main__":
    app.run(debug=True, threaded=True, host="0.0.0.0", port=4444)
