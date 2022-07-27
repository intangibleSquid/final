"""
Program: Peter’s Pizza Palace – Priority order-Placement Program v1.0.0 (.py)
Author: Cameron Coy (ccoy2@ivytech.edu)
Description: This is the payment module for the Peter's Pizza Palace - Priority order-Placement Program. It calculates
the cost of the user's pizza, handles the user's payment and delivery options and returns the user's receipt (as a
printable / savable file). This is the final module in the Peter's Pizza Palace- Priority order-Placement Program.
"""
# import statements
import pizza
from myGUI import *
from sqlite3 import *
# from PIL import ImageTk, Image


# define 'customize_pizza' function (to create new 'customize_pizza' window)
def pizza_payment(pickup, p_size, p_base, ingredient_list):
    payment_window = NewWindow("Pizza Payment Processing", '675x482')
    '''
    print(pickup.get())  # delivery = 0, carry-out = 1
    print(p_size.get())  # small = 0, medium = 1, large = 2, xl = 3
    print(p_base)  # int = dictionary from pizza.py
    print(your_pizza)  # list = based on p_base / customizations made (not reflected by p_base but here) from pizza.py
    '''
    return





'''
# when complete return original window and swap frames to 'thank you for your order!...'
# also go back through other modules and add prices to everything based on algorithm
# features to add eventually:
second or multiple pizza order options
quantity for side items / cart module
'''