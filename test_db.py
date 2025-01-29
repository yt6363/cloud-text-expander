# test_db.py
from auth import get_user_id
from db import add_snippet, get_snippets

user_id = get_user_id()
snippets = get_snippets(user_id)

# Add some snippets
add_snippet(user_id, "@@email", "youremail@example.com")
add_snippet(user_id, "@@name", "John Doe")

# Retrieve all snippets
snippets = get_snippets(user_id)
print("🔥 Current snippets in Firestore:", snippets)
