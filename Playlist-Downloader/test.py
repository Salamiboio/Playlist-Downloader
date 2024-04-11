from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=mbndauRI0TE")

link = ("C:\\Users\\Tyler\\Music\\Salami's Bops and Tunes")
stream = yt.streams.get_by_resolution(720)
stream.download(link)            
