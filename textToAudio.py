#importimg tkinter module for windows.
#gtts for text to audio.
#playsound for playing sound.
from tkinter import *
from gtts import gTTS
from playsound import playsound

#making play function.
def Play():
    #getting value from list for play.
    value = listBox.get(0)
    print(value)
    #naming the audio file.
    audioFile = "textToAudio.mp3"
    #getting object for audio
    speech = gTTS(text = value,lang = "en",slow = False)
    #saving the audio file
    speech.save(audioFile)
    #play the sound
    playsound(audioFile)
#making entry function
def enter():
    listBox.insert(0,entry.get())
    entry.delete(0,END)
    

win = Tk()
win.title("Text to Audio")
win.geometry("350x550")
win.configure(bg = "black")

textLabel = Label(win,text = "Text To Audio",fg = "green",bg = "black",font = ("Calibri",30,"bold"),justify = "right", borderwidth = 5)
textLabel.grid(row = 0,column = 1,columnspan = 3,padx = 10,pady = 15)

listBox = Listbox(win,height = 20,width = 40,bg = "white")
listBox.grid(row = 1,column = 2,columnspan = 5,padx = 10,pady = 15)

entry = Entry(win,width = 40)
entry.place(x = 10, y = 450)

enterButton = Button(win,text = "Enter",command = enter)
enterButton.place(x = 20, y = 490)

playButton = Button(win,text = "Play",command = Play)
playButton.place(x = 100, y = 490)

win.mainloop()
