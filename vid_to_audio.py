"""import moviepy.editor

# Replace the parameter with the location of the video
video = moviepy.editor.VideoFileClip("C:\\Users\\DELL\\Desktop\\python_project\\vid1.mp4")

audio = video.audio

# Replace the parameter with the location along with filename
audio.write_audiofile("C:\\Users\\DELL\\Desktop\\python_project\\sample1.mp3")  """

import speech_recognition as sr
from os import path
from pydub import AudioSegment

# convert mp3 file to wav                                                       
sound = AudioSegment.from_mp3("sample1.mp3")
sound.export("transcript.wav", format="wav")


# transcribe audio file                                                         
AUDIO_FILE = "transcript.wav"

# use the audio file as the audio source                                        
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file                  

        print("Transcription: " + r.recognize_google(audio))