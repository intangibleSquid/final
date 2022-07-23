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


'''
[-] Second Status Report To-Do List:
    1.	[-] Assignment Submission Components:
        a.	[-] Word Document:
            i.	[-] Document Your Project Progress:
                1.	[-] What Have You Completed?
                2.	[-] What Problems Have You Had?
                3.	[-] What Is Your Next Step?
        b.	[-] ZIP File:
            i.	[-] Compressed Project Folder (.zip)
            ii.	[-] Submission File / Folder Contents: 
                1.	[-] Current Project Progress
                2.	[-] Project Files
                3.	[-] Documentation
                4.	[-] Project Assets and Dependencies
        c.	[-] GitHub Link:
            i.	[-] Create GitHub Repository
                #1.	[+] https://github.com/ (External Site)
            ii.	[-] Upload Project Files
            iii.	[-] Upload Project Documentation

[-] Final Project To-Do List:
    1.	[-] Application Specifications:
        a.	[+] Tkinter GUI
        b.	[-] Modular Design
        c.	[-] Consistent / Clear Navigation
        d.	[-] Minimum Component Specifications:
            i.	[-] 2 Windows
            ii.	[-] 2 Images (with Alternate Text)
            iii.	[-] 3 Labels
            iv.	[-] 3 Buttons
            v.	[-] 3 Call Back Functions (with Each Button)
            vi.	[-] Exit Button
    2.	[-] Secure Coding Best Practices:
        a.	[-] Input Validation: 
            i.	[-] Data Types
            ii.	[-] Entry Box Not Empty
            iii.	[-] Etc.
    3.	[-] Validation Testing:
        a.	[-] Test Data Set (to Fully Validate Program):
        i.	[-] Data Sets Tested Against
        ii.	[-] Brief Written Explanation of Test Results / What You Fixed
        iii.	[-] Screen Shots of Good Test Data Working
    4.	[-] Documentation:
        a.	[-] User Manual:
        i.	[-] Write / Submit User Manual for Final Project 
        ii.	[-] Submit Manual According to Instructions (in Attached File)
        b.	[-] Source Code:
        i.	[-] Fully Document (Comment) Corrected Python Tkinter Source Code 
        ii.	[-] Appropriate Comments Including:
        1.	[-] Brief Explanation of the Purpose of Each Module (Sub) at the Beginning of Each Sub
        a.	[-] Header's Comment
        2.	[-] Explanation of Purpose of Each Variable Where it is Declared
        a.	[-] End Line Comment
        3.	[-] Line By Line (or Section by Section) Comments Within Code
        a.	[-] Explain What the Line/Section Does 
        c.	[-] GitHub Repository:
        i.	[-] Upload Project Files
        ii.	[-] Upload Documentation
        iii.	[-] Link to Repo on Assignment Submission
'''