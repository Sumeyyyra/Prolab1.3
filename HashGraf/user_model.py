from data_structures import LinkedList

class User:
    def __init__(self, username, full_name, followers_count, following_count, language, region):
        self.username = username
        self.full_name = full_name
        self.followers_count = followers_count
        self.following_count = following_count
        self.language = language
        self.region = region
        self.tweets = LinkedList()  
        self.following = LinkedList()  
        self.followers = LinkedList()  

    def add_tweet(self, tweet_content):
        self.tweets.insert(self.username, tweet_content)

    def add_following(self, user):
        self.following.insert(user, user)  

    def add_follower(self, user):
        self.followers.insert(user, user)
