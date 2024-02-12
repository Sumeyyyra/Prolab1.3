from user_model import User
from data_structures import HashTable, Graph

import json
def create_users_from_json(json_data, users_hash_table):
    # İlk olarak, tüm kullanıcıları oluştur ve HashTable'a ekle
    for user_data in json_data:
        user = User(
            username=user_data['username'],
            full_name=user_data['name'],
            followers_count=user_data['followers_count'],
            following_count=user_data['following_count'],
            language=user_data['language'],
            region=user_data['region']
        )
        # Tweetleri ekle
        for tweet in user_data['tweets']:
            user.add_tweet(tweet)
        # Takip edilen kullanıcıları ekle
        for following_username in user_data.get('following', []):
            user.add_following(following_username)
        # Takipçi kullanıcıları ekle
        for follower_username in user_data.get('followers', []):
            user.add_follower(follower_username)
        
        users_hash_table.set_val(user.username, user)

    return users_hash_table

def create_graph_from_users(users_hash_table):
    graph = Graph()
    for i in range(users_hash_table.size):
        current_list = users_hash_table.hash_table[i]
        current_node = current_list.head
        while current_node:
            user = current_node.value

            # Kullanıcı düğümünü ekle
            if not graph.has_node(user.username):
                graph.add_node(user.username)
            
            # Kullanıcının takip ettiği kişiler için kenarlar ekle
            following_node = user.following.head
            while following_node:
                if not graph.has_node(following_node.key):
                    graph.add_node(following_node.key)
                graph.add_edge(user.username, following_node.key)
                following_node = following_node.next

            # Kullanıcının takipçileri için kenarlar ekle
            follower_node = user.followers.head
            while follower_node:
                if not graph.has_node(follower_node.key):
                    graph.add_node(follower_node.key)
                graph.add_edge(follower_node.key, user.username)
                follower_node = follower_node.next

            current_node = current_node.next
    return graph