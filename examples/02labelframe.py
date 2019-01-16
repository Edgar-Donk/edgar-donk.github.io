'''
LabelFrame is split, and we have to have two separate configure clauses to be able to alter
the colours of the Label (anciliary part) and the Frame (main part). 2 LabelFrames are 
displayed one with a label colour change  the other with a frame colour change.
'''
from tkinter import Frame,Tk
from tkinter.ttk import LabelFrame,Style

root = Tk()

s = Style()
ch = 'lightgreen'   # change label colour here, we could program different colours to suit the application requirements
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
