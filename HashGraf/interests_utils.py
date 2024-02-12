from collections import Counter
import re
from data_structures import HashTable,DictionaryLinkedList,LinkedList


def get_top_words(linked_list, num_top_words=3):
    word_count = Counter()
    current_node = linked_list.head
    while current_node:
        words = re.findall(r'\w+', current_node.value.lower())
        word_count.update(words)
        current_node = current_node.next
    return word_count.most_common(num_top_words)

def insert_user_to_interests_hash_table(interests_hash_table, interest, username):
    if interest not in interests_hash_table:
        interests_hash_table[interest] = HashTable(10)
    interest_hash_table = interests_hash_table[interest]

    if not interest_hash_table.get_val(username):
        interest_hash_table.set_val(username, None)

def oneri_uret(ilgi_alani_hash_tables, users_hash_table):
    oneriler = DictionaryLinkedList()

    for ilgi_alani, hash_table in ilgi_alani_hash_tables.items():
        ilgi_alani_onerileri = LinkedList()

        for user_key in hash_table:
            user = users_hash_table.get_val(user_key)
            user_following = user.following  
            user_followers = user.followers  

            # Diğer kullanıcılarla karşılaştır
            for other_user_key in hash_table:
                if user_key != other_user_key:
                    other_user = users_hash_table.get_val(other_user_key)
                    other_user_following = other_user.following
                    other_user_followers = other_user.followers

                    # Öneri koşulları
                    if other_user_key not in user_following:
                        ortak_takipciler = set(user_followers).intersection(set(other_user_followers))
                        if ortak_takipciler:
                            ilgi_alani_onerileri.insert(other_user_key, None)
                        else:
                            ilgi_alani_onerileri.insert(other_user_key, None)

        oneriler.insert(ilgi_alani, ilgi_alani_onerileri)

    return oneriler

    
