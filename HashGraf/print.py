import json
from data_structures import HashTable, MyLinkedList
from utils import create_users_from_json, create_graph_from_users
from interests_utils import get_top_words,insert_user_to_interests_hash_table,oneri_uret

def extract_interests_and_add_to_hashtable(users_hash_table, interests_hash_tables):
    users_linked_list = users_hash_table.get_all_values_as_linked_list()
    current_node = users_linked_list.head
    while current_node:
        user = current_node.value
        tweets_text = MyLinkedList()
        tweet_node = user.tweets.head
        while tweet_node:
            tweets_text.append(tweet_node.value)
            tweet_node = tweet_node.next

        top_words = get_top_words(tweets_text)
        for word, _ in top_words:
            insert_user_to_interests_hash_table(interests_hash_tables, word, user.username)

        current_node = current_node.next

def write_interests_to_file(interests_hash_tables, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for interest in interests_hash_tables:
            users_linked_list = interests_hash_tables[interest]
            file.write(f"İlgi Alanı: {interest}\n")
            if users_linked_list:
                for user_key_node in users_linked_list:
                    file.write(f"  Kullanıcı: {user_key_node}\n")

def write_recommendations_to_file(interests_hash_tables, users_hash_table, file_name):
    oneriler = oneri_uret(interests_hash_tables, users_hash_table)
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write("\nÖnerilen Kullanıcı Analizi:\n")
        for ilgi_alani in interests_hash_tables:
            interest_users_list = interests_hash_tables.get_val(ilgi_alani)
            if interest_users_list:
                file.write(f"\nİlgi Alanı Analizi: {ilgi_alani}\n")
                for user_key_node in interest_users_list:
                    user_key = user_key_node.key if hasattr(user_key_node, 'key') else user_key_node
                    user = users_hash_table.get_val(user_key)
                    if user:
                        user_following = [follower_node for follower_node in user.following]
                        file.write(f"Kullanıcı: {user_key}\n")
                        file.write("Önerilen kullanıcılar:\n")
                        ilgi_alani_onerileri = oneriler.find(ilgi_alani)
                        if ilgi_alani_onerileri:
                            for recommendation_node in ilgi_alani_onerileri:
                                recommendation_key = recommendation_node
                                if recommendation_key != user_key and recommendation_key not in user_following:
                                    file.write(f"    - {recommendation_key}\n\n")
