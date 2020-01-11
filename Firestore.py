import time

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


class Firestore:

	def __init__(self):
		cred = credentials.Certificate('./config/smarthome-b5b8f-firebase-adminsdk-dqn8a-5a2ecbf0d2.json')
		firebase_admin.initialize_app(cred)
		self.db = firestore.client()

	def on_snapshot(self, doc_snapshot, changes, read_time):
		for doc in doc_snapshot:
			print(u'Received document snapshot: {}'.format(doc.id))


if __name__ == '__main__':
	firestore = Firestore()
	doc_ref = firestore.db.collection(u'automata').document(u'drive')
	doc_watch = doc_ref.on_snapshot(firestore.on_snapshot)

	# Keep the app running
	while True:
		time.sleep(1)
		print('processing...')
