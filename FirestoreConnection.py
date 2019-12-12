import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from datetime import date

# Use the application default credentials
cred = credentials.Certificate("c-clickr-bde73-firebase-adminsdk-mjknx-52424a2b8c.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def sign_in(uin):
	today = date.today().strftime('%m-%d')
	print(today)
	date_ref = db.collection(u'Dates').document(today)
	date_ref.update({uin: True})

sign_in("987654321")
print("Done")