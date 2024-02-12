from data_structures import DictionaryLinkedList, MySet,HashTable
import re

def dfs_all_users_by_regions(users_hash_table):
    region_count = DictionaryLinkedList()  

    def dfs(username, visited):
        if username in visited:
            return
        visited.add(username)

        user = users_hash_table.get_val(username)
        if user is None:
            return

        region = user.region
        current_count = region_count.get_val(region)
        if current_count is None:
            region_count.insert(region, 1)
        else:
            region_count.update_val(region, current_count + 1)

        for following_username in user.following:
            dfs(following_username, visited)

    visited = MySet()
    for username in users_hash_table:
        dfs(username, visited)

    return region_count

def extract_hashtags(tweet_text):
    hashtags = re.findall(r'#\w+', tweet_text)
    return hashtags



class RegionHashtags:
    def __init__(self):
        self.hashtags = HashTable(50) 

    def add_hashtag(self, hashtag):
        current_count = self.hashtags.get_val(hashtag)
        if current_count is None:
            self.hashtags.insert(hashtag, 1)
        else:
            self.hashtags.insert(hashtag, current_count + 1)

    def get_hashtags(self):
        return self.hashtags
from heapq import nlargest

def dfs_all_users_by_regions(users_hash_table):
    region_count = DictionaryLinkedList()  

    def dfs(username, visited):
        if visited.contains(username): 
            return
        visited.add(username)

        user = users_hash_table.get_val(username)
        if user is None:
            return

        region = user.region
        current_count = region_count.get_val(region)
        if current_count is None:
            region_count.insert(region, 1)
        else:
            region_count.update_val(region, current_count + 1)

        for following_username in user.following:
            dfs(following_username, visited)

    visited = MySet()
    for username in users_hash_table:
        dfs(username, visited)

    return region_count


def process_regions_and_hashtags(users_hash_table):
    regions_hashtags = DictionaryLinkedList()

    users_linked_list = users_hash_table.get_all_values_as_linked_list()
    current_node = users_linked_list.head

    while current_node:
        user = current_node.value
        region = user.region
        tweet_node = user.tweets.head

        region_hashtags = regions_hashtags.find(region)
        if region_hashtags is None:
            region_hashtags = HashTable(50)
            regions_hashtags.insert(region, region_hashtags)

        while tweet_node:
            tweet_text = tweet_node.value
            hashtags_in_tweet = MySet() 
            for hashtag in extract_hashtags(tweet_text):
                hashtags_in_tweet.add(hashtag)
            for hashtag in hashtags_in_tweet:
                current_count = region_hashtags.get_val(hashtag)
                if current_count is None:
                    region_hashtags.set_val(hashtag, 1)
                else:
                    region_hashtags.set_val(hashtag, current_count + 1)
            tweet_node = tweet_node.next

        current_node = current_node.next

    # Dosyaya yaz
    with open('region_analysis.txt', 'w', encoding='utf-8') as file:
        for region, region_hashtags in regions_hashtags.items():
            file.write(f"Region: {region}\n")
            # Her bölge için en popüler 10 hashtag bul ve yazdır
            top_hashtags = nlargest(10, region_hashtags.items(), key=lambda item: item[1])
            for hashtag, count in top_hashtags:
                file.write(f"  {hashtag}: {count}\n")