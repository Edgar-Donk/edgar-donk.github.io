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
```
![button:elements](/images/01button_elements.png) 


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

Tkinter and ttk can work with gif, pgm or ppm images using PhotoImage or xbm images if we use BitmapImage modules, loaded from
tkinter. If your version of tkinter is 8.6 or higher then you can work with png files directly. Some widgets have a property
called image (check out if it is shown on Tkinter 8.5 reference: a GUI for Python) so once the image is initiated we can load it
directly onto the widget. All the images I will be working with will be found in the directory "images". and the programs will
be run assuming that the images can be found in this position created as sub-directory of the directory where the programs run
on your computer.

First off we shall load just an image onto a button and see what happens when we pass the cursor over it, and press the button.
Load up 04button_image.py not forgetting to place the images butImage.png and butImageTrans.png in your images file (if you are
running tkinter 8.5 uncomment the lines as indicated, also comment out the  line indicated). We have loaded PhotoImage from 
tkinter where we load the image into PhotoImage creating a reference which will be used within the widget's property option
image. 

When working with images in a class there is always the problem that the image will not show unless special precautions
are taken. When the image is a local variable reload the image directly after referencing it with the widget. Alternatively we
can make the image a self variable. 

You should see three buttons, the top one with just an image, the second uses the same image with the centre made transparent -
you may think it looks quite promising, until we see the third text. As it stands it is obvious that the image option is not
always useful, it does not change dynamically with the widget. Where a widget can work with a single sized widget, as in a
pictogram, then this option should be considered. We can load the pictogram image and text simultaneously by using the compound
option. 

If multiple pictograms are available we can change these according to state. Check out the example 04button_pictograms.py this
has three pictograms linked to 3 states which must have the active state listed last just as we needed to do in the mapping 
situation. When using the image property always ensure that there are an odd number of states, therefore the first state remains
anonymous.

## 05 Image - Create Widgets with Rounded Corners and Shadow Effects

The 4 themes common to tkinter can be found where your python program is installed under the directory tcl/tk8.6/ttk. Apart from
default which is listed as defaults.tcl, all the other themes are listed themenameTheme.tcl. There are obvious differences
between tcl and tkinter but we can recognise some commands such as map and configure, we can also spot the element and state
names. A new part of the mix is when we look at the OS specefic themes such as aqua or vista have variables that are system
dependant. Even so we should be able to recognise how the answers to some of our scripts were formed. It would seem that the
common themes have little to do with images and thus able to give the widest possible support to any style alterations we wish
to make. By contrast it will be found that if one of the OS dependant themes was to be used as a basis then  changes would not
be so straightforward. 

As I said at the beginning there are remarkably few instances of the more interesting style changes found when trawling the
internet. Up until this point most of the examples could have been made using "Tkinter 8.5 reference: a GUI for Python". The few
instances I did find I will reproduce here.

The first example is based on that created by Bryan Oakley a stalwart of StackOverflow. His original script created visible
frames around entry and text widgets, example 05rounded_frame.py. Since he is using encoded data there is no reference to a
file, instead PhotoImage refers to this data directly. Normally we have no states in the frame widget so he introduces lambda
functions tied into <FocusIn> and <FocusOut> events. He is using 2 separate images, the first is where the frame's contents have
focus, the second where it loses focus. Click within the upper and lower frames, see how the outer colour changes, also note
that the frame has decidedly rounded corners and a shadow on the right hand and lower sided. 
 
Let's remind ourselves about the layout and elements for frame:-
```
>>>s.theme_use('default')
>>>s.layout('TFrame')
[('Frame.border', {'sticky': 'nswe'})]
>>>s.element_options('Frame.border') # only one component to query
('background', 'borderwidth', 'relief')
```
In our script, compared to TFrame. Bryan created an extra state and changed the border, using the command
```
style.element_create("RoundedFrame", "image", "frameBorder", # he was working on the RoundedFrame, added an image 
    ("focus", "frameFocusBorder"), border=16, sticky="nsew") # added the state focus  set to an image and changed the border
```
The number 16 for border is important, it is the allowance needed to create the rounded corners and shadows, without this the 
resulting image created would look pretty terrible. A single figure is the equivalent of (16,16,16,16). The lower frame has
obviously grown in comparison to the upper frame and looks pretty smart, both frames have the same style 'RoundedFrame'. Now is
a good time to have a look at the underlying image. We will need to decode the coded part to find out about the underlying
image. Since the coding is quite old it can only be a gif image. (Use all the code the dots below are just a shortcut for
continuity).
```
import base64
with open ('frameFocusBorder.gif','wb') as f:
    decoded = base64.decodebytes(b"""
R0lGODlhQABAAPcAAHx+fMTCxKSipOTi5JSSlNTS1LSytPTy9IyKjMzKzKyq
..... 
Ry/99NIz//oGrZpUUEAAOw==""")
    f.write(decoded)
