import matplotlib.pyplot as plt
import networkx as nx

def visualize_hash_table(hash_table):
    table_size = hash_table.size
    fig, ax = plt.subplots(figsize=(10, 5))

    hash_table_data = [['' for _ in range(table_size)] for _ in range(table_size)]

    for i, linked_list in enumerate(hash_table.hash_table):
        current_node = linked_list.head
        while current_node:
            key = hash_table.simple_hash(current_node.key)
            hash_table_data[i][key] = current_node.key
            current_node = current_node.next

    ax.imshow([[1 if value else 0 for value in row] for row in hash_table_data], cmap="cool", aspect="auto")

    for i in range(table_size):
        for j in range(table_size):
            text = hash_table_data[j][i]
            ax.text(i, j, text, ha='center', va='center')

    ax.set_xticks(range(table_size))
    ax.set_yticks(range(table_size))
    ax.set_xticklabels(range(table_size))
    ax.set_yticklabels(range(table_size))
    ax.set_xlabel('Hashed Key')
    ax.set_ylabel('LinkedList Index')
    ax.set_title('Hash Table Visualization')

    plt.show()

def visualize_graph_with_networkx(graph):
    G = nx.DiGraph()
    
    for username in graph.nodes:  # Kullanıcı adlarının listesini al
        user_node = graph.get_node(username)
        G.add_node(username)  # Her kullanıcı için bir düğüm ekle

        # Kullanıcının takip ettikleri için kenarlar ekle
        following_node = user_node.following.head
        while following_node:
            G.add_edge(username, following_node.key)  # Kullanıcıdan takip edilene kenar
            following_node = following_node.next

        # Kullanıcının takipçileri için kenarlar ekle
        follower_node = user_node.followers.head
        while follower_node:
            G.add_edge(follower_node.key, username)  # Takipçiden kullanıcıya kenar
            follower_node = follower_node.next

    # Grafiği çiz
    plt.figure(figsize=(100, 100))
    nx.draw(G, with_labels=True, node_color='pink', edge_color='gray', node_size=2000, font_size=10)
    plt.show()
    
def visualize_user_graph_with_networkx(graph, username):
    G = nx.DiGraph()

    if graph.has_node(username):
        user_node = graph.get_node(username)
        G.add_node(username) 

        following_node = user_node.following.head
        while following_node:
            G.add_node(following_node.key)
            G.add_edge(username, following_node.key)  
            following_node = following_node.next

        
        follower_node = user_node.followers.head
        while follower_node:
            G.add_node(follower_node.key)
            G.add_edge(follower_node.key, username)  
            follower_node = follower_node.next

       
        plt.figure(figsize=(10, 10))  
        nx.draw(G, with_labels=True, node_color='purple', edge_color='purple', node_size=500, font_size=12)
        plt.show()
    else:
        print(f"Graph does not contain user: {username}")