import moviepy.editor as mp
import random

class VideoToAudio:
    def __init__(self, url):
        self.video_url =  url

    def convert(self):
        b = mp.VideoFileClip(self.video_url)
        fileName = f"audio{random.randrange(0,4548)}.mp3"
        
        b.audio.write_audiofile(repr(fileName)[1:-1])

        return fileName