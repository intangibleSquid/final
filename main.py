"""
Program: Peter’s Pizza Palace – Priority order-Placement Program v1.0.0 (.py)
Author: Cameron Coy (ccoy2@ivytech.edu)
Description:
"""
# import statements
from myGUI import *
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
                      row=1, col=0)  # welcome text

    # order pick-up options
    pickup = MyLabel(root, "How would you like to receive your order today?", row=2, col=0)  # ask about pick-up
    pickup_frame = MyFrame(root, row=3, col=0)  # frame to hold pick-up options
    delivery = MyRadio(pickup_frame, 'Delivery', row=0, col=1)  # delivery option
    carry = MyRadio(pickup_frame, 'Carry-Out', row=0, col=2)  # carry-out option

    # program navigation
    nav_frame = MyFrame(root, row=4, col=0)  # frame to hold nav buttons

    # 'start order' button's function
    def start_order():
        return
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

