from tkinter import *



root = Tk()

def start():
    pass

def stop():
    pass

def reload():
    pass

parent = Frame(root, bg="grey")
bottomframe = Frame(root, bg="grey")
parent.pack() 
bottomframe.pack( side = BOTTOM )


startbutton = Button(parent, text="Start", fg="black", bg="white")
startbutton.pack( side = LEFT)

stopbutton = Button(parent, text="Stop", fg="black", bg="white")
stopbutton.pack( side = LEFT )

reloadButton = Button(parent, text="Reload", fg="black", bg="white")
reloadButton.pack( side = LEFT )

timeVar = StringVar()
timeVar.set("0.00")
timeLabel = Label( bg="white", fg="black", text= "Time: ", padx=5)
vartimeLabel = Label( bg="white", fg="black", textvariable=timeVar)

timeLabel.pack(side=LEFT)
vartimeLabel.pack(side=LEFT)



root.mainloop()
