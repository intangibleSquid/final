"""
Custom tkinter GUI classes for easier calls to tkinter widgets from my own programs.
Integrated tkinter's Grid Geometry manager into most widgets for a one-line widget placement and creation.
Only used the most frequently called attributes, others can be edited individually in the modules.
"""
# import modules
from tkinter import *  # import tkinter


# window class
class MyWindow(Tk):
    """Custom syntax for creating a tkinter Window.

    Expected Arguments:
        1. Window's Title
            title: str = 'Root Window'
        2. Window's Dimensions
            size: str = '400x400'

    Optional Arguments:
        3. Window's Icon
            icon: str = '/path/to/ico/icon.ico'

    Examples:
        w = MyWindow('My Window", 600x600')
        w = MyWindow('Root Window', '400x440', 'icon.ico')
    """
    def __init__(self, title, size, icon=None):
        Tk.__init__(self)
        self.title(title)
        self.geometry(size)
        self.iconbitmap(icon)


# toplevel class
class NewWindow(Toplevel):
    """Custom syntax for creating a tkinter Toplevel Window (New Window).

    Expected Arguments:
        1. Window's Title
            title: str = 'Root Window'
        2. Window's Dimensions
            size: str = '400x400'

    Optional Arguments:
        3. Window's Icon
            icon: str = '/path/to/ico/icon.ico'

    Examples:
        w = NewWindow('My Window", 600x600')
        w = NewWindow('Root Window', '400x440', 'icon.ico')
    """
    def __init__(self, title, size, icon=None):
        Toplevel.__init__(self)
        self.title(title)
        self.geometry(size)
        self.iconbitmap(icon)


# label frame class
class MyLabelFrame(LabelFrame):
    """Custom syntax for creating a tkinter LabelFrame.

    Expected Positional Arguments:
        1. LabelFrame's Parent Window
            master: str = root
        2. LabelFrame's Label
            text: str = 'Results Frame'

    Expected Keyword Arguments:
        row= LabelFrame's Grid Row
            row: int = 0
        col= LabelFrame's Grid Column
            col: int = 0

    Optional Keyword Arguments:
        rowspan= LabelFrame's Grid Rowspan
            rowspan: int = 1
        colspan= LabelFrame's Grid Columnspan
            colspan: int = 1
        sticky= LabelFrame's Grid Sticky Option
            sticky: str = N+S+W+E
        bd= LabelFrame's Border Width (Default = 2)
            bd: int = 2
        font= LabelFrame's Font Options
            font: str | tuple = 'Helvetica 16 bold'
        padx= LabelFrame's Grid X-Axis Padding
            padx: int | tuple = (10, 2)
        pady= LabelFrame's Grid Y-Axis Padding
            pady: int | tuple = 15

    Examples:
        f = MyLabelFrame(root, 'A Frame', row=1, col=0)
        f = MyLabelFrame(root, 'Tall Frame', row=1, col=1, rowspan=3, sticky=W+E)
    """
    def __init__(self, master, text, *, row, col, rowspan=1, colspan=1, sticky=None, bd=None, font=None, padx=None,
                 pady=None):
        LabelFrame.__init__(self, master)
        # self.master = master
        self['text'] = text
        self['bd'] = bd
        self['font'] = font
        self.grid(row=row,
                  column=col,
                  rowspan=rowspan,
                  columnspan=colspan,
                  sticky=sticky,
                  padx=padx,
                  pady=pady)


# frame class
class MyFrame(Frame):
    """Custom syntax for creating a tkinter Frame.

    Expected Positional Arguments:
        1. Frame's Parent Window
            master: str = root

    Expected Keyword Arguments:
        row= Frame's Grid Row
            row: int = 0
        col= Frame's Grid Column
            col: int = 0

    Optional Keyword Arguments:
        rowspan= Frame's Grid Rowspan
            rowspan: int = 1
        colspan= Frame's Grid Columnspan
            colspan: int = 1
        sticky= Frame's Grid Sticky Option
            sticky: str = N+S+W+E

    Examples:
        f = MyFrame(root, 'Button Frame', row=2, col=2)
        f = MyFrame(root, 'Long Frame', row=3, col=0, colspan=4)
    """
    def __init__(self, master, *, row, col, rowspan=1, colspan=1, sticky=None):
        Frame.__init__(self, master)
        self.grid(row=row,
                  column=col,
                  rowspan=rowspan,
                  columnspan=colspan,
                  sticky=sticky)


