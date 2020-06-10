#pip install pafy
#pip install youtube-dl
import pafy
#pip install pafy
#pip install youtube-dl
import pafy
url=input("Enter URL of YouTube video : ")
video=pafy.new(url)
print(video.title)
print(video.duration)
best=video.getbest(preftype='mp4')
filename=best.download(quiet=False)