### edgar-donk.github.io

# Tkinter in Python - you've got to have style!

As you are no doubt aware tkinter introduced a theme (or tile) based module. Searching the web I was struck by how little the
new capabilities were demonstrated, questions and answers concentrated mostly on how to colour widgets and suchlike.

In order to use the scripts developed here, a modern version of Python and Tkinter (>= v 8.5) will be necessary. I find it
helpful to download the pdf version of “Tkinter 8.5 reference: a GUI for Python” 
http://infohost.nmt.edu/tcc/help/pubs/tkinter/tkinter.pdf, then run it on my pdf reader. At some stage we will be encoding and
decoding small images using the base64 module. To see what has already been achieved it will be helpful to view and install the
external module ttkthemes (pip install ttkthemes). Since we will be checking images, a graphics editor will be needed.

## What to expect

A quick tour, with working examples, through the tkinter.ttk Style module, so that you should be able to test a widget and check 
its styling changes on your own ideas and scripts.  

An even more lightning tour through the themes from tkinter.ttk and ttkthemes.

Create a few specials to show what can be achieved, after that you are only limited by your imagination.

## 01. Basics

If you are using Python 2.7 or later or any of the Python 3 versions then the tkinter version will be 8.5 or later, and if we 
import the ttk module in an active Python session then there will be no warning message.

1 import tkinter.ttk # applicable to Python 3 - all scripts will assume Python 3 is being used 

2 import Tkinter.ttk # applicable to Python 2

To help distinguish which examples refer to any particular paragraph, the file names will be prefixed by the paragraph number.

All the widgets previously found in tkinter remain, ttk has 12 widgets and 1 Style module. 2 of the widgets in ttk, Combobox and 
Treeview, have been introduced. The widgets Canvas, Listbox, Message, OptionMenu, Spinbox and Text only exist in tkinter. All
other widgets are duplicated, with the proviso that their property options do not correspond, so if we take the Button widget in
tkinter, there are 24 more property options than in ttk which has a single <style> option. If we create a similar style in our
ttk widgets we could save it as a theme. Tkinter has already created 4 standard themes common to all operating systems. Windows
and the MacOS have their own customised themes, therefore wherever possible my examples will use one of the 4 common themes Alt,
Clam, Classic or Default.
  
Widgets have one or more layers that can be referenced directly using the Style module, assisted by the style property option.
If we take a look at the button widget we have a rectangular shape divided into 4 elements, starting from the outside - border,
focus, spacing and label. Look at ![button:elements](/images/01button_elements.png) this is an example of how a button may be
constructed. We shall see that when a widget is modified or called by various themes nothing is totally hard and fast. While 
looking at elements look at the vertical scrollbar ![scrollbar:elements](/images/01scrollbar_elements.png), we have up and
down arrow as well as a thumb element all contained in a trough. We have a method within the Style module whereby we can find
out the element names and their relative positions, so there is no real reason to worry or fret.




  
