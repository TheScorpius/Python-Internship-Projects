import hashlib
import os

USER_FILE = "users.txt"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def user_exists(username):
    if not os.path.exists(USER_FILE):
        return False

    with open(USER_FILE, "r") as file:
        for line in file:
            stored_user, _ = line.strip().split(",")
            if stored_user == username:
                return True
    return False

def register_user(username, password):
    if user_exists(username):
        raise ValueError("User already exists")

    with open(USER_FILE, "a") as file:
        file.write(f"{username},{hash_password(password)}\n")

def login_user(username, password):
    if not os.path.exists(USER_FILE):
        raise FileNotFoundError("No users registered yet")

    hashed = hash_password(password)

    with open(USER_FILE, "r") as file:
        for line in file:
            stored_user, stored_pass = line.strip().split(",")
            if stored_user == username and stored_pass == hashed:
                return True
    return False
