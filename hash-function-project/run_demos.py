from src.simple_hash import simple_hash, show_collisions
from src.hash_table import HashTable
from src.salted_hash import salted_hash

# Demo 1: Simple Hashing
print("=== Simple Hashing ===")
fruits = ["apple", "banana", "cherry", "date"]
print(f"Hash for 'apple': {simple_hash('apple')}")
print("Collisions:", show_collisions(fruits))

# Demo 2: Hash Table
print("\n=== Hash Table ===")
ht = HashTable()
ht.insert("apple", 5)
ht.insert("banana", 6)
print(f"apple → {ht.search('apple')}")
print(f"banana → {ht.search('banana')}")

# Demo 3: Salted Hashing
print("\n=== Salted Hashing ===")
hash_val, salt = salted_hash("secret123")
print(f"Hash: {hash_val}\nSalt: {salt}")