# db.py
from firebase_config import db
from firebase_admin import firestore

def add_snippet(user_id, shortcut, expansion):
    """Adds or updates a snippet field in the Firestore document for user_id."""
    doc_ref = db.collection("snippets").document(user_id)
    doc_ref.set({shortcut: expansion}, merge=True)
    print(f"✅ Snippet '{shortcut}' added/updated successfully!")

def get_snippets(user_id):
    """Fetches all snippets for the given user_id from Firestore."""
    doc = db.collection("snippets").document(user_id).get()
    if doc.exists:
        return doc.to_dict()  # Returns a dictionary of shortcut -> expansion
    return {}

def delete_snippet(user_id, shortcut):
    doc_ref = db.collection("snippets").document(user_id)
    doc_ref.update({shortcut: firestore.DELETE_FIELD})
    print(f"❌ Deleted snippet '{shortcut}'!")


