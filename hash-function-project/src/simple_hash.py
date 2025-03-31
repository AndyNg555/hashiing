def simple_hash(key: str) -> int:

    return sum(ord(char) for char in str(key)) % 10

def show_collisions(keys: list) -> dict:

    groups = {}
    for key in keys:
        h = simple_hash(key)
        if h not in groups:
            groups[h] = []
        groups[h].append(key)
    return groups

