import moviepy.editor as mp
from firebase_admin import credentials, initialize_app, storage
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

def firebase_init():
    cred = credentials.Certificate(r'firebase.json')
    initialize_app(cred, {
        "storageBucket": os.getenv('BUCKET_NAME')
    })

firebase_init()

class VideoToAudio:
    def __init__(self, url):
        self.video_url =  url

    def convert(self):
        b = mp.VideoFileClip(self.video_url)
        m = b.audio.write_audiofile(r'demo.mp3')

        return self.upload_to_firebase()

    def upload_to_firebase(self):
        fileName = r'demo.mp3'
        bucket = storage.bucket()
        
        macrosec = datetime.now().isoformat()
        destination_blob_name = f'aud{macrosec}.mp3'
        blob = bucket.blob(destination_blob_name)
        
        blob.upload_from_filename(fileName)
        
        blob.make_public()

        return {"url" : blob.public_url}
