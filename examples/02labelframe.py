from tkinter import Frame,Tk
from tkinter.ttk import LabelFrame,Style

root = Tk()

s = Style()
ch = 'lightgreen'   # change colour here
s.configure(ch +'.TLabelframe.Label', background=ch)  # altering label - anciliary part
s.configure('pink.TLabelframe', background='pink')    # altering main part

# LabelFrame with altered anciliary part
lf = LabelFrame(root, text = "Test", style = ch+".TLabelframe") # do not use ch+".TLabelframe.Label"
lf.pack( anchor = "w", ipadx = 10, ipady = 5, padx = 10,
                  pady = 0, side = "top")
Frame(lf, width=100, height=100, bg='yellow').pack()

lf1 = LabelFrame(root, text = "Test", style = "pink.TLabelframe") 
lf1.pack( anchor = "w", ipadx = 10, ipady = 5, padx = 10,
                  pady = 0, side = "top")
Frame(lf1, width=100, height=100, bg='yellow').pack()

root.mainloop()
