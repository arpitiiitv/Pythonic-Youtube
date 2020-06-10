#pip install pafy
#pip install youtube-dl
import pafy
#url="https://www.youtube.com/watch?v=fbZpz9KbiAY&list=PLl6h6UvLNv39Ao62pIbiylPbIw-6lT77x"
url=input("Enter URL of youtube playlist : ")
playlist=pafy.get_playlist(url)
number_of_videos=len(playlist['items'])
print(number_of_videos)
print(playlist.keys())
for i in range(number_of_videos):
    best=playlist['items'][i]['pafy'].getbest(preftype='mp4')
    filename=best.download(quiet=False)