import pytest
from src.salted_hash import salted_hash, verify_hash, generate_salt

def test_salted_hash_consistency():
    key = "password123"
    salt = generate_salt()
    hash1, salt1 = salted_hash(key, salt)
    hash2, salt2 = salted_hash(key, salt)
    assert hash1 == hash2
    assert salt1 == salt2

def test_salted_hash_uniqueness():
    key = "password123"
    hash1, salt1 = salted_hash(key)
    hash2, salt2 = salted_hash(key)
    assert hash1 != hash2  
    assert salt1 != salt2

def test_verify_hash():
    key = "securepassword"
    hash_val, salt = salted_hash(key)
    assert verify_hash(key, hash_val, salt) is True
    assert verify_hash("wrongpassword", hash_val, salt) is False