```
Using 05rounded_frame.py use the code from img1 (frameFocusBorder), we should see an image file frameFocusBorder.gif is created.
You should see a file that is 64 by 64 pixels large. Load this on an image editor zoom in so that the pixels are shown as
squares and move your cursor to where the centre of the corner is, and we can see why we have a border of 16 all round. If we
reduce this figure to 8 say we will see about 13 indentations on the long side. A border of 12 will still show indentations, 
although not as pronounced, by 16 they have disappeared altogether. It would seem that when a widget image is extended only the
inner part of the image between the border extremes is copied for the extension.

What happens when we adapt the above method for a labelframe? What about the top part of the frame where the text is written
between a visible frame? Will we need a special method to create the gap? Ah well fools rush in where angels fear to tread. Run
05rounded_labelframe.py. Well the labelframe reacts well, we see the label sitting in the frame break, and changing colour as a
result of the program logic, try reversing the selection order and choosing one of the widgets with orientation. The
style.element_create and style.layout remain the same as for the frame example. Since we no longer depend upon an event linked
to clicking there are no more lambda functions but we do change the state of the labelframes triggered by command options of the
widgets. You did notice the colour change of the frame - first obtain the decoded image, make the changes to the colour then 
encode once again. 
```
import base64
with open('borderGrey1.gif', 'rb') as f:
    encoded = base64.encodestring(f.read())
    print(encoded.decode('latin1')) # contains all western characters but not the €
```
I altered the colour of the grey image.

The next example 05search_entry,py will create a special frame, resembling the mac search element. Once again the image is
loaded as encoded data, this time the programmer uses the gif property to make multiple images. Look at the PhotoImage lines of
code where the format is used. The programmer is altering the entry widget, using the PhotoImage alias names "search1" rather
than the "s1" name. Compare is layout to that of a normal entry widget.
```
[('Entry.field',
  {'border': '1',
   'children': [('Entry.padding',
     {'children': [('Entry.textarea', {'sticky': 'nswe'})],
      'sticky': 'nswe'})],
   'sticky': 'nswe'})]
```   
The other item of note is how he deals with the border width. Originally it was 1 all round, now it is ```border=[22, 7, 14]```.
This follows the same convention as used for padding. Check out table 05padding_border_layout.md. Since we are using the normal
interactive states of the entry widget, no additional programming is required as was necessary for the label example. Using our
newly acquired decoding skills we can see how the border layout numbers are derived. 22 pixels clears the tail of the
magnifiying glass, 7 pixels clears the corner and the top clearance, whilst 14 pixels clears the right hand end. As it stands 
this widget could be lengthened horizontally, but there is no was we could extend it vertically without a strange looking
magnifiying glass formed as a result. When using an image ensure there is a section that can be repeated left and right, top and
bottom.

We should now be able to understand how to manage themes. When we use a simple style change affected widgets require that the 
style property refers to the style change name. When a theme change is made affected widgets require no reference, therefore the
names used in the style changes such, as "search1" would not be appropriate. We should be thinking of class names, once a style 
has been tested and is ready to be part of the theme we would change the name from "new.TButton" to just "TButton" say. 

Now would be a good a time as any to inspect what ttkthemes has to offer. Apart from the interface to python most is written in 
TCL scripting language. We can take stock of the themes on offer, most work with gif images, that are substitutes for the border
part of the relevant widget. Most use one of the 4 common themes as a parent. Aquativo uses coded images, whereas the black
theme has no images. There are 3 themes that can use png images, but these are only usable with tkinter 8.6 or above. Clam is
the most popular parent theme, although if you were to run these themes it would be difficult to tell. Most images are about 60
by 60 pixels. 

If you were to install ttkthemes it is easy to swith between the normal themes and ttkthemes. If you were to load the standard
ttk Style module, then ttkthemes ar cut out, however if you load up ttkthemes 
```
import ttkthemes as ts  
.....
        try:
            self.s = ts.themed_style.ThemedStyle()
        except (NameError, AttributeError):
            self.s = Style()
```
then any normal command used by Style can be used with no change providing we use the same alias system, in our case self.s., so
list(sorted(self.s.theme_names())) would work for both the standard themes and the standard themes plus the ttkthemes.

When comparing a ttktheme with a standard theme the first obvious difference is that we are loading the image files and using
photo (we know as PhotoImage in python) on all the images, which are then referred later on by their name without the gif
suffix. Thereafter the ttkthemes closely follow the standard themes by first loading up the colour aliases, then configuring the
general settings using configure, followed by mapping the general states. From thereon the themes configure and map out the
individual widgets, often the simple widgets are left out and the parent theme's widgets are used. The images are loaded using
$I(image filename) as opposed to image as in python. The padding and border sizes would be shown as
```
-padding {6 2 6 2}
as compared to in python
border=[22, 7, 14]
```
After all that we see that ttkthemes has one or two major differences to the standard themes, look at the different ways that
the combobox downward arrow is depicted. The button widget is the normal way to see whether this theme appeals to you or not. 
Check some of the images - you may notice that a pressed image is the same as a normal image except that it has been turned
upside down. So once you are aware of how the themes work you may decide to devise your own. It takes quite a bit of time but is
relatively straighforward.





    
