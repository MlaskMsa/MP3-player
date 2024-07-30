import tkinter
from tkinter import Menu

class Application:
    def __init__(self):
        #Create and gave a title to the app
        tk = tkinter.Tk()
        tk.title("Mp3 Player")
        
        def donothing():
            print("Hi")
        #Created a menu and added a few commands
        menubar = Menu(tk)
        file_menu = Menu(menubar,tearoff=0)
        file_menu.add_command("Open",command= donothing)
        file_menu.add_command("Exit",command= donothing)     
        
        tk.mainloop()
        
Application()