# button class
class MyButton(Button):
    """Custom syntax for creating a tkinter Button.

    Expected Positional Arguments:
        1. Button's Parent Window / Frame
            parent: str = button_frame
        2. Button's Label
            text: str = 'Click Me!'

    Expected Keyword Arguments:
        row= Button's Grid Row
            row: int = 0
        col= Button's Grid Column
            col: int = 0

    Optional Keyword Arguments:
        rowspan= Button's Grid Rowspan
            rowspan: int = 1
        colspan= Button's Grid Columnspan
            colspan: int = 1
        command= Button's Function / Method
            command: str = click

    Examples:
        b = MyButton(button_frame, 'Click Me!', row=1, col=0, command=click)
        b = MyButton(root, 'Exit', row=5, col=0, rowspan=3, command=close)
    """
    def __init__(self, parent, text, *, row, col, rowspan=1, colspan=1, command=None):
        Button.__init__(self, parent)
        self['text'] = text
        self['command'] = command
        self.grid(row=row,
                  column=col,
                  rowspan=rowspan,
                  columnspan=colspan)


# label class
class MyLabel(Label):
    """Custom syntax for creating a tkinter Label.

    Expected Positional Arguments:
        1. Label's Parent Window / Frame
            parent: str = root
        2. Label's Text
            text: str = 'I'm a Label'

    Expected Keyword Arguments:
        row= Label's Grid Row
            row: int = 0
        col= Label's Grid Column
            col: int = 0

    Optional Keyword Arguments:
        rowspan= Label's Grid Rowspan
            rowspan: int = 1
        colspan= Label's Grid Columnspan
            colspan: int = 1
        var= Label Text's Control Variable (StringVar)
            var: str = tkvar
        img= Label's Static Image
            img: str = '/path/to/img/image.png'
        font= Label's Font Settings
            font: str = 'Helvetica 18 bold'
        sticky= Label's Sticky Option
            sticky: str = N+S+W+E

    Examples:
        l = MyLabel(main_frame, 'label text', row=1, col=0
        l = MyLabel(main_frame, 'image', row=0, col=0, img='images/img.png')
    """
    def __init__(self, parent, text, *, row, col, rowspan=1, colspan=1, var=None, img=None, font=None, sticky=None):
        Label.__init__(self, parent)
        self['text'] = text
        self['textvariable'] = var
        self['image'] = img
        self['font'] = font
        self.grid(row=row,
                  column=col,
                  rowspan=rowspan,
                  columnspan=colspan,
                  sticky=sticky)


# radiobutton class
class MyRadio(Radiobutton):
    """Custom syntax for creating a tkinter Radio Button.

    Expected Positional Arguments:
        1. Radio Button's Parent Window / Frame
            parent: str = root
        2. Radio Button's Text
            text: str = 'I'm a Radio Button'

    Expected Keyword Arguments:
        row= Radio Button's Grid Row
            row: int = 0
        col= Radio Button's Grid Column
            col: int = 0

    Optional Keyword Arguments:
        rowspan= Radio Button's Grid Rowspan
            rowspan: int = 1
        colspan= Radio Button's Grid Columnspan
            colspan: int = 1
        sticky= Radio Button's Grid Sticky Option
            sticky: str = N+S+W+E
        var= Radio Button's Control Variable (StringVar or IntVar)
            var: str = tkvar
        val= Radio Button's Control Variable's Value
            val: str | int = 'selection' | 1
        command= Radio Button's Function / Method
            command: str = refresh

    Examples:
        r = MyRadio(main_frame, 'Radio Button', row=2, col=0, sticky=W, var=variable, val=1)
        r = MyRadio(main_frame, 'Radio Button', row=2, col=0, var=variable, val=2)
    """
    def __init__(self, parent, text, *, row, col, rowspan=1, colspan=1, sticky=None, var=None, val=None, command=None):
        Radiobutton.__init__(self, parent)
        self['text'] = text
        self['variable'] = var
        self['value'] = val
        self['command'] = command
        self.grid(row=row,
                  column=col,
                  rowspan=rowspan,
                  columnspan=colspan,
                  sticky=sticky)


