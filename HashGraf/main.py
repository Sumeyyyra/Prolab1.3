import json
from collections import Counter
import re
from utils import create_users_from_json, create_graph_from_users
from visualizations import visualize_hash_table, visualize_user_graph_with_networkx,visualize_graph_with_networkx
from data_structures import HashTable,MyLinkedList,LinkedList,DictionaryLinkedList,MySet
from interests_utils import get_top_words,insert_user_to_interests_hash_table,oneri_uret
from print import extract_interests_and_add_to_hashtable,write_interests_to_file,write_recommendations_to_file
from dfs import extract_hashtags,dfs_all_users_by_regions,process_regions_and_hashtags

def main():
    # JSON dosyasını aç ve oku
    with open('deneme2.json', 'r', encoding='utf-8') as file:



        json_data = json.load(file)

    # Kullanıcılar için HashTable oluştur
    users_hash_table = HashTable(10)

    # İlgi alanları için HashTable'lar saklayacak bir HashTable oluştur
    interests_hash_tables = HashTable(50)

    # JSON verilerini kullanarak kullanıcıları oluştur
    create_users_from_json(json_data, users_hash_table)
    print("Users hash table created")
    
    ##########################################
    # # Kullanıcıların tweet'lerinden ilgi alanlarını çıkar ve ilgili HashTable'a ekle
    extract_interests_and_add_to_hashtable(users_hash_table, interests_hash_tables)
    # # İlgi alanlarına göre HashTable'ları ve kullanıcıları dosyaya yaz
    write_interests_to_file(interests_hash_tables, 'interests_utils.txt')
    # # Önerileri dosyaya yaz
    write_recommendations_to_file(interests_hash_tables, users_hash_table, 'analysis.txt')

    ##########################################
    # Hash tablosunu ve grafiği görselleştir
    visualize_hash_table(users_hash_table)
    graph = create_graph_from_users(users_hash_table)
    print("Graph created")
    visualize_user_graph_with_networkx(graph,'stephencain')
    #visualize_graph_with_networkx(graph)

    
    ###########################################
    # Kullanıcıların bölgesel olarak tweet'lerinden ilgi alanlarını çıkar ve ilgili HashTable'a ekle
    #process_regions_and_hashtags(users_hash_table)

if __name__ == "__main__":
    main()

