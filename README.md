# Twitter Wordcloud

A simple web page where end user can search and analyze the tweet. Enter a hastag and a wordcloud for that hashtag would be generated and shown in a web page.

[Tweepy](http://docs.tweepy.org/en/v3.5.0/getting_started.html#introduction) is used to connect to Twitter API with [Flask](http://flask.pocoo.org/) acting as the backend server.
D3's [wordcloud](https://bl.ocks.org/jyucsiro/767539a876836e920e38bc80d2031ba7) is used to generate wordclouds.

## Installing and running
* Install Flask a server side framework for Python.
```
pip install flask
```

* Create a Twitter App account  on [Twitter Developer Platform](https://developer.twitter.com/) and use access tokens for api request authentication.

* Install [Tweepy](http://docs.tweepy.org/en/v3.5.0/getting_started.html#introduction)
```
pip install tweepy
```

* Clone this repo


* Run app.py on terminal to start the application
```
>>>cd RTTS2
>>>python app.py
```

* Go to [http://localhost:4444](http://localhost:4444) in your web browser.

## Results 
![Screenshot 1](https://github.com/Sonam2211/projectnew/blob/master/screenshots/1.jpg)
![Screenshot 2](https://github.com/Sonam2211/projectnew/blob/master/screenshots/2.jpg)
