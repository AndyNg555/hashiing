import hashlib
import os
from typing import Tuple

def generate_salt(length: int = 16) -> bytes:
    return os.urandom(length)

def salted_hash(key: str, salt: bytes = None) -> Tuple[str, str]:
    key_str = str(key)
    
    if salt is None:
        salt = generate_salt()
    
    salt_hex = salt.hex()
    salted_input = (key_str + salt_hex).encode('utf-8')
    
    hash_hex = hashlib.sha256(salted_input).hexdigest()[:8]
    
    return (hash_hex, salt_hex)

def verify_hash(key: str, hash_value: str, salt_hex: str) -> bool:
    salt = bytes.fromhex(salt_hex)
    new_hash, _ = salted_hash(key, salt)
    return new_hash == hash_value