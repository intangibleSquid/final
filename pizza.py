"""
Program: Peter’s Pizza Palace – Priority order-Placement Program v1.0.0 (.py)
Author: Cameron Coy (ccoy2@ivytech.edu)
Description: This is the pizza module for the Peter's Pizza Palace - Priority order-Placement Program. It allows the
user to customize their pizza order as well as selecting from a number of pre-made pizzas.
"""
# import statements
from myGUI import *
from PIL import ImageTk, Image


# define 'customize_pizza' function (to create new 'customize_pizza' window)
def customize_pizza(pickup, p_size, p_base):
    """function to create a new window (pizza customization window)"""
    # create toplevel window
    pizza_window = NewWindow("Create Your Masterpie-zza", '400x400')









    # pizza_window.mainloop()

# customize_pizza(1, 2, 3)

"""

premade_frame = MyFrame(order, row=0, col=0, rowspan=3)
custom_label = MyLabel(premade_frame, "--Customize Your Pizza Here--", row=0, col=0, font='Helvetica 22 bold')
custom_label.grid(pady=(2, 6))  # put 2px space above and 4px space below 'custom_label'
base_label = MyLabel(premade_frame, "Would you like to start with a base pizza template?", row=1, col=0)
base_label.grid(pady=(0, 4))  # put 4px space below 'base_label'

base_frame = MyLabelFrame(premade_frame, "Base Pizza Template", row=2, col=0, sticky=W+E)
base = IntVar()
base_cheese = MyRadio(base_frame, 'Cheese Pizza', row=0, col=0, sticky=W, var=base, val=0)
base_pepperoni = MyRadio(base_frame, 'Pepperoni Pizza', row=1, col=0, sticky=W, var=base, val=1)
base_sausage = MyRadio(base_frame, 'Sausage Pizza', row=2, col=0, sticky=W, var=base, val=2)
base_supreme = MyRadio(base_frame, 'Supreme Pizza', row=3, col=0, sticky=W, var=base, val=3)
base_meat = MyRadio(base_frame, 'Meat-za™ Pizza', row=4, col=0, sticky=W, var=base, val=4)
base_alfredo = MyRadio(base_frame, 'Chicken Alfredo Pizza', row=5, col=0, sticky=W, var=base, val=5)
base_hawaii = MyRadio(base_frame, 'Hawaiian Pizza', row=6, col=0, sticky=W, var=base, val=6)
base_bbq = MyRadio(base_frame, 'BBQ Chicken Pizza', row=7, col=0, sticky=W, var=base, val=7)


size_frame = MyLabelFrame(order, "Pizza's Size", row=0, col=1, sticky=W+E)
size_frame.grid(pady=(1, 0))
size = IntVar()
sm = MyRadio(size_frame, 'Small (10") - 6-Slices', row=0, col=0, sticky=W, var=size, val=0)
med = MyRadio(size_frame, 'Medium (14") - 8-Slices', row=1, col=0, sticky=W, var=size, val=1)
lrg = MyRadio(size_frame, 'Large (16") - 10-Slices', row=2, col=0, sticky=W, var=size, val=2)
xl = MyRadio(size_frame, 'XL (19") - 12-Slices', row=3, col=0, var=size, sticky=W, val=3)

crust_frame = MyLabelFrame(order, "Pizza's Crust", row=1, col=1, sticky=W+E)
crust = IntVar()
hand = MyRadio(crust_frame, 'Hand Tossed', row=0, col=0, sticky=W, var=crust, val=0)
thin = MyRadio(crust_frame, 'Thin & Crispy', row=1, col=0, sticky=W, var=crust, val=1)

sauce_frame = MyLabelFrame(order, "Pizza's Sauce", row=2, col=1, sticky=W+E)
sauce = IntVar()
red = MyRadio(sauce_frame, "Red Sauce", row=0, col=0, sticky=W, var=sauce, val=0)
alfredo = MyRadio(sauce_frame, "Alfredo Sauce", row=1, col=0, sticky=W, var=sauce, val=1)
bbq = MyRadio(sauce_frame, "BBQ Sauce", row=2, col=0, sticky=W, var=sauce, val=2)



order.mainloop()
"""