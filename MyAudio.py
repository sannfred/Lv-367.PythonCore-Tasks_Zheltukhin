from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
from pygame import mixer



root = Tk()

menubar = Menu(root)
root.config(menu=menubar)
sub_menu = Menu(menubar, tearoff = 0)

def browse_file():
    global musicname
    musicname = filedialog.askopenfilename()
    print(musicname)

menubar.add_cascade(label="File", menu=sub_menu)
sub_menu.add_cascade(label='Add', command =browse_file)
sub_menu.add_cascade(label='Exit', command =root.destroy)



mixer.init()
root.title("MyAudio")



global statusbar
statusbar = Label(root,text="The program has been made by Serhii Zheltukhin",relief=SUNKEN)
statusbar.pack(side=BOTTOM, fill=X)
play_button = PhotoImage(file = 'D:/MyAudio/icons/play.png')
pause_button = PhotoImage(file = 'D:/MyAudio/icons/pause.png')
stop_button = PhotoImage(file = 'D:/MyAudio/icons/stop.png')
backward_button = PhotoImage(file = 'D:/MyAudio/icons/backward.png')
forward_button = PhotoImage(file = 'D:/MyAudio/icons/forward.png')

paused = FALSE
def start():
  global paused
  if paused:
        mixer.music.unpause()
        statusbar["text"]= "You have been returned the party bruh"
        paused = FALSE
  else:
        try:
         mixer.music.load(musicname)
         mixer.music.play()
         statusbar["text"]= "You have been started the party bruh"
        except:
         tkinter.messagebox.showerror('Error','Choose the correct file')

def pause():
    global paused
    mixer.music.pause()
    paused = TRUE
    statusbar["text"]= "Paused"

def forward():
    print('next track')

def backward():
    print('previous track')

def stop():
    mixer.music.stop()
    statusbar["text"]= "The party is over :("

def set_vol(val):
    music_volume = int(val)/100
    mixer.music.set_volume(music_volume)

def rewind():
    mixer.music.play()
    statusbar["text"]= "Rewinded track"

midleframe = Frame(root)
midleframe.pack()

b_play = Button(midleframe, image = play_button, command = start)
b_play.grid(row = 0, column = 0, padx =5)
b_pause = Button(midleframe, image = pause_button, command = pause)
b_pause.grid(row = 0, column = 1, padx =5)
b_stop = Button(midleframe, image = stop_button, command = stop)
b_stop.grid(row = 0, column = 2, padx =5)
b_backward = Button(midleframe, image = backward_button, command = rewind)
b_backward.grid(row = 0, column = 3, padx=5)
volume_scale = Scale(root, from_=0,to_=100, orient=HORIZONTAL, command = set_vol)
volume_scale.set(100)
mixer.music.set_volume(1)
volume_scale.pack()

root.mainloop()
