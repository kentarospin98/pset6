from flask import Flask, redirect, render_template, request, url_for

import helpers
import os
import sys
from analyzer import Analyzer

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():

    # validate screen_name
    screen_name = request.args.get("screen_name", "")
    if not screen_name:
        return redirect(url_for("index"))

    # get screen_name's tweets
    tweets = helpers.get_user_timeline(screen_name, count=100)
    
    positives = os.path.join(sys.path[0], "positive-words.txt")
    negatives = os.path.join(sys.path[0], "negative-words.txt")
    anz = Analyzer(positives, negatives)
    
    po = ne = nu = 0
    for tweet in tweets:
        if anz.analyze(tweet) > 0:
            po += 1
        elif anz.analyze(tweet) < 0:
            ne += 1
        else:
            nu += 1
    
    positive, negative, neutral = po/len(tweets)*100,ne/len(tweets)*100,nu/len(tweets)*100

    # generate chart
    chart = helpers.chart(positive, negative, neutral)

    # render results
    return render_template("search.html", chart=chart, screen_name=screen_name)
