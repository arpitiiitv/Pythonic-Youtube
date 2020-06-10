#pip install pafy
#pip install youtube-dl
import pafy
#url=""
url=input("Enter URL of Youtube video : ")
audio=pafy.new(url).audiostreams
print(audio)
#best quality at last audio[-1]
filename=audio[-1].download(quiet=False)
