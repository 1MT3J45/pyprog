from Tkinter import *
import tkMessageBox
import Tkinter
top = Tk()

mb=Menubutton ( top, text="condiments", relief=RAISED )
mb.grid()
mb.menu = Menu ( mb, tearoff = 0 )
mb["menu"] = mb.menu
m = IntVar()

k = IntVar()
mb.menu.add_checkbutton ( label="mayo", variable=m )
mb.menu.add_checkbutton ( label="ketchup",variable=k )
mb.pack()
top.mainloop()
