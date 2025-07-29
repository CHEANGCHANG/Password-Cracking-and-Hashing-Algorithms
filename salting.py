import os
import hashlib

salt = os.urandom(16)
password = "mypassword"
hashed = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
print(f"Salt: {salt.hex()}")
print(f"Hashed with Salt: {hashed.hex()}")