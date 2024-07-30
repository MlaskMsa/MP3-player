import tkinter
from tkinter import Menu
from tkinter import Button
from tkinter import filedialog
import pygame

class Application:
    def __init__(self):
        #Create and gave a title to the app
        tk = tkinter.Tk()
        tk.title("Mp3 Player")
        tk.geometry("250x250")
        tk.resizable(False,False)
        
        #Create a functino to open a file    
        def open():
            self.path = filedialog.askopenfilename()
            
        #Created a menu and added a few commands
        menubar = Menu(tk)
        file_menu = Menu(menubar,tearoff=0)
        menubar.add_cascade(menu=file_menu, label="File")
        file_menu.add_command(label="Open",command=open)
        tk.config(menu=menubar)
        
        #Create a function to play audio
        def Play():
            if self.path:
                pygame.mixer.init()
                pygame.mixer_music.load(self.path)
                pygame.mixer_music.play()
            else:
                print("File not found")
        
        def Stop():
            pygame.mixer.music.stop()
            
        #Create a button for playing audio
        playbutton = Button(tk,text="Play",command=Play)
        playbutton.pack()
        
        #Create a button for stop playing the audio
        stopbutton =  Button(tk,text="Stop",command=Stop)
        stopbutton.pack()
        #Mainloop
        tk.mainloop()
        
Application()