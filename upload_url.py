import firebase_admin
from firebase_admin import credentials, firestore
import os

# Load credentials and initialize app
cred = credentials.Certificate('creds.json')
firebase_admin.initialize_app(cred)

# Connect to Firestore
db = firestore.client()

# Prepare the document
doc_ref = db.collection('reemo_sessions').document(os.environ['GITHUB_ID'])

# Set session data
doc_ref.set({
    'github_id': os.environ['GITHUB_ID'],
    'vm_name': os.environ['VM_NAME'],
    'session_id': os.environ['SESSION_ID'],
    'device_id': os.environ['DEVICE_ID']
})

print('Uploaded to Firebase successfully.')
