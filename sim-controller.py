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
topFrame.pack() 
bottomframe.pack( side = BOTTOM, pady=26)

topInnerFrame1 = Frame(topFrame,  width=126, height=60)
topInnerFrame2 = Frame(topFrame,  width=126, height=60)
topInnerFrame3 = Frame(topFrame, width=126, height=60)
topInnerFrame1.pack(side=LEFT)
topInnerFrame2.pack(side=LEFT)
topInnerFrame3.pack(side=LEFT)

startbutton = Button(topInnerFrame1, text="Start", fg="black", bg="grey")
startbutton.pack(padx=23, pady=5)

stopbutton = Button(topInnerFrame2, text="Stop", fg="black", bg="grey")
stopbutton.pack(padx=22, pady=5)

reloadButton = Button(topInnerFrame3, text="Reload", fg="black", bg="grey")
reloadButton.pack(padx=23, pady=5)

timeVar = StringVar()
timeVar.set("0.00")
timeLabel = Label(bottomframe, fg="white",  text= "Time:")
vartimeLabel = Label(bottomframe, fg="white", textvariable=timeVar)
timeLabel.pack(side = LEFT, fill=BOTH)
vartimeLabel.pack(side = RIGHT, fill=BOTH)

root.mainloop()
