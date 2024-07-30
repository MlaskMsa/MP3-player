import tkinter
from tkinter import Menu
from tkinter import filedialog  

class Application:
    def __init__(self):
        #Create and gave a title to the app
        tk = tkinter.Tk()
        tk.title("Mp3 Player")
        
        #Create a functino to open a file    
        def open():
            path = filedialog.askopenfilename()
            print(path)
            
        #Created a menu and added a few commands
        menubar = Menu(tk)
        file_menu = Menu(menubar,tearoff=0)
        menubar.add_cascade(menu=file_menu, label="File")
        file_menu.add_command(label="Open",command=open)
        tk.config(menu=menubar)
        
        tk.mainloop()
        
Application()