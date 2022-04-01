from textwrap import fill
from tkinter import *
root = Tk()
def start():
    pass

def stop():
    pass

def reload():
    pass

topFrame = Frame(root, bg="grey", width=380, height=60)
bottomframe = Frame(root, bg="grey", width= 380, height=60)
topFrame.grid(row=0)
bottomframe.grid(row=1, pady=26)

topInnerFrame1 = Frame(topFrame,  width=126, height=60)
topInnerFrame2 = Frame(topFrame,  width=126, height=60)
topInnerFrame3 = Frame(topFrame, width=126, height=60)
topInnerFrame1.grid(row=0, column=0)
topInnerFrame2.grid(row=0, column=1)
topInnerFrame3.grid(row=0,column=2)

startbutton = Button(topInnerFrame1, text="Start", fg="black", bg="grey")

startbutton.grid(padx=23, pady=5)

stopbutton = Button(topInnerFrame2, text="Stop", fg="black", bg="grey")

stopbutton.grid(padx=22, pady=5)

reloadButton = Button(topInnerFrame3, text="Reload", fg="black", bg="grey")

reloadButton.grid(padx=23, pady=5)

timeVar = StringVar()
timeVar.set("0.00")
timeLabel = Label(bottomframe, fg="black",  text= "Time:")
vartimeLabel = Label(bottomframe, fg="black", textvariable=timeVar)
timeLabel.grid(row= 0,column=0)
vartimeLabel.grid(row=0, column=1)

root.mainloop()
