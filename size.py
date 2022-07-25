"""
Program: Peter’s Pizza Palace – Priority order-Placement Program v1.0.0 (.py)
Author: Cameron Coy (ccoy2@ivytech.edu)
Description: This is the size module for the Peter's Pizza Palace - Priority order-Placement Program. It allows the
user to select the size of their pizza in a new pop-up Toplevel window.
"""
# import statements
from myGUI import *
import base


# define 'pizza_size' function (to create a new 'pizza_size' window)
def pizza_size(pickup):
    """function to create a new window / get the pizza's size from the user"""
    # create toplevel window
    size_window = NewWindow("Pizza's Size", '235x150')

    # 'pizza_size' label
    size_label = MyLabel(size_window, "Select your pizza's size:", row=0, col=0,
                         font=('Helvetica', 14, 'bold', 'underline'))
    size_label.grid(sticky=W)

    # 'pizza_size' options (radio buttons)
    global p_size  # makes 'size' variable global (access across windows)
    p_size = IntVar()  # variable for pizza size
    options_frame = MyFrame(size_window, row=1, col=0)  # frame to hold radio button options
    sm = MyRadio(options_frame, 'Small (10") - 6 Slices', row=0, col=0, sticky=W, var=p_size, val=0)
    med = MyRadio(options_frame, 'Medium (14") - 8 Slices', row=1, col=0, sticky=W, var=p_size, val=1)
    lrg = MyRadio(options_frame, 'Large (16") - 10 Slices', row=2, col=0, sticky=W, var=p_size, val=2)
    xl = MyRadio(options_frame, 'XL (19") - 12 Slices', row=3, col=0, var=p_size, sticky=W, val=3)

    # program navigation
    nav_frame = MyFrame(size_window, row=2, col=0)  # frame to hold navigation buttons

    # 'exit' button function
    def exit_size():
        p_size.set(0)  # reset 'size' variable (avoid weird behavior)
        size_window.destroy()  # destroy 'size_window' window

    # 'next' button function
    def next_base():
        size_window.destroy()  # destroy 'size_window' window
        base.pizza_base(pickup, p_size)  # opens the 'pizza_base' window (base.py) (passing variables to it)

    back_btn = MyButton(nav_frame, '<< Back', row=0, col=0)
    back_btn['state'] = DISABLED  # disabled back button (there's nothing before this window) [also no command]
    exit_btn = MyButton(nav_frame, 'EXIT', row=0, col=1, command=exit_size)
    next_btn = MyButton(nav_frame, 'Next >>', row=0, col=2, command=next_base)
