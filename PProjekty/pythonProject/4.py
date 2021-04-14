from tkinter import *

okno = Tk()

topFrame = Frame(okno)
topFrame.pack()
bottomFrame = Frame(okno)
bottomFrame.pack(side = BOTTOM)

b1 = Button(topFrame, text = "elo ", fg = "red")
b2 = Button(topFrame, text = "elo xs", fg = "green")
b3 = Button(topFrame, text = "320", fg = "blue")

b1.pack()
b2.pack()
b3.pack()

okno.mainloop()