from tkinter import Tk
from tkinter.ttk import Style, Entry

root_window = Tk()

estyle = Style()
estyle.theme_use('clam') # if not used then uncomment element_create and layout
# estyle.element_create("plain.field", "from", "clam")
# follows the layout of "vista", need layout to enable configure with vista
'''
estyle.layout("EntryStyle.TEntry",
                   [('Entry.plain.field', {'children': [(
                       'Entry.background', {'children': [(
                           'Entry.padding', {'children': [(
                               'Entry.textarea', {'sticky': 'nswe'})],
                      'sticky': 'nswe'})], 'sticky': 'nswe'})],
                      'border':'2', 'sticky': 'nswe'})])
'''
estyle.configure("EntryStyle.TEntry",
    fieldbackground="light blue" # Set color here "EntryStyle.TEntry"
    )   # font must be set in entry properties - not here        

entry = Entry(root_window, style="EntryStyle.TEntry", font="Gigi 12")
entry.pack(padx=10, pady=10)

root_window.mainloop()
