import os
import threading
import time
import tkinter.messagebox
from tkinter import *
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
from ttkthemes import themed_tk as tk

from mutagen.mp3 import MP3
from pygame import mixer

root = tk.ThemedTk()
root.get_themes()                 # Returns a list of all themes that can be set
root.set_theme("radiance")         # Sets an available theme
mixer.init() 
# Fonts - Arial (corresponds to Helvetica), Courier New (Courier), Comic Sans MS, Fixedsys,
# MS Sans Serif, MS Serif, Symbol, System, Times New Roman (Times), and Verdana
#
# Styles - normal, bold, roman, italic, underline, and overstrike.

statusbar = ttk.Label(root, text="Welcome to Canzone", relief=SUNKEN, anchor=W, font='Times 10 italic')
statusbar.pack(side=BOTTOM, fill=X)

# Create the menubar
menubar = Menu(root)
root.config(menu=menubar)

# Create the submenu

subMenu = Menu(menubar, tearoff=0)
subMenu2 = Menu(menubar, tearoff=0)
subMenu3 = Menu(menubar, tearoff=0)
subMenu4 = Menu(menubar, tearoff=0)
subMenu5 = Menu(menubar, tearoff=0)

playlist = []


# playlist - contains the full path + filename
# playlistbox - contains just the filename
# Fullpath + filename is required to play the music inside play_music load function

def browse_file():
    global filename_path
    filename_path = filedialog.askopenfilename()
    add_to_playlist(filename_path)

    mixer.music.queue(filename_path)


def add_to_playlist(filename):
    filename = os.path.basename(filename)
    index = 0
    playlistbox.insert(index, filename)
    playlist.insert(index, filename_path)
    index += 1


menubar.add_cascade(label="File", menu=subMenu)


menubar.add_cascade(label="Edit", menu=subMenu2)
menubar.add_cascade(label="View", menu=subMenu3)
menubar.add_cascade(label="Settings", menu=subMenu4)

#File
subMenu.add_command(label="New", command=browse_file)
subMenu.add_command(label="Open", command=browse_file)
subMenu.add_command(label="Media", command=browse_file)
subMenu.add_command(label="Stream", command=browse_file)
subMenu.add_command(label="Downloads", command=browse_file)
subMenu.add_command(label="Search", command=browse_file)
subMenu.add_command(label="Search", command=browse_file)
subMenu.add_command(label="Exit", command=root.destroy)

#Edit
subMenu2.add_command(label="Undo")
subMenu2.add_command(label="Redo")
subMenu2.add_command(label="Playlist")
subMenu2.add_command(label="Find")
subMenu2.add_command(label="Rename")
subMenu2.add_command(label="Bookmark")
#View
subMenu3.add_command(label="Apperance")
subMenu3.add_command(label="Display")
subMenu3.add_command(label="Night Theme")
subMenu3.add_command(label="Extensions")
#Settings
subMenu4.add_command(label="Report a issue")
subMenu4.add_command(label="Change font")
subMenu4.add_command(label="Full Screen")



subMenu2.add_command(label="Open", command=browse_file)

leftframe = Frame(root)
leftframe.pack(side=LEFT, padx=5, pady=7)

playlistbox = Listbox(leftframe)
playlistbox.pack()

s = ttk.Style()
s.configure('W.TButton', font =
               ('calibri', 15, 'bold',), 
                foreground = 'brown',background="pink",padding=0,relief="flat") 
                
s.map("C.TButton",
    foreground=[('pressed', 'red'), ('active', 'blue')],
    background=[('pressed', '!disabled', 'black'), ('active', 'white')]
    )
addBtn = ttk.Button(leftframe, text="+ Add",style = 'C.TButton', command=browse_file)
# addBtn2 = ttk.Button(leftframe, text="+ Add",style = 'C.TButton', command=browse_file)
addBtn.pack(side=LEFT)
# addBtn2.pack(side=RIGHT)


def del_song():
    selected_song = playlistbox.curselection()
    selected_song = int(selected_song[0])
    playlistbox.delete(selected_song)
    playlist.pop(selected_song)


delBtn = ttk.Button(leftframe, text="- Del",style = 'C.TButton', command=del_song)
delBtn.pack(side=LEFT)





















rightframe = Frame(root)
rightframe.pack(pady=30)

topframe = Frame(rightframe)
topframe.pack()



lengthlabel = ttk.Label(topframe, text='Total Length : --:--')
lengthlabel.pack(pady=5)

currenttimelabel = ttk.Label(topframe, text='Current Time : --:--', relief=GROOVE)
currenttimelabel.pack()











middleframe = Frame(rightframe)
middleframe.pack(pady=30, padx=30)

playPhoto = PhotoImage(file='images/play.png')
playBtn = ttk.Button(middleframe, image=playPhoto)
# playBtn2 = ttk.Button(middleframe, image=playPhoto, command=play_music)
playBtn.grid(row=0, column=0, padx=10)
# playBtn2.grid(row=0, column=0, padx=10)


stopPhoto = PhotoImage(file='images/stop.png')
stopBtn = ttk.Button(middleframe, image=stopPhoto)
stopBtn.grid(row=0, column=1, padx=10)

pausePhoto = PhotoImage(file='images/pause.png')
pauseBtn = ttk.Button(middleframe, image=pausePhoto)
pauseBtn.grid(row=0, column=2, padx=10)

bottomframe = Frame(rightframe)
bottomframe.pack()

rewindPhoto = PhotoImage(file='images/rewind.png')
rewindBtn = ttk.Button(bottomframe, image=rewindPhoto)
rewindBtn.grid(row=0, column=0)

mutePhoto = PhotoImage(file='images/mute.png')
volumePhoto = PhotoImage(file='images/volume.png')
volumeBtn = ttk.Button(bottomframe, image=volumePhoto)
volumeBtn.grid(row=0, column=1)

scale = ttk.Scale(bottomframe, from_=0, to=100, orient=HORIZONTAL)
scale.set(70)  # implement the default value of scale when music player starts
mixer.music.set_volume(0.7)
scale.grid(row=0, column=2, pady=15, padx=30)




















root.mainloop()