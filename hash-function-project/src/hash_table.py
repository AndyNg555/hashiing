class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, size: int = 10):
        self.size = size
        self.table = [None] * size
    
    def _get_hash(self, key) -> int:
        return sum(ord(char) for char in str(key)) % self.size
    
    def insert(self, key, value) -> None:
        hash_value = self._get_hash(key)
        node = self.table[hash_value]
        
        if node is None:
            self.table[hash_value] = Node(key, value)
        else:
            while node.next is not None:
                if node.key == key:
                    node.value = value
                    return
                node = node.next
            node.next = Node(key, value)
    
    def search(self, key):
        hash_value = self._get_hash(key)
        node = self.table[hash_value]
        
        while node is not None:
            if node.key == key:
                return node.value
            node = node.next
        return None
    
    def delete(self, key) -> bool:
        hash_value = self._get_hash(key)
        node = self.table[hash_value]
        prev = None
        
        while node is not None:
            if node.key == key:
                if prev is None:
                    self.table[hash_value] = node.next
                else:
                    prev.next = node.next
                return True
            prev = node
            node = node.next
        return False
    
    def display(self) -> None:
        for i in range(self.size):
            node = self.table[i]
            print(f"Bucket {i}:", end=" ")
            while node is not None:
                print(f"({node.key}:{node.value})", end=" -> ")
                node = node.next
            print("None")