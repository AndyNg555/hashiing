import pytest
from src.simple_hash import simple_hash, demonstrate_collisions

def test_simple_hash_with_strings():
    assert simple_hash('test') == 4
    assert simple_hash('apple') == 0
    assert simple_hash('banana') == 1

def test_simple_hash_with_numbers():
    assert simple_hash(123) == 6
    assert simple_hash(45.67) == 4

def test_collision_demonstration():
    keys = ['apple', 'banana', 'orange', 'grape']
    result = demonstrate_collisions(keys)
    assert isinstance(result, dict)
    for hash_val, key_list in result.items():
        assert 0 <= hash_val <= 9
        assert len(key_list) >= 1