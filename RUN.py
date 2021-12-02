import tkinter as tk
from tkinter import messagebox
from crypter import main

root= tk.Tk()
root.withdraw()


def ExitApplication():
    MsgBox = tk.messagebox.askquestion ('NOTE',"""\
NOTE:
if you lose your key your data is gone i'm not responsible it's YOUR mistake!

proceed anyway?""",icon = 'warning')
    if MsgBox == 'yes':
       main()
    else:
        tk.messagebox.showinfo('exit','you will now exit the porgramm!', icon = 'warning')
        exit()
ExitApplication()
  
root.mainloop()