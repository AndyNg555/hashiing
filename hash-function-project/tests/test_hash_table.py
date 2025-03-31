import pytest
from src.hash_table import HashTable

@pytest.fixture
def sample_hash_table():
    ht = HashTable()
    ht.insert('apple', 5)
    ht.insert('banana', 6)
    ht.insert('orange', 6)
    return ht

def test_hash_table_insert_search(sample_hash_table):
    assert sample_hash_table.search('apple') == 5
    assert sample_hash_table.search('banana') == 6
    assert sample_hash_table.search('orange') == 6
    assert sample_hash_table.search('grape') is None

def test_hash_table_collision_handling(sample_hash_table):
    assert sample_hash_table.search('banana') == 6
    assert sample_hash_table.search('orange') == 6

def test_hash_table_delete(sample_hash_table):
    assert sample_hash_table.delete('apple') is True
    assert sample_hash_table.search('apple') is None
    assert sample_hash_table.delete('grape') is False