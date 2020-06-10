#pip install pafy
#pip install youtube-dl
import pafy
#url="https://www.youtube.com/watch?v=SA4m_rcSwqs&list=RDSA4m_rcSwqs"
url=input("Enter URL of Youtube video : ")
audio=pafy.new(url).videostreams
print(audio)
#best quality at last audio[-1]
filename=audio[-1].download(quiet=False)
