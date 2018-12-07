### edgar-donk.github.io

# Tkinter in Python - you've got to have style!

As you are no doubt aware tkinter introduced a theme (or tile) based module. Searching the web I was struck by how little the new 
capabilities were demonstrated, questions and answers concentrated mostly on how to colour widgets and suchlike.

In order to use the scripts developed here, a modern version of Python and Tkinter (>= v 8.5) will be necessary. I find it helpful
to download the pdf version of “Tkinter 8.5 reference: a GUI for Python” http://infohost.nmt.edu/tcc/help/pubs/tkinter/tkinter.pdf,
then run it on my pdf reader. At some stage we will be encoding and decoding small images using the base64 module. To see what has 
already been achieved it will be helpful to view and install the external module ttkthemes (pip install ttkthemes). Since we will
be checking images, a graphics editor will be needed.

## What to expect

A quick tour, with working examples, through the tkinter.ttk Style module, so that you should be able to test a widget and check 
its styling changes on your own ideas and scripts.  

An even more lightning tour through the themes from tkinter.ttk and ttkthemes.

Create a few specials to show what can be achieved, after that you are only limited by your imagination.

## 01. Basics

If you are using Python 2.7 or later or any of the Python 3 versions then the tkinter version will be 8.5 or later, and if we 
import the ttk module in an active Python session then there will be no warning message.

import tkinter.ttk # applicable to Python 3 - all scripts will assume Python 3 is being used 
import Tkinter.ttk # applicable to Python 2

To help distinguish which examples refer to any particular paragraph, the file names will be prefixed by the paragraph number.


