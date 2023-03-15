import tkinter as tk
import pytube
import os
from pathlib import Path
from PIL import ImageTk, Image

root = tk.Tk()

root.title("YouTube Downloader")
root.geometry("450x250")#standard size
root.minsize(width=450,height=250)#minimal size
root.maxsize(width=450,height=250)#max size

URL_label = tk.Label(root,text="URL: ")
URL_label.place(x=20,y=10)#bei 20x10y platziert

def To_MP3():
    try:
        destination = str(Path.home() / "Downloads")
        URL = pytube.YouTube(input_url.get())
        input_url.delete(0,4096)
        input_url.insert(0,"Downloading...")  
        video = URL.streams.filter(only_audio=True).first()
        out_file = video.download(output_path=destination)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        input_url.delete(0,4096)
        input_url.insert(0,"Done!")   
    except:
        input_url.delete(0,4096)
        input_url.insert(0,"Not a valid URL")


def To_MP4():
    try:
        downloads_path = str(Path.home() / "Downloads")
        URL = input_url.get()
        YT = pytube.YouTube(URL)
        input_url.delete(0,4096)
        input_url.insert(0,"Downloading...")        
        vid = YT.streams.get_highest_resolution()
        vid.download(downloads_path)
        input_url.delete(0,4096)
        input_url.insert(0,"Done!")
    except:
        input_url.delete(0,4096)
        input_url.insert(0,"Not a valid URL")
    
mp3_button = tk.Button(root, text="Convert to MP3", command = To_MP3)
mp3_button.place(x=54,y=40)

mp4_button = tk.Button(root, text="Convert to MP4", command = To_MP4)
mp4_button.place(x=150,y=40)

input_url = tk.Entry(root, width = 50, bg="lightgray")
input_url.place(x=55, y=12)
input_url.focus()

img = ImageTk.PhotoImage(Image.open(os.path.join("assets","Image.png")))
panel = tk.Label(root, image = img)
panel.place(x=20,y=100)

mp3_img = ImageTk.PhotoImage(Image.open(os.path.join("assets","mp4.png")))
mp4_img = ImageTk.PhotoImage(Image.open(os.path.join("assets","mp3.png")))
img_3 = tk.Label(root, image = mp3_img)
img_4 = tk.Label(root, image = mp4_img)
img_3.place(x=250,y=108)
img_4.place(x=340,y=108)

def on_enter(e):
    mp4_button['background'] = "#a595f5"
def on_leave(e):
    mp4_button['background'] = 'SystemButtonFace'
mp4_button.bind("<Enter>", on_enter)
mp4_button.bind("<Leave>", on_leave)

def on_enter_(e):
    mp3_button['background'] = "#a595f5"
def on_leave_(e):
    mp3_button['background'] = 'SystemButtonFace'
mp3_button.bind("<Enter>", on_enter_)
mp3_button.bind("<Leave>", on_leave_)

text = tk.Label(root, text = "The file will be exported to the download folder")
text.place(x=52,y=70)

ico = Image.open(os.path.join("assets",'icon.png'))
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

root.mainloop()
