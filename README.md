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

All the widgets previously found in tkinter remain, ttk has 17 widgets and 1 Style module. 2 of the widgets in ttk, Combobox and 
Treeview are new. The widgets Canvas, Listbox, Message, OptionMenu, Spinbox and Text only exist in tkinter. All
other widgets are duplicated, with the proviso that their property options do not correspond, so if we take the Button widget in
tkinter, there are 24 more property options than in ttk which has a single <style> option. If we create a similar style in our
ttk widgets we could save it as a theme. Tkinter has already created 4 standard themes common to all operating systems. Windows
and the MacOS have their own customised themes, therefore wherever possible my examples will use one of the 4 common themes Alt,
Clam, Classic or Default.
  
Widgets have one or more layers that can be referenced directly using the Style module, assisted by the style property option.
If we take a look at the button widget we have a rectangular shape divided into 4 elements, starting from the outside - border,
focus, spacing and label. Look at
```
![button:elements](/images/01button_elements.png) 
```

this is an example of how a button may be constructed. We shall see that when a widget is modified or called by various themes
nothing is totally hard and fast. While we are thinking of elements look at the vertical scrollbar 

![scrollbar:elements](/images/01scrollbar_elements.png)

, we have up and down arrow as well as a thumb element all contained in a trough. We have a method within the Style module
whereby we can find out the element names and their relative positions, so there is no real reason to worry or fret.

Let us compare the two button widgets, using the script /examples/01two_buttons.py found under the examples directory. When you
run this script you will see 3 buttons. The top one is standard tkinter, the lower two are ttk. All three are grey but the
tkinter button is paler. Move the cursor over all three buttons. The two ttk buttons lighten but the tkinter button does not
react. Click on all three buttons, all three appear to be depressed, but the two ttk buttons show which of the two buttons was
depressed last. We have just seen how the ttk button's state interacts with style. If we had left out the line

s.theme_use('default')

and we were running either a Windows or Mac system then we would have seen blue ttk buttons. By using a theme all ttk widgets
react without any special input by default. This is in contrast to the original tkinter widgets which have to be individually
programmed.

## 02 Simple Style Changes

Using named elements we can change the colours, width, font and relief of our widget. Instead of using property options on each
widget, we use the Style module together with relevant component and element names. The first task is to determine the relevant
elements of our widget.

The dependancies of the queries to find out the elements and their properties are as follows:-
1 Widget name
````
--> 2 class name (widget.winfo_class)
--> 3 component name (Style.layout)
--> 4 element name (Style.element_options) 
--> 5 element value (Style.lookup)
````
Each dependancy relies on the information gained from the previous enquiry. Once the queries are set up with an interactive
session running with Style you may be able to short circuit one or more steps.

If we use the button widget as a first example run the following queries interactively in Python. 
Find the class name:-
```
import ttk
>>> s = ttk.Style()
>>> s.theme_use('classic')
>>> b = ttk.Button(None, text='Yo') # step 1 widget name
>>> bClass = b.winfo_class()
>>> bClass
'TButton'
```
The class name is 'TButton'. Now let's find the component name:-
````
>>> layout = s.layout('TButton')
>>> layout
[('Button.highlight', {'children': [('Button.border', {'border':
'1', 'children': [('Button.padding', {'children': [('Button.label',
{'sticky': 'nswe'})], 'sticky': 'nswe'})], 'sticky': 'nswe'})],
'sticky': 'nswe'})]
````
We have found 4 component names - highlight, border, padding and label (they were all preceded with 'Button.'). Be careful to
use the correct component name with right theme. That just completed the second step. As a help in determining the component
names for each widget check out the table /tables/02Components.md. See how the names change not only with the widgets, but 
sometimes also with the theme.

Now onto the element names:-
````
d = s.element_options('Button.highlight')
>>> d
('-highlightcolor', '-highlightthickness') # step 3
>>>s.lookup('Button.highlight', 'highlightthickness')
1
>>> s.lookup('Button.highlight', 'highlightcolor')
'#d9d9d9' # step 4
````
Button is a fairly straightforward widget, but some such as Progressbar, Scale and Scrollbar have an orientation, whereas 
LabelFrame, Notebook and Treeview have a main and auxiliary class name. Lastly PanedWindow has both orientation and an auxiliary
part. Let's see the differences, with a widget with an orientation property such as Scale:-
````
>>>b = ttk.Scale(None)
>>>b.winfo_class()
'TScale'    # class name
>>> layout = s.layout('Vertical.TScale') # It won't work if you use just TScale
>>>layout
[('Vertical.Scale.trough',
  {'children': [('Vertical.Scale.slider', {'side': 'top', 'sticky': ''})],
   'sticky': 'nswe'})]
