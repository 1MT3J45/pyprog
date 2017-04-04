import Tkinter
import tkMessageBox
top = Tkinter.Tk()
def helloCallBack():
	tkMessageBox.showinfo( "Hello Python", "Hello World")

B = Tkinter.Button(top, text ="Hello", command = helloCallBack, bg="BLACK", fg="WHITE", font="Arial", height=20)
B.pack()
top.mainloop()
