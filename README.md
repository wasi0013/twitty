# Twitty  
A utility built using tweepy to ease up twitter account maintenance 

## Installation:

* install [Python 3](https://www.python.org/downloads/)
* install [pip](https://pypi.python.org/pypi/pip)
* clone this repository 
## Dependency:  
* [tweepy](https://www.tweepy.org)

install dependencies `pip install -r requirements.txt` 

## Methods added so far:


* `friendlist_purifier()` - unfollows who unfollowed or, never follow back, keeping a predefined list of people you follow safe (even if they unfollow)

* `show_protected_friends()` - shows list of friends safe from friendlist_purifier (if any)