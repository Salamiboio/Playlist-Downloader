from pytube import Playlist
from pytube import YouTube
from tqdm import tqdm

def type_selector():
    while True: 
        type_download = input("Are you downloading a Playlist or a Link? ").lower()
        if type_download == "playlist":
            return 1
            break
        elif type_download == "link":
                return 2 
                break
        else:
             print("Invalid Input please try again.")
             type_selector()
             
def file_type_selector():
    while True: 
        file_type = input("What would you like the output to be Video or Audio? ").lower()
        if file_type == "video":
            return 1 
            break
        elif file_type == "audio":
                return 2
                break
        else:
             print("Invalid Input please try again.")
             type_selector()
 
def audio_quality():
    while True: 
        file_type = input("What would you audio quality to be in Kbps? 48 or 128?  ").lower()
        if file_type == "48":
            return 139 
            break
        elif file_type == "128":
                return 140
                break
        else:
             print("Invalid Input please try again.")
             audio_quality()
             
def video_quality():
    while True: 
        file_type = input("What would you video quality to be? 720P, 1080P, 1440P?  ").lower()
        if file_type == "720p":
            return 720 
            break
        elif file_type == "1080p":
                return 1080
                break
        elif file_type == "1440p":
                return 1440
                break
        else:
             print("Invalid Input please try again.")
             video_quality()
 
def playlist_downloader(link, destination, itag):
    p = Playlist(link)
    if file_type_selected == 1:
        with tqdm(total=len(p.videos), desc = "Downloading Files", unit = "Mbps", colour = "GREEN") as pbar:
            for video in p.videos:
                 video.streams.get_by_resolution(itag).download(destination)
                 pbar.update(1)
    if file_type_selected == 2:
        with tqdm(total=len(p.videos), desc = "Downloading Files", unit = "Mbps", colour = "GREEN") as pbar:
            for video in p.videos:
                 video.streams.get_by_itag(itag).download(destination)
                 pbar.update(1)
                 
def individual_downloader(link, destination, itag):
    yt = YouTube(link)
    if file_type_selected == 1:
        with tqdm(total=1, desc = "Downloading File", unit = "Mbps", colour = "GREEN") as pbar:
             stream = yt.streams.get_by_resolution(itag)
             stream.download(destination) 
             pbar.update(1)
    if file_type_selected == 2:
        with tqdm(total=1, desc = "Downloading File", unit = "Mbps", colour = "GREEN") as pbar:
             stream = yt.streams.get_by_itag(itag)
             stream.download(destination)    
             pbar.update(1)
             
def youtube_download():
    if type_selected == 1:
         if file_type_selected == 1:
              itag = video_quality()
              playlist_downloader(link, destination, itag)
         else:
              itag = audio_quality()
              playlist_downloader(link, destination, itag)
    else:
         if file_type_selected == 1:
              itag = video_quality()
              individual_downloader(link, destination, itag)
         else:
              itag = audio_quality()
              individual_downloader(link, destination, itag)
    print("Download Complete!")
          
type_selected = type_selector()
file_type_selected = file_type_selector()
link = input("Input your YouTube link: ")
destination = input("Input your file(s) destination: ")

if __name__ == "__main__":
    youtube_download() 