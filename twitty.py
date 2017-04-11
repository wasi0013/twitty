import tweepy
import os, json, random


current_dir = os.path.dirname(os.path.abspath(__file__))
try:
    with open(current_dir+ '/' + 'config.local.json') as f:
        config = json.load(f)
except FileNotFoundError:
    with open(current_dir + '/' + 'config.json') as f:
        config = json.load(f)

consumer_key= config["consumer_key"]
consumer_secret=config["consumer_secret"]
access_token=config["access_token"]
access_token_secret= config["access_token_secret"]
protected_friends = config["protected_friends"]
    
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
print("logged in as:",api.me().name)


def show_protected_friends():
    print("list of all protected friends:")
    for friend in protected_friends:
        print("https://twitter.com/%s"%api.get_user(friend).screen_name)

def friendlist_purifier():
    name = api.me().name
    friendlist = api.friends_ids(name)        
    followers = api.followers_ids(name)    
    for suspect in friendlist:
        if suspect not in followers and suspect not in protected_friends:
            print("Unfollowing: https://twitter.com/%s" % api.get_user(suspect).screen_name)
            api.destroy_friendship(suspect)        
    print("Number of friends after purification: %d(%d)" % (api.me().friends_count, len(friendlist)))

if __name__ == '__main__':
    # removes all who unfollowed you except protected_friends    
    # friendlist_purifier()
