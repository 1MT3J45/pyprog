from Tkinter import *
root = Tk()

e1 = Entry(root)
e2 = Entry(root)
l = Label(root)
def callback():
    total = float(e1.get())-float(e2.get())
    l.config(text="Result = %f" % total)

b = Button(root, text="SUB", command=callback)
for widget in (e1, e2, l, b):
    widget.pack()

b.mainloop()
