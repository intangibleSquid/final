"""
Program: Peter’s Pizza Palace – Priority order-Placement Program v1.0.0 (.py)
Author: Cameron Coy (ccoy2@ivytech.edu)
Description: This is the final module for the Peter's Pizza Palace - Priority order-Placement Program. It finalizes
your order by getting payment information and delivery address as well as confirming your order and timing you pickup
or delivery.
"""
# import statements
import payment  # import 'payment' module (for the 'back' nav button)
from myGUI import *  # import 'myGUI' module to create instances of my tkinter widgets (custom syntax)
import time  # import the time module (for delivery/pickup times)
from tkinter import messagebox as mb  # import messagebox for popup windows


# define 'finalize_order' function (to create 'finalize_order' window)
def finalize_order(pickup_selection, total_order_price):  # add passed variables (if anything pull prices from previous module and delivery questions etc)
    """Finalizes your order by calling a number of functions                    change me!       """

    # create new toplevel tkinter window
    global final_window  # make 'payment_window' object global
    final_window = NewWindow("Finalize Your Order", '660x170')  # create 'finalize order' window


    # define function to pay cash
    def pay_cash():
        """Function for the 'Pay Cash' option, opens popup window and moves to the next frame"""
        if pickup_selection == 0:  # delivery picup option
            delivery_popup = mb.askokcancel('Pay Cash', f'Please pay ${total_order_price} to your delivery driver when'
                                                        f' they arrive with your order!')  # pay cash / delivery popup
            if delivery_popup is True:  # if user pressed 'ok' on popup window
                get_payment_frame.destroy()  # destroy the last frame (get payment frame)
                get_delivery_info()  # get delivery information
                # (above add a force focus on new frame)
            else:
                get_payment_method()
                get_payment_frame.focus_force()

    # function to get delivery information
    def get_delivery_info():
        """Function to collect the user's delivery information"""
        final_window.geometry('600x600')
        # get delivery frame
        global get_delivery_frame  # make get delivery frame global
        get_delivery_frame = MyFrame(final_window, row=0, col=0, colspan=3)

        # build delivery collection above (don't forget the rest of the assignment!!)
        # reading!
        # document! also user manual and testing data
        # myGUI Entry class


    # define function to get payment method and relevant information (first frame of the module)
    def get_payment_method():
        """Function to get the user's payment method and collect relevant information"""
        # get payment frame
        global get_payment_frame  # make get payment frame global
        get_payment_frame = MyFrame(final_window, row=0, col=0, colspan=3)  # get payment frame
        get_payment_frame.grid(pady=(10, 0))  # get payment frame padding (10px top)
        # get payment heading
        get_payment_label = MyLabel(get_payment_frame, f'Total Price of Your Order: ${total_order_price}', row=0, col=0,
                                    font=('Helvetica', 18, 'bold', 'underline'))  # total price label
        get_payment_label['width'] = 60  # total price label width (60px)
        # get payment method
        get_payment_method_frame = MyLabelFrame(get_payment_frame, 'Select Payment Method:', row=1, col=0,
                                                font='Helvetica 14 bold')  # get payment method frame
        get_payment_method_frame.grid(pady=(10, 0), ipady=6, ipadx=10)  # give payment method frame padding
        cc_btn = MyButton(get_payment_method_frame, 'Credit/Debit Card', row=0, col=0)  # yes button
        cc_btn.grid(padx=(20, 0))  # give yes button padding (20px top)
        cash_btn = MyButton(get_payment_method_frame, 'Cash', row=0, col=1, command=pay_cash)  # no button
        cash_btn['width'] = 12  # make cash button same side as credit/debit button




    # navigation functions
    # 'back' button function
    def back_extras():
        """Loads the previous module and destroys the current window (also passes variables on to the that module)"""
        #pizza.customize_pizza(pickup, p_size, p_base, your_pizza)  # opens the 'customize_pizza' window (and passes variables)
        #extras_window.destroy()  # destroy this window
        pass

    # 'exit' button function
    def exit_extras():
        """Exits the current window and resets variables"""
        #p_size.set(0)  # reset 'size' variable (avoid weird behavior)
        #p_base = IntVar()  # resent p_base as a tkinter variable (instead of an integer, so it can be reset below)
        #p_base.set(0)  # reset 'base' variable (avoid weird behavior)
        #your_pizza = None  # reset 'your_pizza' variable (avoid weird behavior)
        #custom = False  # reset custom variable (avoid weird behavior)
        #changes = None  # reset changes variable (avoid weird behavior)
        #order = []  # reset order variable (avoid weird behavior)
        #extras_window.destroy()  # destroy 'extras' window
        pass

    # 'next' button function
    def next_payment():
        """Loads the next module and destroys the current window (also passes variables on to the next module)"""
        #extras_window.destroy()  # destroy this window
        #payment.pizza_payment()  # go to the next module
        pass

    # program navigation
    nav_frame = MyFrame(final_window, row=1, col=0, colspan=4, sticky=N+S)  # navigation frame
    nav_frame.grid(pady=(15, 0))  # nav frame padding (40px top)
    back_btn = MyButton(nav_frame, '<< Back', row=0, col=0, command=back_extras)  # back button
    exit_btn = MyButton(nav_frame, 'EXIT', row=0, col=1, command=exit_extras)  # exit button
    next_btn = MyButton(nav_frame, 'Next >>', row=0, col=2, command=next_payment)  # next button
    next_btn['state'] = DISABLED  # disable next button (until all selections are made)

    # testing statements
    get_payment_method()
    final_window.mainloop()


# testing statements
finalize_order(0, 20.99)

'''
# documentation
# button spacing and window size
# icons on mb windows

# when complete return original window and swap frames to 'thank you for your order!...'
# also go back through other modules and add prices to everything based on algorithm
# features to add eventually:
# update readme
# add costs to items
# cheese custom?
# document, document, document
# window title
# make functions and structure code
second or multiple pizza order options
quantity for side items / cart module

pizza.py to-do
# extra or half options?
# alt text / labels and non-viusual representation

payment.py
# logic to change window size based on receipt length

# myGUI.py
TO DO:
- [ ] look into window icons (mac specific) [error changing mac window icons]
- [ ] use logic checking to use window icons across all os / platforms
- [ ] look into images in tkinter (no PIL / external libraries)
- [ ] finish tkinter messagebox customizations (if needed)
'''