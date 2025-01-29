import os
import firebase_admin
from firebase_admin import credentials, firestore

# Get the absolute path of service-account.json
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SERVICE_ACCOUNT_PATH = os.path.join(BASE_DIR, "service-account.json")

# Initialize Firebase app
cred = credentials.Certificate(SERVICE_ACCOUNT_PATH)
firebase_admin.initialize_app(cred)

db = firestore.client()
