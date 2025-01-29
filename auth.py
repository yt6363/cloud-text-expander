import firebase_admin.auth as auth
import os

def get_user_id():
    # Check if we already have a stored UID
    if os.path.exists("user_id.txt"):
        with open("user_id.txt", "r") as f:
            uid = f.read().strip()
            return uid

    # Otherwise, create a new anonymous user
    user = auth.create_user()
    with open("user_id.txt", "w") as f:
        f.write(user.uid)
    return user.uid
