import pytube  
from pytube import YouTube  
video_url = 'https://www.youtube.com/watch?v=t5trXhAmWWk&list=RDy6NSdGL8czw&index=3'
youtube = pytube.YouTube(video_url)  
video = youtube.streams.first()  
video.download('C:/Users/DELL/Desktop/')  
