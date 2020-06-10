#pip install pafy
#pip install youtube-dl
import pafy
filename=pafy.new(input("Enter url of YouTube video : ")).getbest(preftype="mp4").download(quiet=False)