from tkinter import *
from tkinter.ttk import *
from tkinter.font import *
from tk_extensions import ScrollableTV

root = Tk()
ff10=Font(family="Consolas", size=10)
ff10b=Font(family="Consolas", size=10, weight=BOLD)

# init a scrollabletv
tv=ScrollableTV(root, selectmode=BROWSE, height=4, show="tree headings", columns=("Time", "Sensor", "Task", "Payload"), style="Foo2.Treeview")
tv.heading("Time", text="Time", anchor=W)
tv.heading("Sensor", text="Sensor", anchor=W)
tv.heading("Task", text="Task", anchor=W)
tv.heading("Payload", text="Payload", anchor=W)
tv.column("#0", width=0, stretch=False)
tv.column("Time", width=100, stretch=False)
tv.column("Sensor", width=100, stretch=False)
tv.column("Task", width=100, stretch=False)
tv.column("Payload", minwidth=1400, width=680, stretch=True)
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
tv.insert("", END, values=("626", "2", "send",  "'TYPE': 'advertisingPkt', 'SRC': 2, 'DST': 0, 'LSRC': 2, 'LDST': 0, 'SEQ': 0, 'DATA': None, 'CHANNEL': 7"))
tv.insert("", END, values=("837", "1", "receive",  "'TYPE': 'advertisingPkt', 'SRC': 2, 'DST': 0, 'LSRC': 2, 'LDST': 0, 'SEQ': 0, 'DATA': None, 'CHANNEL': 7"))
tv.insert("", END, values=("1126", "1", "send", '''"TYPE": "CONNECT", "SRC": 7, "DST": 0, "LSRC": 7, "LDST": 2, "SEQ": 0, "DATA": null, "CHANNEL": 7"'''))
tv.insert("", END, values=("1616", "2", "receive", '''"TYPE": "CONNECT", "SRC": 7, "DST": 0, "LSRC": 7, "LDST": 2, "SEQ": 0, "DATA": null, "CHANNEL": 7"'''))
#click in the TV to test
root.mainloop()
