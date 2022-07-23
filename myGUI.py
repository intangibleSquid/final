"""
Custom tkinter GUI classes
!!look into window icons (mac specific) and images in tkinter!!
"""
# import modules
from tkinter import *
# from tkinter import messagebox as mb


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

    Examples:
        f = MyLabelFrame(root, 'A Frame', row=1, col=0)
        f = MyLabelFrame(root, 'Tall Frame', row=1, col=1, rowspan=3, sticky=W+E)
    """
    def __init__(self, master, text, *, row, col, rowspan=1, colspan=1, sticky=None):
        LabelFrame.__init__(self, master)
        # self.master = master
        self['text'] = text
        self.grid(row=row,
                  column=col,
                  rowspan=rowspan,
                  columnspan=colspan,
                  sticky=sticky)


# frame class
class MyFrame(Frame):
    """Custom syntax for creating a tkinter Frame.

    Expected Positional Arguments:
        1. Frame's Parent Window
            master: str = root
        2. Frame's Label
            text: str = 'Button Frame'

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
        Button.__init__(self, master=parent)
        self['text'] = text
        self.command = command
        self.grid(row=row,
                  column=col,
                  rowspan=rowspan,
                  columnspan=colspan)


'''class MyLabel(Label):
    """Custom syntax for tkinter Labels"""
    def __init__(self, parent, text, row, column):'''