>>>layout = s.layout('Horizontal.TScale') # now try the Horizontal orientation
>>>layout
[('Horizontal.Scale.trough',
  {'children': [('Horizontal.Scale.slider', {'side': 'left', 'sticky': ''})],
   'sticky': 'nswe'})]  # notice the orientation
>>>d = s.element_options('Horizontal.Scale.trough') # using the component name
>>>d
('borderwidth', 'troughcolor', 'troughrelief')  # element names
>>>s.lookup('Horizontal.Scale.slider', 'troughcolor')
'#c3c3c3'
````
That wasn't too bad, let's try a widget with an auxiliary class such as LabelFrame:-
````
>>>b=ttk.LabelFrame(None)
>>>b.winfo_class()
'TLabelframe' # you noticed it's a small f didn't you
>>>s.layout('TLabelframe')
 [('Labelframe.border', {'sticky': 'nswe'})]  # where is the label part then!!!?
>>>s.layout('TLabelframe.Label')    # OK I cheated, I knew the answer
[('Label.fill',
  {'children': [('Label.text', {'sticky': 'nswe'})], 'sticky': 'nswe'})]
````
It took a bit of web searching to find the answer in http://wiki.tcl.tk/37973 Changing Widget Colors. Read the author's opening
sentences. The information is strictly for TCL so the widgets are not totally applicable to ttk, otherwise great information. In 
order to access all the elements of Notebook use TNotebook and TNotebook.Tab, for Treeview use Treeview and Heading. (We can
optionally use 'Treeview.Heading', it produces the same results as for 'Heading'). Be careful with the names used in the
Treeview and Heading layouts:-
````
>>>s.layout('Treeview')
[('Treeview.field',
  {'border': '1',
   'children': [('Treeview.padding',
     {'children': [('Treeview.treearea', {'sticky': 'nswe'})],
      'sticky': 'nswe'})],
   'sticky': 'nswe'})]
>>>s.layout('Heading')
[('Treeheading.cell', {'sticky': 'nswe'}),
 ('Treeheading.border',
  {'children': [('Treeheading.padding',
     {'children': [('Treeheading.image', {'side': 'right', 'sticky': ''}),
       ('Treeheading.text', {'sticky': 'we'})],
      'sticky': 'nswe'})],
   'sticky': 'nswe'})]
````
This now only leaves PanedWindow, the main class is TPanedwindow, the auxiliary class is either Horiontal.Sash or Vertical.Sash.

Rather than find out the class names every time we can use the table 02ClassNames.md instead. Check this table, the main class
name is formed from the widget name where only the first letter is capitalised prefixed by a capital T, except for Treeview that
retains its widget name. Remember that those widgets that have orientation need to be prefixed by either 'Horizontal.' or
'Vertical.'.

