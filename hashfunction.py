import hashlib

password = "mypassword"
hashed = hashlib.sha256(password.encode()).hexdigest()
print(f"SHA-256 Hash: {hashed}")
