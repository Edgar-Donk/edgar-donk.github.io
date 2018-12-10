# comparing the button widgets
from tkinter.ttk import Style
from tkinter import Tk
from tkinter import Button as orig
from tkinter.ttk import Button as tile

root=Tk()
s = Style()
s.theme_use('default')
origbutton(root,text='original').pack()
tilebutton(root,text='ttk themed').pack()
tilebutton(root,text='2nd ttk').pack()

root.mainloop()
