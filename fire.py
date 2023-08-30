import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('serviceAccountKey.json')

firebase_admin.initialize_app(cred)

db = firestore.client()

# Add a document to the "rides" collection
rides_ref = db.collection('rides')
new_ride_ref = rides_ref.add({
    'name': 'ride400'
})

print("Updated to Firebase")
