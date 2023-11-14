from pytube import YouTube
from tqdm import tqdm
import time
global size
choice = int(input('Video or Audio ?\n1. Video\n2. Audio\nEnter the choice : '))
url = input('Enter the link : ')
video = YouTube(url)
if choice == 1:
    x = video.streams.get_highest_resolution()
    size = x.filesize
    x.download()
elif choice == 2:
    x = video.streams.get_audio_only()
    size = x.filesize
    x.download()
else:
    exit("Wrong Choice !")
for i in tqdm(range(size//10000)):
    time.sleep(0.000001)
