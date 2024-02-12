class Node:
    def __init__(self, data):
        self.key, self.value = data
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node((None, value))  
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, key, value):
        new_node = Node((key, value))
        new_node.next = self.head
        self.head = new_node

    def find(self, key):
        cur_node = self.head
        while cur_node:
            if cur_node.key == key:
                return cur_node.value
            cur_node = cur_node.next
        return None

    def delete(self, key):
        cur_node = self.head
        prev_node = None
        while cur_node:
            if cur_node.key == key:
                if prev_node:
                    prev_node.next = cur_node.next
                else:
                    self.head = cur_node.next
                return
            prev_node = cur_node
            cur_node = cur_node.next

    def __str__(self):
        output = ""
        cur_node = self.head
        while cur_node:
            node_representation = str((cur_node.key, cur_node.value))
            output += node_representation
            if cur_node.next:  
                output += " -> "
            cur_node = cur_node.next
        return output
    
    def __iter__(self):
        self.current = self.head  
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        current_key = self.current.key
        self.current = self.current.next
        return current_key
    
class KeyValuePair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class DictionaryLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, key, value):
        new_node = KeyValuePair(key, value)
        new_node.next = self.head
        self.head = new_node

    def find(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def __str__(self):
        output = ""
        current = self.head
        while current:
            output += f"{current.key}: {current.value}\n"
            current = current.next
        return output
    
    def keys(self):
        current = self.head
        keys = LinkedList()
        while current:
            keys.insert(current.key, None)  
            current = current.next
        return keys

    def values(self):
        current = self.head
        values = LinkedList()
        while current:
            values.insert(None, current.value)  
            current = current.next
        return values
    
    def items(self):
        current = self.head
        while current:
            yield current.key, current.value
            current = current.next

    def __iter__(self):
        current = self.head
        while current:
            yield current.key
            current = current.next

class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = [LinkedList() for _ in range(self.size)]

    def simple_hash(self, key):
        hash_value = 0
        for char in key:
            hash_value = (hash_value * 31 + ord(char)) % self.size
        return hash_value
 
    def set_val(self, key, val):
        hashed_key = self.simple_hash(key)
        self.hash_table[hashed_key].insert(key, val)
 
    def get_val(self, key):
        hashed_key = self.simple_hash(key)
        return self.hash_table[hashed_key].find(key)

    def delete_val(self, key):
        hashed_key = self.simple_hash(key)
        self.hash_table[hashed_key].delete(key)

    def get_all_values_as_linked_list(self):
            all_values_linked_list = LinkedList()
            for linked_list in self.hash_table:
                current_node = linked_list.head
                while current_node:
                    all_values_linked_list.insert(current_node.key, current_node.value)
                    current_node = current_node.next
            return all_values_linked_list

    def __iter__(self):
        for linked_list in self.hash_table:
            current_node = linked_list.head
            while current_node:
                yield current_node.key
                current_node = current_node.next
    
    def insert(self, key, value):
        
        index = self.hash_function(key)
                
    def __getitem__(self, key):
        hashed_key = self.simple_hash(key)
        return self.hash_table[hashed_key].find(key)
    
    def __setitem__(self, key, value):
        self.set_val(key, value)

    def items(self):
        for linked_list in self.hash_table:
            current_node = linked_list.head
            while current_node:
                yield current_node.key, current_node.value
                current_node = current_node.next
    
    def _str_(self):
        return "\n".join(str(item) for item in self.hash_table)
    
class UserNode:
    def __init__(self, username):
        self.username = username
        self.followers = LinkedList()
        self.following = LinkedList()

    def add_follower(self, follower_username):
        if not self.followers.find(follower_username):
            self.followers.insert(follower_username, None)  

    def add_following(self, following_username):
        if not self.following.find(following_username):
            self.following.insert(following_username, None) 

class Graph:
    def __init__(self):
        self.nodes = DictionaryLinkedList()

    def add_node(self, username):
        if not self.nodes.find(username):
            self.nodes.insert(username, UserNode(username))

    def get_node(self, username):
        return self.nodes.find(username)

    def add_edge(self, from_username, to_username):
        from_node = self.get_node(from_username)
        to_node = self.get_node(to_username)
        if from_node and to_node:
           
            from_node.add_following(to_username)
           
            to_node.add_follower(from_username)


    def has_node(self, node):
        return node in self.nodes

    def __str__(self):
        return str(self.nodes)
    

class SetNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class MySet:
    def __init__(self):
        self.head = None

    def add(self, element):
        if not self.contains(element):
            new_node = SetNode(element)
            new_node.next = self.head
            self.head = new_node

    def contains(self, element):
        current = self.head
        while current:
            if current.value == element:
                return True
            current = current.next
        return False

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next
