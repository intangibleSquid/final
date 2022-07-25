"""
Program: Peter’s Pizza Palace – Priority order-Placement Program v1.0.0 (.py)
Author: Cameron Coy (ccoy2@ivytech.edu)
Description: This is the base module for the Peter's Pizza Palace - Priority order-Placement Program. It allows the
user to either start with a base pizza or start customizing their pizza from scratch in a new pop-up Toplevel window.
"""
# import statements
from myGUI import *
import pizza
import size


# define 'pizza_base' function (to create a new 'pizza_base' window)
def pizza_base(pickup, p_size):
    """function to create a new window / determine if user wants to build pizza from template or start from scratch"""
    # create toplevel window
    base_window = NewWindow("Pizza's Base", '235x302')

    # 'pizza_base' label (select pre-made pizza)
    base_label = MyLabel(base_window, "Select a Pre-Made Pizza:", row=0, col=0,
                         font=('Helvetica', 14, 'bold', 'underline'))
    base_label.grid(sticky=W)

    # 'base_pizza' options (radio buttons)
    global p_base  # makes 'base' variable global (access across windows)
    p_base = IntVar()  # variable for base pizza selection
    base_frame = MyFrame(base_window, row=1, col=0)  # frame to hold radio button options
    base_cheese = MyRadio(base_frame, 'Cheese Pizza', row=0, col=0, sticky=W, var=p_base, val=0)
    base_pepperoni = MyRadio(base_frame, 'Pepperoni Pizza', row=1, col=0, sticky=W, var=p_base, val=1)
    base_sausage = MyRadio(base_frame, 'Sausage Pizza', row=2, col=0, sticky=W, var=p_base, val=2)
    base_supreme = MyRadio(base_frame, 'Supreme Pizza', row=3, col=0, sticky=W, var=p_base, val=3)
    base_meat = MyRadio(base_frame, 'Meat-za™ Pizza', row=4, col=0, sticky=W, var=p_base, val=4)
    base_alfredo = MyRadio(base_frame, 'Chicken Alfredo Pizza', row=5, col=0, sticky=W, var=p_base, val=5)
    base_hawaii = MyRadio(base_frame, 'Hawaiian Pizza', row=6, col=0, sticky=W, var=p_base, val=6)
    base_bbq = MyRadio(base_frame, 'BBQ Chicken Pizza', row=7, col=0, sticky=W, var=p_base, val=7)

    # 'scratch' label (create pizza from scratch)
    scratch_label = MyLabel(base_window, "Create Pizza from Scratch:", row=2, col=0,
                            font=('Helvetica', 14, 'bold', 'underline'))
    scratch_label.grid(sticky=W, pady=(10, 0))

    # 'scratch' option (radio button)
    no_base = MyRadio(base_window, 'Start From Scratch', row=3, col=0, sticky=W, var=p_base, val=8)
    no_base.grid(padx=(36, 0))  # line up 'no_base' button with the buttons above

    # program navigation
    nav_frame = MyFrame(base_window, row=4, col=0)  # frame to hold navigation buttons
    nav_frame.grid(pady=(1, 0))

    # 'back' button function
    def back_base():
        size.pizza_size(pickup)
        base_window.destroy()

    # 'exit' button function
    def exit_base():
        p_size.set(0)  # reset 'size' variable (avoid weird behavior)
        p_base.set(0)  # reset 'base' variable (avoid weird behavior)
        base_window.destroy()  # destroy 'base_window' window

    # 'next' button function
    def next_pizza():
        base_window.destroy()  # destroy 'base_window' window
        pizza.customize_pizza(pickup, p_size, p_base)  # opens the 'customize_pizza' window (passes variables to it)

    back_btn = MyButton(nav_frame, '<< Back', row=0, col=0, command=back_base)
    exit_btn = MyButton(nav_frame, 'EXIT', row=0, col=1, command=exit_base)
    next_btn = MyButton(nav_frame, 'Next >>', row=0, col=2, command=next_pizza)
