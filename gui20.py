from Tkinter import *
root = Tk()

labelframe = LabelFrame(root)
labelframe.pack()

left = Label(labelframe, text="Inside the LabelFrame")
left.pack()

left = Label(labelframe, text="Inside the LabelFrame")
left.pack()

root.mainloop()
