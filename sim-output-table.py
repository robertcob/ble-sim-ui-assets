from tkinter import *
from tkinter.ttk import *
from tkinter.font import *
from tk_extensions import ScrollableTV

root = Tk()
ff10=Font(family="Consolas", size=10)
ff10b=Font(family="Consolas", size=10, weight=BOLD)

# init a scrollabletv for output table
tv=ScrollableTV(root, selectmode=BROWSE, height=13, show="tree headings", columns=("Time", "Sensor", "Message"), style="Foo2.Treeview")
tv.heading("Time", text="Time", anchor=W)
tv.heading("Sensor", text="Sensor", anchor=W)
tv.heading("Message", text="Message", anchor=W)
tv.column("#0", width=0, stretch=False)
tv.column("Time", width=80, stretch=False)
tv.column("Sensor", width=80, stretch=False)
tv.column("Message", minwidth=1400, width=220, stretch=True)
tv.grid(padx=8, pady=(8,0))

# style config. use a ScrollableStyle and pass in the ScrollableTV whose configure needs to be managed. if you had more than one ScrollableTV, you could modify ScrollableStyle to store a list of them and operate configure on each of them
s=ScrollableTV.ScrollableStyle(tv)
s.configure("Foo2.Treeview", font=ff10, padding=1)
s.configure("Foo2.Treeview.Heading", font=ff10b, padding=1)

# init a scrollbar
sb=Scrollbar(root, orient=HORIZONTAL)
sb.grid(row=1, sticky=EW, padx=8, pady=(0,8))
tv.configure(xscrollcommand=sb.set)
sb.configure(command=tv.xview)

### example insertion into table
### will be used programatically in driver code
tv.insert("", END, values=("0", "2", "Waiting for messages..."))
tv.insert("", END, values=("0", "1", "Waiting for messages..."))
tv.insert("", END, values=("1616", "2", "Connected to central"))
tv.insert("", END, values=("1650", "1", "Connected to peripheral"))
tv.insert("", END, values=("1721", "2", "Sending GATT  Profile..."))
tv.insert("", END, values=("2505", "1", "Created Service w/ handle 0x180D"))
tv.insert("", END, values=("2612", "1", "Identified serial-number characteristic"))
tv.insert("", END, values=("3282", "1", "Identified model-number characteristic"))
tv.insert("", END, values=("3397", "1", "Identified manufacturer-name characteristic"))
tv.insert("", END, values=("3834", "1", "Service created w/ handle 0x2A29"))
tv.insert("", END, values=("4215", "1", "Identified heart-measurment characteristic"))
tv.insert("", END, values=("2824", "1", "Identified heart-rate-control-point characteristic"))
tv.insert("", END, values=("5024", "2", "Completed sending profile"))
tv.insert("", END, values=("5604", "2", "writing to handle 0x2A29 heart-measurment characteristic"))




#click in the TV to test
root.mainloop()