After all that we can find the class and element names for all widgets with our chosen theme. We will use Style.configure().
As a first example let's change the button widget, we want to change the text properties, foreground, background and font.
Foreground and background are both colours which can be expressed as names or a six figure hexadecimal hash. Colour names in
tkinter are based on those used by TCL/TK colors — symbolic color names recognized by Tk 
https://tcl.tk/man/tcl8.6/TkCmd/colors.htm, note they are using RGB values that must first be converted to hash values to be
used in tkinter. Haven't we got the element names for button already? No, well we'll have to use the right component name in
our query (and it wasn't highlight). Use your interactive session, and if you were on the right track you should get an answer
together with 11 other elements. Now you are no longer limited to just foreground, background and font. 

When using configure we reference the change to make the style change using the format *newStyleName.oldStyleName*, where
oldStyleName corresponds to our class name, in our case TButton. Normally we choose a descriptive name for the newStyleName, so
for the button widget we can write :-
````
s.configure('green.TButton', foreground='green')
b = ttk.Button(self, text='Friday', style='green.TButton')
````
The style property of Button agrees with the style name for the relevant Style configuration. The configuration name can be
built on a previously named style, so we could create red.green.TButton using a red background, say. If we need to configure
another element just list the extra elemnt.
````
s.configure('mix.TButton', foreground='green',background='red')
b = ttk.Button(self, text='Friday', style='mix.TButton')
````
We can modify /examples/01two_buttons.py to incorporate the colour changes, we should see something like 
/examples/02two_coloured_buttons.py. Did you notice that the background colour on the second ttk button changed as the mouse
moved over it and when the button was pressed. The widget inherits all expressly styled properties not overwritten by our style
changes, in our case shades of grey. 

That was easy wasn't it, feel like a challenge? Let's try modifying a horizontal scrollbar, use the layout and element_options
to find all likely element candidates for the classic theme. We need to use place and set (instead of pack or grid) or else the
scrollbar remains squashed and you can't see your results. If we make the scrollbar green with a blue border the result should
look like 02scrollbar.py. When querying the element_options you should see that both the arrows and thumb have a background as
well as borderwidth so the appearance is matched. I have created a second scrollbar where the borderwidth is not changed, look
at the arrows. In reality there was not a great deal of difference to the button example, just that we had to remember to add
the orientation to the configuration name. If you try one of the other themes alt, clam or default we have the additional option
of arrowcolor, try out this element with pink say. Classic has no arrowcolor but if you leave it in then there is no reaction,
not even a warning.

The last type of widget are those with auxiliary parts. Taking LabelFrame as an example, we would normally wish to modify the
label part rather than the Frame. We can fill the frame with a tkinter coloured frame to show off the widget. The second
labelframe by contrast has a coloured frame. It is important to emphasise that configure calls either TLabelframe or
TLabelframe.Label, depending whether we wish to alter the label or the frame, but in both cases the style property only refers
to TLabelframe with no suffix. This is illustrated in /examples/02labelframe.py.

We are now in a position to change the colour and size of any widget, but whenever the state changes our widget will revert to
a style inherited from the theme being used, so the interaction of states and style will be our next topic.

## 03 Linking Style with State

Every widget exists with a dynamic state that for some widgets can be directly changed by the user's actions, such as moving the
mouse over the widget, or by selecting or pressing the widget. To assist the user the widget changes in colour, relief and/or
size. This positive feedback assists in enhancing the user's experience. Other states are changed through the program. States
are a fundamental part of styles and themes. Check out the table /tables/03states.md if you need to refresh your memory. All
stated have an opposite situation whereby the name is prefixed by an exclamation mark, so the opposite of disabled is !disabled
and not one of the other states such as active.

Some widgets, such as Frame would hardly ever need a state other than the normal state, others such as Button only really are 
useful if they have different states. When programming with states be aware that a widget with no named state is in the "normal"
state even though it is not directly referenced, it is implicitly the state we have used when making simple changes. 

We can determine what states are currently being used in a theme. Just as in the simple style change we need to know the class
name and the element we are interested in. So if we wished to find the situation for the relief elemnt on a button we use 
map() in the following manner:-
````
from tkinter.ttk import Style, Button
>>>s = Style()
>>>s.theme_use('default')
>>>s.map('TButton', 'relief')
[('!disabled', 'pressed', 'sunken')]
````
In this case the theme uses a compound state, in that the pressed state only applies when the button is not disabled, and the
property is 'sunken'. These mapped states vary with both widget and theme. Within a theme we can have a common mapping.
````
>>>s.theme_use('default')
>>>s.map('TButton', 'background')
[]
````
Weird - we know that this changed in our button examples, so how to find out what is going on. Let's see if we have a common
mapping working here.
````
>>>s.theme_use('default')
>>>s.map('.', 'background')
[('disabled', '#d9d9d9'), ('active', '#ececec')]
````
Ahha - now we can see that all widgets with a background element will react in a similar way, so if you haven't done it see what
happens when you pass the cursor over our scrollbar example. By the by if we test for relief with a common mapping we get an
empty result, so common is a specific instance and not some form of wildcard.
````
>>>s.map('.', 'relief')
[]
````

One way to change the properties of a widget is to expand upon our simple method, so the normal state is set by configure(), we
can then set the other states using map(). This means that any single element could have several properties corresponding to 
more than one states. Related states should be listed with tuples. We can see this in the example above, we have an element
called background with a list of two tuples, the first tuple is for the disabled state ('disabled', '#d9d9d9').

In the example 03map_button.py we have configure which sets up the general widget appearance then using map to set the active
state by changing the background colour. Both configure and map use the same reference used in the style property. For a bit of
fun we have a random selection from 6 colours, in order to set the active colour we first find the RGB colour using
winfo_rgb(color) - color is the variable - then we change each of the RGB components and finally convert back to the hash value.
Simple colour manipulations are possible in the RGB scheme. A further frill is that we use a white foreground for dark
background and a black foreground for a yellow background.

As we can see keeping to the style system we can easily have two or more widgets with differing properties - this is useful when
comparing total effects during the testing phase.

The order of mapping states for the element is important. If the active element is placed at the head then when the button or
scrollbar is pressed the colour remains as the active colour. 

## 04 Image - First Steps

Tkinter and ttk can work with gif, pgm or ppm images using PhotoImage or xbm images if we use BitmapImage modules loaded from
tkinter. If your version of tkinter is 8.6 or higher then you can work with png files direct. Some widgets have a property
called image (check out if it is shown on Tkinter 8.5 reference: a GUI for Python) so once the image is initiated we can load it
directly onto the widget. All the images I will be working with will be found in the directory "images". and the programs will
be run assuming that the images can be found in this position created as sub-directory of the directory where the programs run
on your computer.




