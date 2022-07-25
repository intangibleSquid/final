"""
Program: Peter’s Pizza Palace – Priority order-Placement Program v1.0.0 (.py)
Author: Cameron Coy (ccoy2@ivytech.edu)
Description: This is the main module for the Peter's Pizza Palace - Priority order-Placement Program. It displays the
logo and gives the user the option to select between 'Delivery' or 'Carry-Out' for their order.
"""
# import statements
from myGUI import *
import size
from PIL import ImageTk, Image


# main function
def main():
    """main function / root window of the pizza ordering program"""

    # create program's root GUI window
    root = MyWindow("Peter's Pizza Palace - Priority order-Placement Program", '600x420')

    # create program's logo and welcome text
    logo = ImageTk.PhotoImage(Image.open('images/logo.png'))  # open logo image
    logo_label = MyLabel(root, 'logo', row=0, col=0, img=logo)  # place logo image
    welcome = MyLabel(root, "Welcome to Peter's Pizza Palace! Let's get started taking your order today!\n",
                      row=1, col=0,
                      font=('Helvetica', 14, 'bold', 'underline'))  # welcome text

    # order pick-up options
    pickup_label = MyLabel(root, "How would you like to receive your order today?", row=2, col=0)  # ask about pick-up
    pickup = IntVar()  # pick-up tkinter variable
    pickup_frame = MyFrame(root, row=3, col=0)  # frame to hold pick-up options
    delivery = MyRadio(pickup_frame, 'Delivery', row=0, col=1, var=pickup, val=0)  # delivery option
    carry = MyRadio(pickup_frame, 'Carry-Out', row=0, col=2, var=pickup, val=1)  # carry-out option

    # program navigation
    nav_frame = MyFrame(root, row=4, col=0)  # frame to hold nav buttons

    # 'start order' button's function
    def start_order():
        size.pizza_size(pickup)  # opens the 'pizza_size' window (size.py) (passes pickup to it)
    start_order = MyButton(nav_frame, "Start Order", row=0, col=0, command=start_order)  # 'start order' button

    # 'exit program' button's function
    def exit_prog():
        """closes the program when button is clicked"""
        root.quit()  # close the root GUI window
    close_root = MyButton(nav_frame, "Exit Program", row=0, col=1, command=exit_prog)

    # main GUI loop
    root.mainloop()


# main loop
if __name__ == '__main__':
    main()

