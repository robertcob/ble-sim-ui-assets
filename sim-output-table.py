from tkinter import *
from tkinter.ttk import *
from tkinter.font import *
from tk_extensions import ScrollableTV

root = Tk()
ff10=Font(family="Consolas", size=10)
ff10b=Font(family="Consolas", size=10, weight=BOLD)

# init a scrollabletv
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
### tv.insert("", END, values=("foobar", "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"))

#click in the TV to test
root.mainloop()
