from tkinter import *
from textwrap import fill
# from tkinter.ttk import *
from tkinter.font import *
from tk_extensions import ScrollableTV


root = Tk()
root.title("ble-simulation")
ff10=Font(family="Consolas", size=10)
ff10b=Font(family="Consolas", size=10, weight=BOLD)

menu = Menu(root, border=2)
root.config(menu=menu)
subMenu = Menu(menu)
menu.add_cascade(label="Attack Models", menu=subMenu)

masterFrame =Frame(root)
masterFrame.grid(row=0)

winH = 420
winW = 580
ncols = 10
nrows = 10
cellW = winW / ncols
cellH = winH / nrows

class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        return

def generatGrid(nrows, ncols):
    grid = []
    for r in range(nrows):
        row = [ Node(r, c) for c in range(ncols) ]
        grid.append(row)
    return grid

def drawNode(canvas, node):
    x1 = cellW * node.col
    y1 = cellH * node.row
    x2 = x1 + cellW
    y2 = y1 + cellH
    canvas.create_rectangle(x1, y1, x2, y2)
    return

def drawGrid(canvas, grid):
    for row in grid:
        for node in row:
            drawNode(canvas, node)
    return
canvas = Canvas(masterFrame, width=winW, height=winH, 
                   borderwidth=0, highlightthickness=0, bg="white")
canvas.grid( row=0, column=0, sticky=EW)

# init a scrollabletv
bottomMasterFrame = Frame(root)
bottomMasterFrame.grid(row=1)
tv1=ScrollableTV(bottomMasterFrame, selectmode=BROWSE, height=4, show="tree headings", columns=("Time", "Sensor", "Task", "Payload"), style="Foo2.Treeview")
tv1.heading("Time", text="Time", anchor=W)
tv1.heading("Sensor", text="Sensor", anchor=W)
tv1.heading("Task", text="Task", anchor=W)
tv1.heading("Payload", text="Payload", anchor=W)
tv1.column("#0", width=0, stretch=False)
tv1.column("Time", width=100, stretch=False)
tv1.column("Sensor", width=100, stretch=False)
tv1.column("Task", width=100, stretch=False)
tv1.column("Payload", minwidth=1400, width=680, stretch=True)
tv1.grid(row=2, column=0, padx=8, pady=(8,0))

# style config. use a ScrollableStyle and pass in the ScrollableTV whose configure needs to be managed. if you had more than one ScrollableTV, you could modify ScrollableStyle to store a list of them and operate configure on each of them
s1=ScrollableTV.ScrollableStyle(tv1)
s1.configure("Foo2.Treeview", font=ff10, padding=1)
s1.configure("Foo2.Treeview.Heading", font=ff10b, padding=1)

# init a scrollbar
sb1=Scrollbar(bottomMasterFrame, orient=HORIZONTAL)
sb1.grid(row=3, sticky=EW, padx=8, pady=(0,8))
tv1.configure(xscrollcommand=sb1.set)
sb1.configure(command=tv1.xview)

sideContentFrame = Frame(masterFrame)
sideContentFrame.grid( row = 0, column=1)

## init a scrollabletv for output table
tv2=ScrollableTV(sideContentFrame, selectmode=BROWSE, height=13, show="tree headings", columns=("Time", "Sensor", "Message"), style="Foo2.Treeview")
tv2.heading("Time", text="Time", anchor=W)
tv2.heading("Sensor", text="Sensor", anchor=W)
tv2.heading("Message", text="Message", anchor=W)
tv2.column("#0", width=0, stretch=False)
tv2.column("Time", width=80, stretch=False)
tv2.column("Sensor", width=80, stretch=False)
tv2.column("Message", minwidth=1400, width=220, stretch=True)
# tv2.grid(row=0, column=0, padx=8, pady=(8,0))
tv2.grid(padx=8, pady=(8,0))

# style config. use a ScrollableStyle and pass in the ScrollableTV whose configure needs to be managed. if you had more than one ScrollableTV, you could modify ScrollableStyle to store a list of them and operate configure on each of them
s2=ScrollableTV.ScrollableStyle(tv2)
s2.configure("Foo2.Treeview", font=ff10, padding=1)
s2.configure("Foo2.Treeview.Heading", font=ff10b, padding=1)

# init a scrollbar
sb2=Scrollbar(sideContentFrame, orient=HORIZONTAL)
##sb2.grid(row=1, sticky=EW, padx=8, pady=(0,8))
sb2.grid(row=1, sticky=EW, padx=8, pady=(0,8))
tv2.configure(xscrollcommand=sb2.set)
sb2.configure(command=tv2.xview)

notes = Text(root, width=50, height=10, bg="white")
# notes.grid(row=1, column=1)

grid = generatGrid(nrows, ncols)
drawGrid(canvas, grid)

def start():
    pass

def stop():
    pass

def reload():
    pass

rootFrame= Frame(sideContentFrame, highlightbackground="#F6F5F5", highlightthickness=2)
rootFrame.grid(row=2)
topFrame = Frame(rootFrame, bg="grey", width=380, height=60)
bottomframe = Frame(rootFrame, bg="grey", width= 380, height=60)
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
