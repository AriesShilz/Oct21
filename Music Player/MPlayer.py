import pygame #used to create video games
import tkinter as tkr #used to develop GUI
from tkinter.filedialog import askdirectory #it permit to select dir
import os #it permits to interact with the operating system
from mutagen.id3 import ID3     #for tagging the meta data to our songs
from ttkthemes import themed_tk as tk



user_emotion = input("Enter your mood as Happy, Sad, Calm or Energetic: ")
print(user_emotion)

if user_emotion=="Happy" or user_emotion=="happy" or user_emotion=="HAPPY":
	directory = "C:\\...\\Happy"
elif user_emotion=="Sad" or user_emotion=="sad" or user_emotion=="SAD":
	directory = "C:\\...\\Sad"
elif user_emotion=="energetic" or user_emotion=="ENERGETIC" or user_emotion=="Energetic":
	directory = "C:\\...\\Energetic"
elif user_emotion=="calm" or user_emotion=="CALM" or user_emotion=="Calm":
	directory = "C:\\...\\Calm"
else:
	print("The requested emotion based songs are currently unavailable. Please choose either Happy, Sad, Calm or Energetic if interested!")

#music_player = tkr.Tk() 
#music_player.title("Emotion Based Music Player") 
#music_player.geometry("450x430")
# Creates an object for the ThemedTk wrapper for the normal Tk class
music_player = tk.ThemedTk()       # Creates an object for the ThemedTk wrapper for the normal Tk class
music_player.title("Emotion Based Music Player")
music_player.iconbitmap(r'title.ico')
music_player.iconbitmap(r'title.ico')
music_player.geometry("480x300")


listofsongs = []
realnames = []

var = tkr.StringVar() 
song_title = tkr.Label(music_player, font="Helvetica 12 bold italic", textvariable=var, bg="MediumTurquoise", fg="white",height=2)

index = 0



def directorychooser():

    os.chdir(directory)
    song_list = os.listdir() #it returns the list of files song
    #loop over all the files in the directory

    for files in os.listdir(directory):
        #only add files with mp3 extension
        if files.endswith(".mp3"):
            realdir = os.path.realpath(files)

            #load the meta data of that song into audio variable( A dictionary)
            audio = ID3(realdir)

            #TIT2 refers to the TITLE of the song. so lets append that to realnames
            realnames.append(audio['TIT2'].text[0])
            listofsongs.append(files)

    #inializing pygame
    play_list = tkr.Listbox(music_player, font="Helvetica 10 bold italic", bg="yellowgreen", fg="white", selectmode=tkr.SINGLE, justify="center",height=10)
    song_list.reverse()
    for item in song_list:
    	pos = 0
    	play_list.insert(pos, item)
    	pos += 1
    play_list.pack(fill="x")
    pygame.init()
    pygame.mixer.init()

    #load the first song
    pygame.mixer.music.load(listofsongs[0])
    pygame.mixer.music.play()


directorychooser()

#fumction to update our label as the song changes or updates
def updatelabel():
    global index
    global songname

    var.set(realnames[index]) #set StringVar to the real name

def setvol(val):
    volume = int(val)/100    #typecasting(string into int)
    pygame.mixer.music.set_volume(volume)

def nextsong():
    #get index from gloabl
    global index
    #increament index
    index += 1
    #get the nect song from the listofsongs
    pygame.mixer.music.load(listofsongs[index])
    #play the next song
    pygame.mixer.music.play()
    #do not forget to update the Label
    updatelabel()

#similarly for the previous song
def prevsong():
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

#stop the song!!!
def stop():
    # stop the current playing song
    pygame.mixer.music.stop()
    #set our label to empty
    var.set("")


def play():
    pygame.mixer.music.play()

def pause():
    pygame.mixer.music.pause()
def unpause():
    pygame.mixer.music.unpause()


#volume control
from tkinter import HORIZONTAL
scale = tkr.Scale(music_player, from_=0, to=100, orient=HORIZONTAL, command=setvol, troughcolor="MediumTurquoise", bg="yellowgreen",width=8)
scale.set(50)
pygame.mixer.music.set_volume(50)

#, width=3, height=2, font="Helvetica 10 bold", text="Play", bg="yellowgreen/MediumTurquoise", fg="white"

prevphoto = tkr.PhotoImage(file="C:\\Users\\Shilpa\\Documents\\Music_Recommendation_from_user_emotion\\Code\\prevphoto.png")
prevbutton = tkr.Button(music_player, image=prevphoto, command=prevsong)
#prevbutton.grid()


playphoto = tkr.PhotoImage(file="C:\\Users\\Shilpa\\Documents\\Music_Recommendation_from_user_emotion\\Code\\playphoto.png")
playbutton = tkr.Button(music_player, image=playphoto, command=play)
#playbutton.grid()

stopphoto = tkr.PhotoImage(file="C:\\Users\\Shilpa\\Documents\\Music_Recommendation_from_user_emotion\\Code\\stopphoto.png")
stopbutton = tkr.Button(music_player, image=stopphoto, command=stop)
#stopbutton.grid()

pausephoto = tkr.PhotoImage(file="C:\\Users\\Shilpa\\Documents\\Music_Recommendation_from_user_emotion\\Code\\pausephoto.png")
pausebutton = tkr.Button(music_player, image=pausephoto, command=pause)
#pausebutton.grid()

resumephoto = tkr.PhotoImage(file="C:\\Users\\Shilpa\\Documents\\Music_Recommendation_from_user_emotion\\Code\\resumephoto.png")
resumebutton = tkr.Button(music_player, image=resumephoto, command=unpause)
#resumebutton.grid()


nextphoto = tkr.PhotoImage(file="C:\\Users\\Shilpa\\Documents\\Music_Recommendation_from_user_emotion\\Code\\nextphoto.png")
nextbutton = tkr.Button(music_player, image=nextphoto, command=nextsong)
#nextbutton.grid()




song_title.pack(fill="x")
scale.pack(fill="x")
prevbutton.pack(side="left",padx=20)
playbutton.pack(side="left",padx=16)
stopbutton.pack(side="left",padx=16)
pausebutton.pack(side="left",padx=16)
resumebutton.pack(side="left",padx=16)
nextbutton.pack(side="left",padx=16)
music_player.mainloop()


