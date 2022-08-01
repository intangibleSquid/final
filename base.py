"""
Program: Peter’s Pizza Palace – Priority order-Placement Program v1.0.0 (.py)
Author: Cameron Coy (ccoy2@ivytech.edu)
Description: This is the base module for the Peter's Pizza Palace - Priority order-Placement Program. It allows the
user to either start with a base pizza or start customizing their pizza from scratch in a new pop-up Toplevel window.
"""
# import statements
from myGUI import *  # import my custom tkinter syntax
import pizza  # import next module (for next button)
import size  # import previous module (for back button)


# define 'pizza_base' function (to create a new 'pizza_base' window)
def pizza_base(pickup, p_size):
    """function to create a new window / determine if user wants to build pizza from template or start from scratch"""
    # create toplevel window
    base_window = NewWindow("Pizza's Base", '235x302')

    # 'pizza_base' label (select pre-made pizza)
    base_label = MyLabel(base_window, "Select a Pre-Made Pizza:", row=0, col=0,
                         font=('Helvetica', 14, 'bold', 'underline'))  # base label
    base_label.grid(sticky=W)  # force base_label to the right of the window

    # 'base_pizza' options (radio buttons)
    global p_base  # makes 'base' variable global (access across windows)
    p_base = IntVar()  # variable for base pizza selection
    base_frame = MyFrame(base_window, row=1, col=0)  # frame to hold radio button options
    base_cheese = MyRadio(base_frame, 'Cheese Pizza', row=0, col=0, sticky=W, var=p_base, val=0)  # radio button
    base_pepperoni = MyRadio(base_frame, 'Pepperoni Pizza', row=1, col=0, sticky=W, var=p_base, val=1)  # radio button
    base_sausage = MyRadio(base_frame, 'Sausage Pizza', row=2, col=0, sticky=W, var=p_base, val=2)  # radio button
    base_supreme = MyRadio(base_frame, 'Supreme Pizza', row=3, col=0, sticky=W, var=p_base, val=3)  # radio button
    base_meat = MyRadio(base_frame, 'Meat-za™ Pizza', row=4, col=0, sticky=W, var=p_base, val=4)  # radio button
    base_alfredo = MyRadio(base_frame, 'Chicken Alfredo Pizza', row=5, col=0, sticky=W, var=p_base, val=5)  # radio but
    base_hawaii = MyRadio(base_frame, 'Hawaiian Pizza', row=6, col=0, sticky=W, var=p_base, val=6)  # radio button
    base_bbq = MyRadio(base_frame, 'BBQ Chicken Pizza', row=7, col=0, sticky=W, var=p_base, val=7)  # radio button

    # 'scratch' label (create pizza from scratch)
    scratch_label = MyLabel(base_window, "Create Pizza from Scratch:", row=2, col=0,
                            font=('Helvetica', 14, 'bold', 'underline'), sticky=W)  # scratch_label
    scratch_label.grid(pady=(10, 0))  # give scratch_label padding (10px top)

    # 'scratch' option (radio button)
    no_base = MyRadio(base_window, 'Start From Scratch', row=3, col=0, sticky=W, var=p_base, val=8)  # radio button
    no_base.grid(padx=(36, 0))  # line up 'no_base' button with the buttons above

    # program navigation
    nav_frame = MyFrame(base_window, row=4, col=0)  # frame to hold navigation buttons
    nav_frame.grid(pady=(1, 0))  # give nav_frame some padding (1px top)

    # 'back' button function
    def back_base():
        """Loads the previous module and destroys the current window (also passes variables on to the that module)"""
        size.pizza_size(pickup)  # return to the previous module
        base_window.destroy()  # destroy this window

    # 'exit' button function
    def exit_base():
        """Exits the current window and resets variables"""
        p_size.set(0)  # reset 'size' variable (avoid weird behavior)
        p_base.set(0)  # reset 'base' variable (avoid weird behavior)
        base_window.destroy()  # destroy 'base_window' window

    # 'next' button function
    def next_pizza():
        """Loads the next module and destroys the current window (also passes variables on to the next module)"""
        base_window.destroy()  # destroy 'base_window' window
        pizza.customize_pizza(pickup, p_size, p_base.get())  # opens the 'customize_pizza' window (and passes variables)

    back_btn = MyButton(nav_frame, '<< Back', row=0, col=0, command=back_base)  # back button
    exit_btn = MyButton(nav_frame, 'EXIT', row=0, col=1, command=exit_base)  # exit button
    next_btn = MyButton(nav_frame, 'Next >>', row=0, col=2, command=next_pizza)  # next button
