import hashlib
import itertools
import string

target_hash = hashlib.sha256("abc".encode()).hexdigest()

for combo in itertools.product(string.ascii_lowercase, repeat=3):
    attempt = ''.join(combo)
    if hashlib.sha256(attempt.encode()).hexdigest() == target_hash:
        print(f"Password cracked: {attempt}")
        break
