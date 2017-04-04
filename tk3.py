import Tkinter
import tkMessageBox

top = Tkinter.Tk()
C = Tkinter.Canvas(top, bg="blue", height=250, width=300)

coord = 100, 100, 200, 100
arc = C.create_line(coord)
C.pack()
top.mainloop()
