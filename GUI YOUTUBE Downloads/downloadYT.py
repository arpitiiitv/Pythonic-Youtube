from tkinter import *

master = Tk()
master.geometry("700x500")
master.title("Download Youtube Video")
master.configure(bg='pink')


def download():
    try:
        import pafy
        video_link = data.get()
        video_link = video_link.strip()
        video = pafy.new(video_link)
        Label(master, text="Title : "+video.title, font='Consolas 15 bold', bg='pink').pack()
        Label(master, text="Duration : "+video.duration, font='Consolas 15 bold', bg='pink').pack()
        video = video.getbest(preftype="mp4")
        filename = video.download(quiet=False)
        Label(master, text="Downloading Completed",font='Consolas 15 bold',bg='pink').pack()
    except Exception as e:
        Label(master,text="\n\n", bg='pink').pack()
        Label(master, text="Please check you Internet\nOr enter correct URL",bg='red', font='Consolas 15 bold').pack()


Label(master, text="\n\n\n|| Download Youtube video in one click ||", bg='pink', font='Consolas 18 bold', width=50).pack()
Label(master, text="\n\n", bg='pink').pack()
data = StringVar()
Label(master, text="Enter Video link in input box\n", bg='pink', font='Consolas 15 bold').pack()
entry = Entry(master, textvariable=data, width=50).pack()
Label(master, text="\n",bg='pink').pack()
button = Button(master, text="DOWNLOAD NOW", width=15, height=2, bg='green',command=download).pack()
master.mainloop()