# checkbutton class
class MyCheck(Checkbutton):
    """Custom syntax for creating a tkinter Check Button.

    Expected Positional Arguments:
        1. Check Button's Parent Window / Frame
            parent: str = root
        2. Check Button's Text
            text: str = 'I'm a Radio Button'

    Expected Keyword Arguments:
        row= Check Button's Grid Row
            row: int = 0
        col= Check Button's Grid Column
            col: int = 0

    Optional Keyword Arguments:
        rowspan= Check Button's Grid Rowspan
            rowspan: int = 1
        colspan= Check Button's Grid Columnspan
            colspan: int = 1
        var= Check Button's Control Variable (StringVar or IntVar)
            var: str = tkvar
        on= Check Button's Control Variable's 'On' Value
            on: str | int = 'selection' | 1
        command= Check Button's Function / Method
            command: str = refresh

    Examples:
        c = MyCheck(main_frame, 'Check Button', row=3, col=0, var=variable, on='option1')
        c = MyCheck(main_frame, 'Check Button', row=3, col=0, var=variable, on='option2')
    """
    def __init__(self, parent, text, *, row, col, rowspan=1, colspan=1, sticky=None, var=None, on=None, command=None):
        Checkbutton.__init__(self, parent)
        self['text'] = text
        self['variable'] = var
        self['onvalue'] = on
        self['command'] = command
        self.grid(row=row,
                  column=col,
                  rowspan=rowspan,
                  columnspan=colspan,
                  sticky=sticky)


# textbox class
class MyText(Text):
    """Custom syntax for creating a tkinter Textarea.

    Expected Positional Arguments:
        1. Textarea's Parent Window / Frame
            parent: str = root

    Expected Keyword Arguments:
        height= Textarea's Height
            height: int = 0
        width= Textarea's Width
            width: int = 0
        row= Textarea's Grid Row
            row: int = 0
        col= Textarea's Grid Column
            col: int = 0

    Optional Keyword Arguments:
        rowspan= Textarea's Grid Rowspan
            rowspan: int = 1
        colspan= Textarea's Grid Columnspan
            colspan: int = 1
        sticky= Textarea's Grid Sticky Option
            sticky: str = N+S+W+E
        state= Textarea's State
            state: keyword = NORMAL

    Examples:
        t = MyText(root, height=10, width=100, row=0, col=0)
        t = MyText(root, height=5, width=500, row=1, col=0, state=DISABLED)
    """
    def __init__(self, parent, *, height, width, row, col, rowspan=1, colspan=1, sticky=None, state=NORMAL):
        Text.__init__(self, parent)
        self['height'] = height
        self['width'] = width
        self['state'] = state
        self.grid(row=row,
                  column=col,
                  rowspan=rowspan,
                  columnspan=colspan,
                  sticky=sticky)


# entry widget class
class MyEntry(Entry):
    """Custom syntax for creating a tkinter Entry widget.

    Expected Positional Arguments:
        1. Entry Widgets's Parent Window / Frame
            parent: str = root

    Expected Keyword Arguments:
        var= Entry Widget's Textvariable
            var: str = tkvar
        width= Entry Widgets's Width
            width: int = 0
        row= Entry Widgets's Grid Row
            row: int = 0
        col= Entry Widgets's Grid Column
            col: int = 0

    Optional Keyword Arguments:
        rowspan= Entry Widgets's Grid Rowspan
            rowspan: int = 1
        colspan= Entry Widgets's Grid Columnspan
            colspan: int = 1
        sticky= Entry Widgets's Grid Sticky Option
            sticky: str = N+S+W+E
        state= Entry Widgets's State
            state: keyword = NORMAL

    Examples:
        e = MyEntry(root, var=tkStringVar, width=100, row=0, col=0)
        e = MyEntry(root, var=tkStringVar, width=100, row=0, col=1, state=DISABLED)
    """
    def __init__(self, parent, *, var, width, row, col, rowspan=1, colspan=1, sticky=None, state=NORMAL):
        Entry.__init__(self, parent)
        self['textvariable'] = var
        self['width'] = width
        self['state'] = state
        self.grid(row=row,
                  column=col,
                  rowspan=rowspan,
                  columnspan=colspan,
                  sticky=sticky)
