"""
Program: Peter’s Pizza Palace – Priority order-Placement Program v1.0.0 (.py)
Author: Cameron Coy (ccoy2@ivytech.edu)
Description: This is the extras module for the Peter's Pizza Palace - Priority order-Placement Program. It allows the
user to add side items, desserts and drinks to their order and sends them to the payment module when finished.
"""
# import statements
import pizza  # import previous module (for back button)
import payment  # import next module (for next button)
from myGUI import *  # import my custom tkinter syntax
from PIL import ImageTk, Image  # pip -install Pillow dependency (PIL)
from tkinter import messagebox as mb  # import messagebox for popup windows


# define 'customize_pizza' function (to create new 'customize_pizza' window)
def add_extras(pickup, p_size, p_base, your_pizza, custom=False, changes=None):
    """Add extras to your pizza order"""
    # create extras_window toplevel window
    extras_window = NewWindow("Sides, Desserts, and Drinks", '490x135')

    # define lists of items and selected items
    items = ['Breadsticks', 'Garlic Bread',
             'Cheese', 'Garlic Butter', 'Marinara', 'Ranch',
             'Cinnastix™', 'Brownies', 'Cookies', 'Choc Cookies',
             'Coke', 'Diet Coke', 'Sprite', 'Dr Pepper', 'Mtn Dew', 'Orange Soda', 'Grape Soda']  # list of items
    order = []  # list for selected items

    # define function for when we're done with the selection menus
    def done_adding():
        """Function for when you're done with the selection menus to enable the next button"""
        next_btn['state'] = NORMAL  # set next_btn state to noraml
        yes_btn['state'] = DISABLED  # set yes_btn state to disabled
        last_ask_btn['state'] = DISABLED  # set last_ask_btn state to disabled

    # define function to ask if we're done with adding extra items
    def ask_done():
        """Asks if you're done adding extra items to your order"""
        ask_drink_frame.destroy()  # destroy ask_drink frame
        # ask done
        global ask_done_frame  # make ask_done_frame global
        frame = 'Done'  # frame name
        ask_done_frame = MyFrame(extras_window, row=0, col=0, colspan=3)  # create ask_done frame
        ask_done_frame.grid(pady=(5, 0))  # give ask_done frame padding (5px top)
        ask_done_label = MyLabel(ask_done_frame, 'Are you done adding extras to your order?', row=0, col=0,
                                 font='Helvetica 14 bold')  # ask_done label
        ask_done_label['width'] = 60  # set ask_done label 60px width
        global yes_btn  # make yes button global
        global last_ask_btn  # make last ask button global
        answer_frame = MyFrame(ask_done_frame, row=1, col=0)  # create answer frame
        yes_btn = MyButton(answer_frame, 'Yes', row=0, col=0, command=done_adding)  # yes button
        no_btn = MyButton(answer_frame, 'No', row=0, col=2)  # no button
        no_btn['state'] = DISABLED  # disable no button (just press back button)
        last_ask_btn = MyButton(answer_frame, 'Back', row=0, col=1, command=lambda: last_ask(frame))  # back button

    # define function to go forward in selection
    def done(current):
        """Next button's function: destroy current frame, reset window size and load next frame"""
        if current == 'Side':  # frame is named side
            add_side_frame.destroy()  # destroy side frame
            extras_window.geometry('490x135')  # set window size
            ask_dipping()  # ask about dipping sauces
        if current == 'Dipping':  # frame is named dipping
            add_dipping_frame.destroy()  # destroy dipping frame
            extras_window.geometry('490x135')  # set window size
            ask_dessert()  # ask about dessert items
        if current == 'Dessert':  # frame is named dessert
            add_dessert_frame.destroy()  # destroy dessert frame
            extras_window.geometry('490x135')  # set window size
            ask_drink()  # ask about drink items
        if current == 'Drink':  # frame is named drink
            add_drink_frame.destroy()  # destroy drink frame
            extras_window.geometry('490x135')  # set window size
            ask_done()  # ask if done adding extra items

    # define function to add items to your order
    def add_to_order(item):
        """Add to Order Button: opens a popup window to confirm and adds selected extra item to your order"""
        added = mb.askokcancel('Added!', f'Added {item} to Order!')  # creates popup window to confirm, cancel won't add
        extras_window.focus_force()  # force the extras window back into focus
        if added is True:  # if you clicked 'ok' on the popup window
            order.append(item)  # add the item to your order
        return order  # return updated order

    # define function for the back button
    def last_ask(current):
        """Back button's function: destroy current frame, reset window size and load previous frame"""
        if current == 'Dipping':  # frame named dipping
            ask_dipping_frame.destroy()  # destroy dipping frame
            ask_side()  # ask about side items
        if current == 'Dessert':  # frame named dessert
            ask_dessert_frame.destroy()  # destroy dessert frame
            ask_dipping()  # ask about dipping sauces
        if current == 'Drink':  # frame named drink
            ask_drink_frame.destroy()  # destroy drink frame
            ask_dessert()  # ask about dessert items
        if current == 'Done':  # frame named done
            ask_done_frame.destroy()  # destroy done frame
            ask_drink()  # ask about drinks

    # define function to add drinks
    def add_drink():
        """Add drinks to your order (loads images and new frame)"""
        ask_drink_frame.destroy()  # destroy the ask drink frame
        extras_window.geometry('860x214')  # set window size
        # add_drink
        global add_drink_frame  # make add_drink_frame global
        global coke  # make coke global
        global diet  # make diet global
        global sprite  # make sprite global
        global pepper  # make pepper global
        global dew  # make dew global
        global orange  # make orange global
        global grape  # make grape global
        # open drink images
        coke = ImageTk.PhotoImage(Image.open('images/drinks/coke.png'))  # coke image
        diet = ImageTk.PhotoImage(Image.open('images/drinks/diet.png'))  # diet image
        sprite = ImageTk.PhotoImage(Image.open('images/drinks/sprite.png'))  # sprite image
        pepper = ImageTk.PhotoImage(Image.open('images/drinks/pepper.png'))  # pepper image
        dew = ImageTk.PhotoImage(Image.open('images/drinks/dew.png'))  # dew image
        orange = ImageTk.PhotoImage(Image.open('images/drinks/orange.png'))  # orange image
        grape = ImageTk.PhotoImage(Image.open('images/drinks/grape.png'))  # grape image

        frame = 'Drink'  # frame named drink
        add_drink_frame = MyFrame(extras_window, row=0, col=0, colspan=7)  # create add drink frame
        add_drink_label = MyLabel(add_drink_frame, 'Add drinks to your order', row=0, col=0,
                                  font='Helvetica 18 bold')  # create add drink label
        add_drink_label['width'] = 60  # set add drink label width (60 px)
        add_drink_label.grid(pady=(5, 10))  # give add drink label padding (5px top, 10px bottom)

        drink_images_frame = MyFrame(add_drink_frame, row=1, col=0)  # drink images frame

        coke_frame = MyLabelFrame(drink_images_frame, 'Coke', row=0, col=0,
                                  font='Helvetica 14 bold', padx=20)  # coke frame
        coke_image = MyLabel(coke_frame, '', row=0, col=0, img=coke)  # coke image
        add_coke = MyButton(drink_images_frame, 'Add to Order', row=1, col=0,
                            command=lambda: add_to_order(items[10]))  # add coke to order button

        diet_frame = MyLabelFrame(drink_images_frame, 'Diet Coke', row=0, col=1,
                                  font='Helvetica 14 bold', padx=20)  # diet frame
        diet_image = MyLabel(diet_frame, '', row=0, col=0, img=diet)  # diet image
        add_diet = MyButton(drink_images_frame, 'Add to Order', row=1, col=1,
                            command=lambda: add_to_order(items[11]))  # add diet to order button

        sprite_frame = MyLabelFrame(drink_images_frame, 'Sprite', row=0, col=2,
                                    font='Helvetica 14 bold', padx=20)  # sprite frame
        sprite_image = MyLabel(sprite_frame, '', row=0, col=0, img=sprite)  # sprite image
        add_sprite = MyButton(drink_images_frame, 'Add to Order', row=1, col=2,
                              command=lambda: add_to_order(items[12]))  # add sprite to order button

        pepper_frame = MyLabelFrame(drink_images_frame, 'Dr Pepper', row=0, col=3,
                                    font='Helvetica 14 bold', padx=20)  # dr pepper frame
        pepper_image = MyLabel(pepper_frame, '', row=0, col=0, img=pepper)  # dr pepper image
        add_pepper = MyButton(drink_images_frame, 'Add to Order', row=1, col=3,
                              command=lambda: add_to_order(items[13]))  # add dr pepper to order button

        dew_frame = MyLabelFrame(drink_images_frame, 'Mtn Dew', row=0, col=4,
                                 font='Helvetica 14 bold', padx=20)  # dew frame
        dew_image = MyLabel(dew_frame, '', row=0, col=0, img=dew)  # dew image
        add_dew = MyButton(drink_images_frame, 'Add to Order', row=1, col=4,
                           command=lambda: add_to_order(items[14]))  # add dew to order button

        orange_frame = MyLabelFrame(drink_images_frame, 'Orange', row=0, col=5,
                                    font='Helvetica 14 bold', padx=20)  # orange frame
        orange_image = MyLabel(orange_frame, '', row=0, col=0, img=orange)  # orange image
        add_orange = MyButton(drink_images_frame, 'Add to Order', row=1, col=5,
                              command=lambda: add_to_order(items[15]))  # add orange to order button

        grape_frame = MyLabelFrame(drink_images_frame, 'Grape', row=0, col=6,
                                   font='Helvetica 14 bold', padx=20)  # grape frame
        grape_image = MyLabel(grape_frame, '', row=0, col=0, img=grape)  # grape image
        add_grape = MyButton(drink_images_frame, 'Add to Order', row=1, col=6,
                             command=lambda: add_to_order(items[16]))  # add grape to order button

        done_btn = MyButton(drink_images_frame, 'Done', row=2, col=0, colspan=7, command=lambda: done(frame))  # done bt
        done_btn['width'] = 6  # set done button width
        done_btn.grid(pady=(4, 0))  # give done button padding (4px top)

    # define function to add dessert items
    def add_dessert():
        """Add dessert items to your order (loads images and new frame)"""
        ask_dessert_frame.destroy()  # destroy ask dessert frame
        extras_window.geometry('670x239')  # set window size
        # add_dessert
        global add_dessert_frame  # make add_dessert_frame global
        global cinnastix  # make cinnastix global
        global brownies  # make brownies global
        global cookies  # make cookies global
        global chocolate  # make chocolate global
        # open dessert images
        cinnastix = ImageTk.PhotoImage(Image.open('images/desserts/cinna.png'))  # cinnastix
        brownies = ImageTk.PhotoImage(Image.open('images/desserts/brown.png'))  # brownies
        cookies = ImageTk.PhotoImage(Image.open('images/desserts/cookie.png'))  # cookies
        chocolate = ImageTk.PhotoImage(Image.open('images/desserts/choc.png'))  # chocolate

        frame = 'Dessert'  # frame name dessert
        add_dessert_frame = MyFrame(extras_window, row=0, col=0, colspan=4)  # add dessert frame
        add_dessert_label = MyLabel(add_dessert_frame, 'Add desserts to your order', row=0, col=0,
                                    font='Helvetica 18 bold')  # dessert label
        add_dessert_label['width'] = 60  # set dessert label width (60px)
        add_dessert_label.grid(pady=(5, 10))  # give dessert label padding (5px top, 10px bottom)

        dessert_images_frame = MyFrame(add_dessert_frame, row=1, col=0)  # dessert images frame

        cinnastix_frame = MyLabelFrame(dessert_images_frame, 'Cinnastix™', row=0, col=0,
                                       font='Helvetica 14 bold', padx=20)  # cinnastix frame
        cinnastix_image = MyLabel(cinnastix_frame, '', row=0, col=0, img=cinnastix)  # cinnastix image
        add_cinnastix = MyButton(dessert_images_frame, 'Add to Order', row=1, col=0,
                                 command=lambda: add_to_order(items[6]))  # add cinnastix to order button

        brownies_frame = MyLabelFrame(dessert_images_frame, 'Brownies', row=0, col=1,
                                      font='Helvetica 14 bold', padx=20)  # brownies frame
        brownies_image = MyLabel(brownies_frame, '', row=0, col=0, img=brownies)  # brownies image
        add_brownies = MyButton(dessert_images_frame, 'Add to Order', row=1, col=1,
                                command=lambda: add_to_order(items[7]))  # add brownies to order button

        cookies_frame = MyLabelFrame(dessert_images_frame, 'Cookies', row=0, col=2,
                                     font='Helvetica 14 bold', padx=20)  # cookies frame
        cookies_image = MyLabel(cookies_frame, '', row=0, col=0, img=cookies)  # cookies image
        add_cookies = MyButton(dessert_images_frame, 'Add to Order', row=1, col=2,
                               command=lambda: add_to_order(items[8]))  # add cookies to order button

        chocolate_frame = MyLabelFrame(dessert_images_frame, 'Choc Cookies', row=0, col=3,
                                       font='Helvetica 14 bold', padx=20)  # chocolate frame
        chocolate_image = MyLabel(chocolate_frame, '', row=0, col=0, img=chocolate)  # chocolate image
        add_chocolate = MyButton(dessert_images_frame, 'Add to Order', row=1, col=3,
                                 command=lambda: add_to_order(items[9]))  # add chocolate to order button

        done_btn = MyButton(dessert_images_frame, 'Done', row=2, col=0, colspan=4, command=lambda: done(frame))  # done
        done_btn['width'] = 6  # set done button width (6px)
        done_btn.grid(pady=(4, 0))  # give done button padding (4px top)

    # define function to ask about drink items
    def ask_drink():
        """Ask to add drinks to your order (destroy last frame and load next frame)"""
        ask_dessert_frame.destroy()  # destroy ask dessert frame
        # ask add_drink
        global ask_drink_frame  # make ask_drink_frame global
        frame = 'Drink'  # frame name drink
        ask_drink_frame = MyFrame(extras_window, row=0, col=0, colspan=3)  # ask drink frame
        ask_drink_frame.grid(pady=(5, 0))  # give ask drink frame padding (5px top)
        ask_drink_label = MyLabel(ask_drink_frame, 'Would you like to add a drink to your order?', row=0, col=0,
                                  font='Helvetica 14 bold')  # drink label
        ask_drink_label['width'] = 60  # set drink label width (60px)
        answer_frame = MyFrame(ask_drink_frame, row=1, col=0)  # answer frame
        yes_btn = MyButton(answer_frame, 'Yes', row=0, col=0, command=add_drink)  # yes button
        no_btn = MyButton(answer_frame, 'No', row=0, col=2, command=ask_done)  # done button
        last_ask_btn = MyButton(answer_frame, 'Back', row=0, col=1, command=lambda: last_ask(frame))  # back button

    # define function to add dipping sauces
    def add_dipping():
        """Add dipping sauces to your order (loads images and new frame)"""
        ask_dipping_frame.destroy()  # destroy ask dipping frame
        extras_window.geometry('670x239')  # set window size
        # add_dipping
        global add_dipping_frame  # make add_dipping_frame global
        global cheesy_jalapeno  # make cheesy_jalapeno global
        global garlic_butter  # make garlic_butter global
        global marinara  # make marinara global
        global ranch  # make ranch global
        # open dipping images
        cheesy_jalapeno = ImageTk.PhotoImage(Image.open('images/sauces/chee.png'))  # cheesy jalapeno
        garlic_butter = ImageTk.PhotoImage(Image.open('images/sauces/gar.png'))  # garlic butter
        marinara = ImageTk.PhotoImage(Image.open('images/sauces/mar.png'))  # marinara
        ranch = ImageTk.PhotoImage(Image.open('images/sauces/ran.png'))  # ranch

        frame = 'Dipping'  # frame name dipping
        add_dipping_frame = MyFrame(extras_window, row=0, col=0, colspan=4)  # add dipping frame
        add_dipping_label = MyLabel(add_dipping_frame, 'Add dipping sauces to your order', row=0, col=0,
                                    font='Helvetica 18 bold')  # dipping label
        add_dipping_label['width'] = 60  # set dipping label width (60px)
        add_dipping_label.grid(pady=(5, 10))  # give dipping label padding (5px top, 10px bottom)

        dipping_images_frame = MyFrame(add_dipping_frame, row=1, col=0)  # dipping images frame

        cheesy_jalapeno_frame = MyLabelFrame(dipping_images_frame, 'Cheese', row=0, col=0,
                                             font='Helvetica 14 bold', padx=20)  # cheesy_jalapeno frame
        cheesy_jalapeno_image = MyLabel(cheesy_jalapeno_frame, '', row=0, col=0, img=cheesy_jalapeno)  # cheesy image
        add_cheesy_jalapeno = MyButton(dipping_images_frame, 'Add to Order', row=1, col=0,
                                       command=lambda: add_to_order(items[2]))  # add to order button

        garlic_butter_frame = MyLabelFrame(dipping_images_frame, 'Garlic Butter', row=0, col=1,
                                           font='Helvetica 14 bold', padx=20)  # garlic_butter frame
        garlic_butter_image = MyLabel(garlic_butter_frame, '', row=0, col=0, img=garlic_butter)  # garlic_butter image
        add_garlic_butter = MyButton(dipping_images_frame, 'Add to Order', row=1, col=1,
                                     command=lambda: add_to_order(items[3]))  # add to order button

        marinara_frame = MyLabelFrame(dipping_images_frame, 'Marinara', row=0, col=2,
                                      font='Helvetica 14 bold', padx=20)  # marinara frame
        marinara_image = MyLabel(marinara_frame, '', row=0, col=0, img=marinara)  # marinara image
        add_marinara = MyButton(dipping_images_frame, 'Add to Order', row=1, col=2,
                                command=lambda: add_to_order(items[4]))  # add to order button

        ranch_frame = MyLabelFrame(dipping_images_frame, 'Ranch', row=0, col=3,
                                   font='Helvetica 14 bold', padx=20)  # ranch frame
        ranch_image = MyLabel(ranch_frame, '', row=0, col=0, img=ranch)  # ranch image
        add_ranch = MyButton(dipping_images_frame, 'Add to Order', row=1, col=3,
                             command=lambda: add_to_order(items[5]))  # add to order button

        done_btn = MyButton(dipping_images_frame, 'Done', row=2, col=0, colspan=4, command=lambda: done(frame))  # done
        done_btn['width'] = 6  # done button width (6px)
        done_btn.grid(pady=(4, 0))  # add done button padding (4px top)

    # define function to ask about dessert items
    def ask_dessert():
        """Ask to add desserts to your order (destroy last frame and load next frame)"""
        ask_dipping_frame.destroy()  # destroy ask dipping frame
        # ask add_dessert
        global ask_dessert_frame  # make ask_dessert_frame global
        frame = 'Dessert'  # frame name dessert
        ask_dessert_frame = MyFrame(extras_window, row=0, col=0, colspan=3)  # ask dessert frame
        ask_dessert_frame.grid(pady=(5, 0))  # ask dessert frame padding (5px top)
        ask_dessert_label = MyLabel(ask_dessert_frame, 'Would you like to add a dessert to your order?', row=0, col=0,
                                    font='Helvetica 14 bold')  # dessert label
        ask_dessert_label['width'] = 60  # dessert label width (60px)
        answer_frame = MyFrame(ask_dessert_frame, row=1, col=0)  # answer frame
        yes_btn = MyButton(answer_frame, 'Yes', row=0, col=0, command=add_dessert)  # yes button
        no_btn = MyButton(answer_frame, 'No', row=0, col=2, command=ask_drink)  # no button
        last_ask_btn = MyButton(answer_frame, 'Back', row=0, col=1, command=lambda: last_ask(frame))  # back button

    # define function to add site items
    def add_side():
        """Add side items to your order (loads images and new frame)"""
        ask_side_frame.destroy()  # destroy ask side frame
        extras_window.geometry('670x335')  # set window size
        # add_side
        global add_side_frame  # make add_side_frame global
        global breadsticks  # make breadsticks global
        global garlic_bread  # make garlic_bread global
        # open side images
        breadsticks = ImageTk.PhotoImage(Image.open('images/sides/bs.png'))  # breadsticks
        garlic_bread = ImageTk.PhotoImage(Image.open('images/sides/gb.png'))  # garlic bread
        frame = 'Side'  # frame name side
        add_side_frame = MyFrame(extras_window, row=0, col=0, colspan=3)  # add side frame
        add_side_label = MyLabel(add_side_frame, 'Add sides to your order', row=0, col=0,
                                 font='Helvetica 18 bold')  # side label
        add_side_label['width'] = 60  # side label width (60px)
        add_side_label.grid(pady=(5, 10))  # add side label padding (5px top, 10px bottom)

        side_images_frame = MyFrame(add_side_frame, row=1, col=0)  # side images

        breadsticks_frame = MyLabelFrame(side_images_frame, 'Breadsticks', row=0, col=0,
                                         font='Helvetica 14 bold', padx=20)  # breadsticks frame
        breadsticks_image = MyLabel(breadsticks_frame, '', row=0, col=0, img=breadsticks)  # breadsticks image
        add_breadsticks = MyButton(side_images_frame, 'Add to Order', row=1, col=0,
                                   command=lambda: add_to_order(items[0]))  # add to order button

        garlic_bread_frame = MyLabelFrame(side_images_frame, 'Garlic Bread', row=0, col=1,
                                          font='Helvetica 14 bold', padx=20)  # garlic_bread frame
        garlic_bread_image = MyLabel(garlic_bread_frame, '', row=0, col=0, img=garlic_bread)  # garlic_bread image
        add_garlic_bread = MyButton(side_images_frame, 'Add to Order', row=1, col=1,
                                    command=lambda: add_to_order(items[1]))  # add to order button

        done_btn = MyButton(side_images_frame, 'Done', row=2, col=0, colspan=3, command=lambda: done(frame))  # done
        done_btn['width'] = 6  # done button width (6px)

    # define function to ask about dipping sauces
    def ask_dipping():
        """Ask to add dipping sauces to your order (destroy last frame and load next frame)"""
        ask_side_frame.destroy()  # destroy ask side frame
        # ask add_dipping
        global ask_dipping_frame  # make ask_dipping_frame global
        frame = 'Dipping'  # frame name dipping
        ask_dipping_frame = MyFrame(extras_window, row=0, col=0, colspan=3)  # ask dipping frame
        ask_dipping_frame.grid(pady=(5, 0))  # ask dipping frame padding (5px top)
        ask_dipping_label = MyLabel(ask_dipping_frame, 'Would you like to add dipping sauces to your order?', row=0,
                                    col=0, font='Helvetica 14 bold')  # dipping label
        ask_dipping_label['width'] = 60  # dipping label width (60px)
        answer_frame = MyFrame(ask_dipping_frame, row=1, col=0)  # answer frame
        yes_btn = MyButton(answer_frame, 'Yes', row=0, col=0, command=add_dipping)  # yes button
        no_btn = MyButton(answer_frame, 'No', row=0, col=2, command=ask_dessert)  # no button
        last_ask_btn = MyButton(answer_frame, 'Back', row=0, col=1, command=lambda: last_ask(frame))  # back button

    # define function to ask about side items (first frame of the module)
    def ask_side():
        """Ask to add side items to your order (destroy last frame and load next frame)"""
        # ask add_side
        global ask_side_frame  # make ask_side_frame global
        frame = 'Side'  # frame name side
        ask_side_frame = MyFrame(extras_window, row=0, col=0, colspan=3)  # ask side frame
        ask_side_frame.grid(pady=(5, 0))  # ask side frame padding (5px top)
        ask_side_label = MyLabel(ask_side_frame, 'Would you like to add sides to your order?', row=0, col=0,
                                 font='Helvetica 14 bold')  # side label
        ask_side_label['width'] = 60  # side label width (60px)
        answer_frame = MyFrame(ask_side_frame, row=1, col=0)  # answer frame
        yes_btn = MyButton(answer_frame, 'Yes', row=0, col=0, command=add_side)  # yes button
        no_btn = MyButton(answer_frame, 'No', row=0, col=2, command=ask_dipping)  # no button
        last_ask_btn = MyButton(answer_frame, 'Back', row=0, col=1, command=lambda: last_ask(frame))  # back button
        last_ask_btn['state'] = DISABLED  # back button disabled (this is the first frame)

    # 'back' button function
    def back_extras():
        """Loads the previous module and destroys the current window (also passes variables on to the that module)"""
        pizza.customize_pizza(pickup, p_size, p_base, your_pizza)  # opens the 'customize_pizza' window (and passes variables)
        extras_window.destroy()  # destroy this window

    # 'exit' button function
    def exit_extras():
        """Exits the current window and resets variables"""
        p_size.set(0)  # reset 'size' variable (avoid weird behavior)
        p_base = IntVar()  # resent p_base as a tkinter variable (instead of an integer, so it can be reset below)
        p_base.set(0)  # reset 'base' variable (avoid weird behavior)
        your_pizza = None  # reset 'your_pizza' variable (avoid weird behavior)
        custom = False  # reset custom variable (avoid weird behavior)
        changes = None  # reset changes variable (avoid weird behavior)
        order = []  # reset order variable (avoid weird behavior)
        extras_window.destroy()  # destroy 'extras' window

    # 'next' button function
    def next_payment():
        """Loads the next module and destroys the current window (also passes variables on to the next module)"""
        extras_window.destroy()  # destroy this window
        payment.pizza_payment(pickup, p_size, p_base, your_pizza, custom, changes, order)  # go to the next module

    # ask about side items (first frame of the module)
    ask_side()

    # program navigation
    nav_frame = MyFrame(extras_window, row=1, col=0, colspan=4, sticky=N+S)  # navigation frame
    nav_frame.grid(pady=(40, 0))  # nav frame padding (40px top)
    back_btn = MyButton(nav_frame, '<< Back', row=0, col=0, command=back_extras)  # back button
    exit_btn = MyButton(nav_frame, 'EXIT', row=0, col=1, command=exit_extras)  # exit button
    next_btn = MyButton(nav_frame, 'Next >>', row=0, col=2, command=next_payment)  # next button
    next_btn['state'] = DISABLED  # disable next button (until all selections are made)
