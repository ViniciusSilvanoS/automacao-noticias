import hashlib


def fazer_hash(valor):
    hash = hashlib.sha256(valor.encode()).hexdigest()
    return hash