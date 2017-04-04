from Tkinter import *

top = Tk()
mb=Menubutton ( top, text="File")
#mb.grid()
mb.menu=Menu ( mb )

mb["menu"] = mb.menu

mb.menu.add_checkbutton ( label="Open" )
mb.menu.add_radiobutton ( label="Save" )
mb.pack()
top.mainloop()
