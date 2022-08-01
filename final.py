"""
Program: Peter’s Pizza Palace – Priority order-Placement Program v1.0.0 (.py)
Author: Cameron Coy (ccoy2@ivytech.edu)
Description: This is the final module for the Peter's Pizza Palace - Priority order-Placement Program. It finalizes
your order by getting payment information and delivery address as well as confirming your order and timing you pickup
or delivery.
"""
# import statements
from myGUI import *  # import 'myGUI' module to create instances of my tkinter widgets (custom syntax)
from datetime import datetime, timedelta  # import the time module (for delivery/pickup times)
from tkinter import messagebox as mb  # import messagebox for popup windows


# define 'finalize_order' function (to create 'finalize_order' window)
def finalize_order(pickup_selection, total_order_price):
    """Finalizes your order by determining your payment method, collecting your payment and delivery information and
    calculating the time of your delivery/pickup"""

    # create new toplevel tkinter window
    global final_window  # make 'payment_window' object global
    final_window = NewWindow("Finalize Your Order", '660x170')  # create 'finalize order' window

    # define function for 'back' button throughout the program
    def back_button(current, cc_info=None):
        """Returns to the previous frame on 'back' button press"""
        if current == 'Card Info':  # coming from the Card Info frame
            get_card_frame.destroy()  # destroy current frame
            final_window.geometry('660x170')  # reset the window size
            get_payment_method()  # load get payment method (previous frame)
        if current == 'Delivery Info':  # coming from Delivery Info
            get_delivery_frame.destroy()  # destroy current frame
            if not cc_info:  # user didn't enter card info (clicked cash payment)
                final_window.geometry('660x170')  # reset the window size
                get_payment_method()  # load get payment method (previous frame)
            else:  # user did enter card info (coming from that frame)
                get_card_info()  # load the previous frame (get card info)
                card_name_entry.focus_force()  # force focus on the card name entry field in the new window (global)

    # define function to pay cash
    def pay_cash():
        """Function for the 'Pay Cash' option, opens popup window and moves to the next frame"""
        frame = 'Pay Cash'  # frame name Pay Cash
        if pickup_selection == 0:  # delivery picup option
            delivery_popup = mb.askokcancel('Pay Cash', f'Please pay ${total_order_price} to your delivery driver when'
                                                        f' they arrive with your order!')  # pay cash / delivery popup
            if delivery_popup is True:  # if user pressed 'ok' on popup window
                get_payment_frame.destroy()  # destroy the last frame (get payment frame)
                get_delivery_info()  # get delivery information
                # (above add a force focus on new frame)
            else:  # if the user pressed Cancel on the popup window
                get_payment_frame.destroy()  # destroy the get payment frame (to avoid a weird glitch if you don't)
                get_payment_method()  # relaunch to the original window
                get_payment_frame.focus_force()  # force focus on original frame (popup unfocused window)
        else:
            pickup_popup = mb.askokcancel('Pay Cash', f'Please pay ${total_order_price} when you pickup your order!')
            if pickup_popup is True:  # if user pressed 'ok' on popup window
                get_payment_frame.destroy()  # destroy the last frame (get payment frame)
                create_final_frame(frame)  # proceed to final frame
            else:  # if the user pressed Cancel on the popup window
                get_payment_frame.destroy()  # destroy the get payment frame (to avoid a weird glitch if you don't)
                get_payment_method()  # relaunch to the original window
                get_payment_frame.focus_force()  # force focus on original frame (popup unfocused window)

    # define function to create the final frame
    def create_final_frame(current, deliver_info=None, cc_info=None):
        """Creates the final frame and displays pickup/delivery times as well as price and payment/address info"""
        if current == 'Delivery Info':  # if you're coming from Delivery Info (delivery)
            get_delivery_frame.destroy()  # destroy current frame
            if cc_info is None:  # if you payed cash
                final_window.geometry('310x400')  # set window size (no card info to show)
            else:  # if you payed with a card
                final_window.geometry('310x510')  # set window size (space for card info)
        elif current == 'Card Info':  # if you came from Card Info (carry out)
            get_card_frame.destroy()  # destroy current frame
            final_window.geometry('310x320')  # set window size
        elif current == 'Pay Cash':  # if you payed cash from the beginning and it's carry out
            final_window.geometry('310x200')  # set window size
            final_window.focus_force()  # force focus on this window (popup unfocused window)

        # create final frame
        global final_frame  # make final frame global
        final_frame = MyFrame(final_window, row=0, col=0, colspan=3)  # create final frame
        final_frame.grid(padx=(4, 0))  # give final frame padding (4px left)
        if deliver_info is not None:  # if there's a delivery address to display
            # heading
            deliver_to = MyLabel(final_frame, 'Delivery Address:', row=0, col=0, sticky=W,
                                 font=('Helvetica', 16, 'bold', 'underline'))  # delivery address heading
            # delivery information
            delivery_info_frame = MyFrame(final_frame, row=1, col=0, colspan=2)  # delivery info frame
            # name
            name_info_label = MyLabel(delivery_info_frame, "Name", row=0, col=0)  # name label
            name_info = StringVar()  # name variable
            name_info_entry = MyEntry(delivery_info_frame, var=name_info, row=0, col=1)  # name entry box
            name_info.set(deliver_info[0])  # populate field
            name_info_entry['state'] = DISABLED  # make field DISABLED
            # address line 1
            address1_info_label = MyLabel(delivery_info_frame, "Address", row=1, col=0)  # address1 label
            address1_info = StringVar()  # address1 variable
            address1_info_entry = MyEntry(delivery_info_frame, var=address1_info, row=1, col=1)  # address1 entry box
            address1_info.set(deliver_info[1])  # populate field
            address1_info_entry['state'] = DISABLED  # make field DISABLED
            # address line 2
            address2_info_label = MyLabel(delivery_info_frame, "Address", row=2, col=0)  # address2 label
            address2_info = StringVar()  # address2 variable
            address2_info_entry = MyEntry(delivery_info_frame, var=address2_info, row=2, col=1)  # address2 entry box
            address2_info.set(deliver_info[2])  # populate field
            address2_info_entry['state'] = DISABLED  # make field DISABLED
            # city
            city_info_label = MyLabel(delivery_info_frame, "City", row=3, col=0)  # city label
            city_info = StringVar()  # city variable
            city_info_entry = MyEntry(delivery_info_frame, var=city_info, row=3, col=1)  # city entry box
            city_info.set(deliver_info[3])  # populate field
            city_info_entry['state'] = DISABLED  # make field DISABLED
            # state
            state_info_label = MyLabel(delivery_info_frame, "State", row=4, col=0)  # state label
            state_info = StringVar()  # state variable
            state_info_entry = MyEntry(delivery_info_frame, var=state_info, row=4, col=1)  # state entry box
            state_info.set(deliver_info[4])  # populate field
            state_info_entry['state'] = DISABLED  # make field DISABLED
            # zipcode
            zipcode_info_label = MyLabel(delivery_info_frame, "Zipcode", row=5, col=0)  # zipcode label
            zipcode_info = StringVar()  # zipcode variable
            zipcode_info_entry = MyEntry(delivery_info_frame, var=zipcode_info, row=5, col=1)  # zipcode entry box
            zipcode_info.set(deliver_info[5])  # populate field
            zipcode_info_entry['state'] = DISABLED  # make field DISABLED

        # payment information
        # heading
        deliver_to = MyLabel(final_frame, 'Payment Information:', row=2, col=0, sticky=W,
                             font=('Helvetica', 16, 'bold', 'underline'))  # payment information heading
        deliver_to.grid(pady=(6, 0))  # give payment info heading padding (6px top)
        # delivery information
        payment_info_frame = MyFrame(final_frame, row=3, col=0, colspan=2)  # payment info frame
        # order cost
        payment_price_info_label = MyLabel(payment_info_frame, "Order Price", row=0, col=0)  # price label
        payment_price_info = StringVar()  # price variable
        payment_price_info_entry = MyEntry(payment_info_frame, var=payment_price_info, row=0, col=1)  # price entry
        payment_price_info.set(f'${total_order_price}')  # set price to order total
        payment_price_info_entry['state'] = DISABLED  # make price entry DISABLED
        # payment type
        payment_info_label = MyLabel(payment_info_frame, "Payment Method", row=1, col=0)  # payment method heading
        payment_info = StringVar()  # payment method variable
        payment_info_entry = MyEntry(payment_info_frame, var=payment_info, row=1, col=1)  # payment method entry
        if cc_info is None:  # if you payed cash
            payment_info.set('Cash')  # place 'Cash' in the payment method entry field
            payment_info_entry['state'] = DISABLED  # make field DISABLED
        else:  # if you payed with a card
            payment_info.set('Credit/Debit Card')  # insert text into payment method field
            payment_info_entry['state'] = DISABLED  # make field DISABLED
            # card information
            # card name
            cc_name_info_label = MyLabel(payment_info_frame, "Name on Card", row=2, col=0)  # card name label
            cc_name_info = StringVar()  # card name variable
            cc_name_info_entry = MyEntry(payment_info_frame, var=cc_name_info, row=2, col=1)  # card name entry
            cc_name_info.set(cc_info[0])  # populate entry field
            cc_name_info_entry['state'] = DISABLED  # disable entry field
            # card number
            cc_number_info_label = MyLabel(payment_info_frame, "Card Number", row=3, col=0)  # card number label
            cc_number_info = StringVar()  # card number variable
            cc_number_info_entry = MyEntry(payment_info_frame, var=cc_number_info, row=3, col=1)  # card number entry
            cc_number_info.set(cc_info[1])  # populate entry field
            cc_number_info_entry['state'] = DISABLED  # disable entry field
            # card expire
            cc_expire_info_label = MyLabel(payment_info_frame, "Expiration Date", row=4, col=0)  # card expire label
            cc_expire_info = StringVar()  # card expire variable
            cc_expire_info_entry = MyEntry(payment_info_frame, var=cc_expire_info, row=4, col=1)  # card expire entry
            cc_expire_info.set(cc_info[2])  # populate entry field
            cc_expire_info_entry['state'] = DISABLED  # disable entry field
            # card cvv
            cc_cvv_info_label = MyLabel(payment_info_frame, "CVV #", row=5, col=0)  # card cvv label
            cc_cvv_info = StringVar()  # card cvv variable
            cc_cvv_info_entry = MyEntry(payment_info_frame, var=cc_cvv_info, row=5, col=1)  # card cvv entry
            cc_cvv_info.set(cc_info[3])  # populate entry field
            cc_cvv_info_entry['state'] = DISABLED  # disable entry field

        # calculate pickup/delivery times
        if pickup_selection == 0:  # delivery
            # delivery time information
            # heading
            delivery_time = MyLabel(final_frame, 'Time of Delivery:', row=4, col=0, sticky=W,
                                    font=('Helvetica', 16, 'bold', 'underline'))  # time of delivery heading
            delivery_time.grid(pady=(6, 0))  # give heading padding (6px top)
            # delivery information
            time_info_frame = MyFrame(final_frame, row=5, col=0, colspan=2)  # time information frame
            # calculate delivery time
            raw_tod = datetime.now() + timedelta(minutes=45)  # add 45 minutes to the current time
            time_of_delivery = format(raw_tod, '%H:%M:%S')  # format the time to be Hours:Minutes:Seconds
            # delivery time
            time_info_label = MyLabel(time_info_frame, "Delivery Time", row=0, col=0)  # delivery time label
            time_info = StringVar()  # delivery time variable
            time_info_entry = MyEntry(time_info_frame, var=time_info, row=0, col=1)  # delivery time entry field
            time_info.set(str(time_of_delivery))  # insert delivery time into field
            time_info_entry['state'] = DISABLED  # disable field
        else:  # pickup
            # pickup time information
            # heading
            pickup_time = MyLabel(final_frame, 'Time of Pickup:', row=4, col=0, sticky=W,
                                  font=('Helvetica', 16, 'bold', 'underline'))  # time of pickup heading
            pickup_time.grid(pady=(6, 0))  # give heading padding (6px top)
            # pickup information
            time_info_frame = MyFrame(final_frame, row=5, col=0, colspan=2)  # time info frame
            # calculate pickup time
            raw_top = datetime.now() + timedelta(minutes=30)  # add 30 minutes to the current time
            time_of_pickup = format(raw_top, '%H:%M:%S')  # format the time to be Hours:Minutes:Seconds
            # pickup time
            time_info_label = MyLabel(time_info_frame, "Pickup Time", row=0, col=0)  # pickup time label
            time_info = StringVar()  # pickup time variable
            time_info_entry = MyEntry(time_info_frame, var=time_info, row=0, col=1)  # pickup time entry field
            time_info.set(str(time_of_pickup))  # insert pickup time into field
            time_info_entry['state'] = DISABLED  # disable the field

            # final nav function
            # define final 'done' button function
            def done_final():
                """Wraps up the order with a popup window"""
                end = mb.showinfo('Done', "Order Received!\n Thanks for choosing Peter's Pizza Palace!")  # final popup
                if end == 'ok':  # if user clicked okay
                    final_window.destroy()  # destroy this window

            # final frame navigation
            final_nav_frame = MyFrame(final_window, row=1, col=0, colspan=4, sticky=N+S)  # navigation frame
            final_nav_frame.grid(pady=(10, 0))  # nav frame padding (15px top)
            done_btn = MyButton(final_nav_frame, 'Complete Order', row=0, col=1, command=done_final)  # done button

    # define function to get delivery information
    def get_delivery_info(cc_info=None):
        """Function to collect the user's delivery information"""
        final_window.geometry('314x220')  # set window size
        frame = 'Delivery Info'  # frame name Delivery Info (for back button and final function)
        # get delivery frame
        global get_delivery_frame  # make get delivery frame global
        get_delivery_frame = MyFrame(final_window, row=0, col=0, colspan=3)  # get delivery frame
        get_delivery_frame.grid(padx=(4, 0))  # give frame padding (4px left)
        # delivery frame heading
        get_delivery_label = MyLabel(get_delivery_frame, 'Enter Your Delivery Address:', row=0, col=0, colspan=4,
                                     font=('Helvetica', 16, 'bold', 'underline'), sticky=W)  # enter addy info heading
        # delivery frame information entry
        # 'name' row
        name_frame = MyFrame(get_delivery_frame, row=1, col=0, colspan=4, sticky=W+E)  # name frame
        name_label = MyLabel(name_frame, 'Name', row=0, col=0)  # name label
        name = StringVar()  # name tkinter variable
        name_entry = MyEntry(name_frame, var=name, row=0, col=1, width=28)  # name entry widget
        name_entry.focus_force()  # when the frame appears name entry will automatically be selected
        # 'address line 1' row
        address1_frame = MyFrame(get_delivery_frame, row=2, col=0, colspan=4)  # address1 frame
        address1_label = MyLabel(address1_frame, 'Address Line 1', row=0, col=0)  # address1 label
        address1 = StringVar()  # address1 tkinter variable
        address1_entry = MyEntry(address1_frame, var=address1, row=0, col=1, width=22)  # address1 entry widget
        # 'address line 2' row
        address2_frame = MyFrame(get_delivery_frame, row=3, col=0, colspan=4)  # address2 frame
        address2_label = MyLabel(address2_frame, 'Address Line 2', row=0, col=0)  # address2 label
        address2 = StringVar()  # address2 tkinter variable
        address2_entry = MyEntry(address2_frame, var=address2, row=0, col=1, width=22)  # address2 entry widget
        # 'city / state' row
        city_state_frame = MyFrame(get_delivery_frame, row=4, col=0, colspan=4)  # city frame
        city_label = MyLabel(city_state_frame, 'City ', row=0, col=0)  # city label
        city = StringVar()  # city tkinter variable
        city_entry = MyEntry(city_state_frame, var=city, row=0, col=1, width=20)  # city entry widget
        # state entry (in city's row / frame)
        state_label = MyLabel(city_state_frame, ' State', row=0, col=2)  # state label
        state = StringVar()  # state tkinter variable
        state_entry = MyEntry(city_state_frame, var=state, row=0, col=3, width=3)  # state entry widget
        # 'zipcode' row
        zipcode_frame = MyFrame(get_delivery_frame, row=5, col=0, colspan=4, sticky=W)  # zipcode frame
        zipcode_label = MyLabel(zipcode_frame, 'Zipcode ', row=0, col=0)  # zipcode label
        zipcode = StringVar()  # zipcode tkinter variable
        zipcode_entry = MyEntry(zipcode_frame, var=zipcode, row=0, col=1, width=17)  # zipcode entry widget

        # define function to save delivery information (and check that all fields are filled in)
        def save_delivery():
            """Function to save delivery information and move to the next frame if mandatory fields are filled in"""
            delivery_info = [None, None, None, None, None, None]  # initialize info variables to None (see below why)
            # define dictionary to set field names for error popup (see below)
            var_names = {0: 'Name', 1: 'Address Line 1', 2: 'Address Line 2', 3: 'City', 4: 'State', 5: 'Zipcode'}
            var_list = [name, address1, address2, city, state, zipcode]  # list of tkinter variables (from entry field)
            # define list of field names for 'focus_force' (see below)
            field_list = [name_entry, address1_entry, address2_entry, city_entry, state_entry, zipcode_entry]

            # check mandatory fields
            index = 0  # initialize index variable
            filled = False  # initialize boolean variable to check if all fields are filled before moving on
            for var in var_list:  # iterate through the list of tkinter StringVars from Entry fields
                var_value = var.get()  # pull the tkinter vars' values
                if not var_value:  # if the value is null / empty
                    if index == 1:  # if the field is an address (no 'Your' prefix)
                        mb.showwarning(str(var), f'Please Enter {var_names[index]}')  # popup window for mandatory field
                        field_list[index].focus_force()  # focus on the field that wasn't filled in (start typing)
                        break  # break out of the loop (without this it will check all fields at once)
                    elif index == 2:  # address line 2 (isn't mandatory)
                        delivery_info.pop(index)  # pop the None value out
                        delivery_info.insert(index, var_value)  # replace with an empty string (again, not mandatory)
                    else:  # if the field is null / empty and it's not address1 or address2
                        mb.showwarning(str(var), f'Please Enter Your {var_names[index]}')  # popup window for mandatory
                        field_list[index].focus_force()  # focus on the field that wasn't filled in (start typing)
                        break  # break out of the loop (without this it will check all fields at once)
                else:   # if the value isn't null / empty
                    delivery_info.pop(index)  # remove the null value at the index of the current variable
                    delivery_info.insert(index, var_value)  # insert the variable's value
                index += 1  # increment the index variable

            # ensure that all fields have been filled before moving on to the next frame
            for info in delivery_info:  # checking the tkinter variable values in delivery_in (values from entry fields)
                if info is not None:  # if the None has been popped above and a value put in its place
                    filled = True  # toggle filled to True indicating all fields have been filled
                else:  # if the value is still 'None' (not all fields have been filled out)
                    filled = False  # toggle filled to False indicating there are empty values still
            # check if we can move on to the next frame (all fields full and info 'saved')
            if filled is True:  # if all Entry fields are filled and values populated into list object
                create_final_frame(frame, delivery_info, cc_info)  # move on to the final frame (and pass variables)

        # section navigation
        button_frame = MyFrame(get_delivery_frame, row=6, col=0, colspan=4, sticky=N + S)  # navigation frame
        button_frame.grid(pady=(10, 0))  # nav frame padding (10px top)
        back_btn = MyButton(button_frame, '<< Back', row=0, col=0, command=lambda: back_button(frame, cc_info))  # back
        exit_btn = MyButton(button_frame, 'EXIT', row=0, col=1, command=exit_final)  # exit button
        next_btn = MyButton(button_frame, 'Next >>', row=0, col=2, command=save_delivery)  # next button

    # define function to collect the user's credit/debit card information
    def get_card_info():
        """Function to collect the user's credit/debit card information"""
        final_window.geometry('290x155')  # set the window size
        frame = 'Card Info'  # frame named Card Info (used for 'back' button and create_final function)
        # get card frame
        global get_card_frame  # make get card frame global
        get_card_frame = MyFrame(final_window, row=0, col=0, colspan=3)
        get_card_frame.grid(padx=(4, 0))
        # card frame heading
        get_card_label = MyLabel(get_card_frame, 'Enter Your Card Information:', row=0, col=0,
                                 colspan=4, font=('Helvetica', 16, 'bold', 'underline'), sticky=W)  # enter card
        # card information entry frame
        # 'card name' row
        global card_name_entry  # had to make card name entry global or back button won't work correctly (no fields)
        card_name_frame = MyFrame(get_card_frame, row=1, col=0, colspan=4, sticky=W)  # card name frame
        card_name_label = MyLabel(card_name_frame, 'Name on Card ', row=0, col=0)  # card name label
        card_name = StringVar()  # card name tkinter variable
        card_name_entry = MyEntry(card_name_frame, var=card_name, row=0, col=1, width=19)  # card name entry widget
        card_name_entry.focus_force()  # start with card name entry selected
        # 'card number' row
        card_number_frame = MyFrame(get_card_frame, row=2, col=0, colspan=4, sticky=W)  # card number frame
        card_number_label = MyLabel(card_number_frame, 'Card Number', row=0, col=0)  # card number label
        card_number = StringVar()  # card number tkinter variable
        card_number_entry = MyEntry(card_number_frame, var=card_number, row=0, col=1, width=20)  # card number entry
        # 'card expire / CVV' row
        # card expire
        expire_cvv_frame = MyFrame(get_card_frame, row=3, col=0, colspan=4, sticky=W)  # expire frame
        expire_label = MyLabel(expire_cvv_frame, 'Expiration Date ', row=0, col=0)  # expire label
        expire = StringVar()  # expire tkinter variable
        expire_entry = MyEntry(expire_cvv_frame, var=expire, row=0, col=1, width=6)  # expire entry widget
        # card cvv
        cvv_label = MyLabel(expire_cvv_frame, 'CVV #', row=0, col=2)  # cvv label
        cvv_label.grid(padx=(18, 0))  # give the CVV entry padding (18px left)
        cvv = StringVar()  # cvv tkinter variable
        cvv_entry = MyEntry(expire_cvv_frame, var=cvv, row=0, col=3, width=4)  # cvv entry widget

        # define function to save card information (for 'next' button) / check mandatory fields
        def save_card():
            """Function to save card information and move to the next frame if mandatory fields are filled"""
            card_info = [None, None, None, None]  # sets card info variables to None initially (see below)
            var_names = {0: 'Name on Your Card', 1: 'Card Number', 2: 'Expiration Date', 3: 'CVV #'}  # titles for popup
            var_list = [card_name, card_number, expire, cvv]  # list of tkinter StringVars from Entry fields
            field_list = [card_name_entry, card_number_entry, expire_entry, cvv_entry]  # list of Entry fields (below)
            # check mandatory fields
            index = 0  # initialize index variable
            filled = False  # initialize boolean variable to check if all fields are filled before moving on
            for var in var_list:  # iterate through the list of tkinter StringVars from Entry fields
                var_value = var.get()  # pull the tkinter vars' values
                if not var_value:  # if the value is null / empty
                    mb.showwarning(str(var), f'Please Enter The {var_names[index]}')  # popup window for mandatory field
                    field_list[index].focus_force()  # focus on the field that wasn't filled in (start typing)
                    break  # break out of the loop (without this it will check all fields at once)
                else:  # if the value isn't null / empty
                    card_info.pop(index)  # remove the null value at the index of the current variable
                    card_info.insert(index, var_value)  # insert the variable's value
                index += 1  # increment the index variable
            # ensure that all fields have been filled before moving on to the next frame
            for info in card_info:  # checking the tkinter variable values in card_info (values from entry fields)
                if info is not None:  # if the None has been popped above and a value put in its place
                    filled = True  # toggle filled to True indicating all fields have been filled
                else:  # if the value is still 'None' (not all fields have been filled out)
                    filled = False  # toggle filled to False indicating there are empty values still
            # check if we can move on to the next frame (all fields full and info 'saved')
            if filled is True:  # if all Entry fields are filled and values populated into list object
                if pickup_selection == 0:  # delivery order
                    get_delivery_info(card_info)  # get delivery address info frame (send card_info to it)
                    get_card_frame.destroy()  # destroy this frame
                else:  # pickup order
                    create_final_frame(frame, cc_info=card_info)  # go to the final frame (send card_info to it)

        # section navigation
        button_frame = MyFrame(get_card_frame, row=4, col=0, colspan=4, sticky=N + S)  # navigation frame
        button_frame.grid(pady=(8, 0))  # nav frame padding (10px top)
        back_btn = MyButton(button_frame, '<< Back', row=0, col=0, command=lambda: back_button(frame))  # back button
        exit_btn = MyButton(button_frame, 'EXIT', row=0, col=1, command=exit_final)  # exit button
        next_btn = MyButton(button_frame, 'Next >>', row=0, col=2, command=save_card)  # next button

    # define function for the pay with card option
    def pay_cc():
        """Function for the 'Pay Credit/Debit' option, moves to the next frame to collect info"""
        get_payment_frame.destroy()  # destroy the last frame (get payment frame)
        get_card_info()  # get card information

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
        cc_btn = MyButton(get_payment_method_frame, 'Credit/Debit Card', row=0, col=0, command=pay_cc)  # cc button
        cc_btn.grid(padx=(20, 0))  # give yes button padding (20px top)
        cash_btn = MyButton(get_payment_method_frame, 'Cash', row=0, col=1, command=pay_cash)  # cash button
        cash_btn['width'] = 12  # make cash button same side as credit/debit button

    # navigation functions
    # 'exit' button function
    def exit_final():
        """Exits the current window"""
        final_window.destroy()  # destroy this window

    # program navigation
    nav_frame = MyFrame(final_window, row=1, col=0, colspan=4, sticky=N+S)  # navigation frame
    nav_frame.grid(pady=(15, 0))  # nav frame padding (15px top)
    exit_btn = MyButton(nav_frame, 'Exit Window', row=0, col=1, command=exit_final)  # exit button

    # first function call to start the module
    get_payment_method()
