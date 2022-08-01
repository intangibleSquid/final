"""
Program: Peter’s Pizza Palace – Priority order-Placement Program v1.0.0 (.py)
Author: Cameron Coy (ccoy2@ivytech.edu)
Description: This is the extras module for the Peter's Pizza Palace - Priority order-Placement Program. It allows the
user to add side items, desserts and drinks to their order and sends them to the payment module when finished.
"""
# import statements
import pizza
import payment
from myGUI import *
from PIL import ImageTk, Image
from tkinter import messagebox as mb


# define 'customize_pizza' function (to create new 'customize_pizza' window)
def add_extras(pickup, p_size, p_base, your_pizza, custom=False, changes=None):
    extras_window = NewWindow("Sides, Desserts, and Drinks", '490x135')

    items = ['Breadsticks', 'Garlic Bread',
             'Cheese', 'Garlic Butter', 'Marinara', 'Ranch',
             'Cinnastix™', 'Brownies', 'Cookies', 'Choc Cookies',
             'Coke', 'Diet Coke', 'Sprite', 'Dr Pepper', 'Mtn Dew', 'Orange Soda', 'Grape Soda']
    order = []

    def done_adding():
        next_btn['state'] = NORMAL
        yes_btn['state'] = DISABLED
        last_ask_btn['state'] = DISABLED

    def ask_done():
        ask_drink_frame.destroy()
        # ask done
        global ask_done_frame
        frame = 'Done'
        ask_done_frame = MyFrame(extras_window, row=0, col=0, colspan=3)
        ask_done_frame.grid(pady=(5, 0))
        ask_done_label = MyLabel(ask_done_frame, 'Are you done adding extras to your order?', row=0, col=0,
                                 font='Helvetica 14 bold')
        ask_done_label['width'] = 60
        global yes_btn
        global last_ask_btn
        answer_frame = MyFrame(ask_done_frame, row=1, col=0)
        yes_btn = MyButton(answer_frame, 'Yes', row=0, col=0, command=done_adding)
        no_btn = MyButton(answer_frame, 'No', row=0, col=2)
        no_btn['state'] = DISABLED
        last_ask_btn = MyButton(answer_frame, 'Back', row=0, col=1, command=lambda: last_ask(frame))

    def done(current):
        if current == 'Side':
            add_side_frame.destroy()
            extras_window.geometry('490x135')
            ask_dipping()
        if current == 'Dipping':
            add_dipping_frame.destroy()
            extras_window.geometry('490x135')
            ask_dessert()
        if current == 'Dessert':
            add_dessert_frame.destroy()
            extras_window.geometry('490x135')
            ask_drink()
        if current == 'Drink':
            add_drink_frame.destroy()
            extras_window.geometry('490x135')
            ask_done()

    def add_to_order(item):
        added = mb.askokcancel('Added!', f'Added {item} to Order!')
        extras_window.focus_force()
        if added is True:
            order.append(item)
        return order


    def last_ask(current):
        if current == 'Dipping':
            ask_dipping_frame.destroy()
            ask_side()
        if current == 'Dessert':
            ask_dessert_frame.destroy()
            ask_dipping()
        if current == 'Drink':
            ask_drink_frame.destroy()
            ask_dessert()
        if current == 'Done':
            ask_done_frame.destroy()
            ask_drink()

    def add_drink():
        ask_drink_frame.destroy()
        extras_window.geometry('860x214')
        # add_drink
        global add_drink_frame
        global coke
        global diet
        global sprite
        global pepper
        global dew
        global orange
        global grape
        # open drink images
        coke = ImageTk.PhotoImage(Image.open('images/drinks/coke.png'))
        diet = ImageTk.PhotoImage(Image.open('images/drinks/diet.png'))
        sprite = ImageTk.PhotoImage(Image.open('images/drinks/sprite.png'))
        pepper = ImageTk.PhotoImage(Image.open('images/drinks/pepper.png'))
        dew = ImageTk.PhotoImage(Image.open('images/drinks/dew.png'))
        orange = ImageTk.PhotoImage(Image.open('images/drinks/orange.png'))
        grape = ImageTk.PhotoImage(Image.open('images/drinks/grape.png'))

        frame = 'Drink'
        add_drink_frame = MyFrame(extras_window, row=0, col=0, colspan=7)
        add_drink_label = MyLabel(add_drink_frame, 'Add drinks to your order', row=0, col=0,
                                  font='Helvetica 18 bold')
        add_drink_label['width'] = 60
        add_drink_label.grid(pady=(5, 10))

        drink_images_frame = MyFrame(add_drink_frame, row=1, col=0)

        coke_frame = MyLabelFrame(drink_images_frame, 'Coke', row=0, col=0,
                                  font='Helvetica 14 bold', padx=20)
        coke_image = MyLabel(coke_frame, '', row=0, col=0, img=coke)
        add_coke = MyButton(drink_images_frame, 'Add to Order', row=1, col=0,
                            command=lambda: add_to_order(items[10]))

        diet_frame = MyLabelFrame(drink_images_frame, 'Diet Coke', row=0, col=1,
                                  font='Helvetica 14 bold', padx=20)
        diet_image = MyLabel(diet_frame, '', row=0, col=0, img=diet)
        add_diet = MyButton(drink_images_frame, 'Add to Order', row=1, col=1,
                            command=lambda: add_to_order(items[11]))

        sprite_frame = MyLabelFrame(drink_images_frame, 'Sprite', row=0, col=2,
                                    font='Helvetica 14 bold', padx=20)
        sprite_image = MyLabel(sprite_frame, '', row=0, col=0, img=sprite)
        add_sprite = MyButton(drink_images_frame, 'Add to Order', row=1, col=2,
                              command=lambda: add_to_order(items[12]))

        pepper_frame = MyLabelFrame(drink_images_frame, 'Dr Pepper', row=0, col=3,
                                    font='Helvetica 14 bold', padx=20)
        pepper_image = MyLabel(pepper_frame, '', row=0, col=0, img=pepper)
        add_pepper = MyButton(drink_images_frame, 'Add to Order', row=1, col=3,
                              command=lambda: add_to_order(items[13]))

        dew_frame = MyLabelFrame(drink_images_frame, 'Mtn Dew', row=0, col=4,
                                 font='Helvetica 14 bold', padx=20)
        dew_image = MyLabel(dew_frame, '', row=0, col=0, img=dew)
        add_dew = MyButton(drink_images_frame, 'Add to Order', row=1, col=4,
                           command=lambda: add_to_order(items[14]))

        orange_frame = MyLabelFrame(drink_images_frame, 'Orange', row=0, col=5,
                                    font='Helvetica 14 bold', padx=20)
        orange_image = MyLabel(orange_frame, '', row=0, col=0, img=orange)
        add_orange = MyButton(drink_images_frame, 'Add to Order', row=1, col=5,
                              command=lambda: add_to_order(items[15]))

        grape_frame = MyLabelFrame(drink_images_frame, 'Grape', row=0, col=6,
                                   font='Helvetica 14 bold', padx=20)
        grape_image = MyLabel(grape_frame, '', row=0, col=0, img=grape)
        add_grape = MyButton(drink_images_frame, 'Add to Order', row=1, col=6,
                             command=lambda: add_to_order(items[16]))

        done_btn = MyButton(drink_images_frame, 'Done', row=2, col=0, colspan=7, command=lambda: done(frame))
        done_btn['width'] = 6
        done_btn.grid(pady=(4, 0))

    def add_dessert():
        ask_dessert_frame.destroy()
        extras_window.geometry('670x239')
        # add_dessert
        global add_dessert_frame
        global cinnastix
        global brownies
        global cookies
        global chocolate
        # open dessert images
        cinnastix = ImageTk.PhotoImage(Image.open('images/desserts/cinna.png'))
        brownies = ImageTk.PhotoImage(Image.open('images/desserts/brown.png'))
        cookies = ImageTk.PhotoImage(Image.open('images/desserts/cookie.png'))
        chocolate = ImageTk.PhotoImage(Image.open('images/desserts/choc.png'))

        frame = 'Dessert'
        add_dessert_frame = MyFrame(extras_window, row=0, col=0, colspan=4)
        add_dessert_label = MyLabel(add_dessert_frame, 'Add desserts to your order', row=0, col=0,
                                    font='Helvetica 18 bold')
        add_dessert_label['width'] = 60
        add_dessert_label.grid(pady=(5, 10))

        dessert_images_frame = MyFrame(add_dessert_frame, row=1, col=0)

        cinnastix_frame = MyLabelFrame(dessert_images_frame, 'Cinnastix™', row=0, col=0,
                                       font='Helvetica 14 bold', padx=20)
        cinnastix_image = MyLabel(cinnastix_frame, '', row=0, col=0, img=cinnastix)
        add_cinnastix = MyButton(dessert_images_frame, 'Add to Order', row=1, col=0,
                                 command=lambda: add_to_order(items[6]))

        brownies_frame = MyLabelFrame(dessert_images_frame, 'Brownies', row=0, col=1,
                                      font='Helvetica 14 bold', padx=20)
        brownies_image = MyLabel(brownies_frame, '', row=0, col=0, img=brownies)
        add_brownies = MyButton(dessert_images_frame, 'Add to Order', row=1, col=1,
                                command=lambda: add_to_order(items[7]))

        cookies_frame = MyLabelFrame(dessert_images_frame, 'Cookies', row=0, col=2,
                                     font='Helvetica 14 bold', padx=20)
        cookies_image = MyLabel(cookies_frame, '', row=0, col=0, img=cookies)
        add_cookies = MyButton(dessert_images_frame, 'Add to Order', row=1, col=2,
                               command=lambda: add_to_order(items[8]))

        chocolate_frame = MyLabelFrame(dessert_images_frame, 'Choc Cookies', row=0, col=3,
                                       font='Helvetica 14 bold', padx=20)
        chocolate_image = MyLabel(chocolate_frame, '', row=0, col=0, img=chocolate)
        add_chocolate = MyButton(dessert_images_frame, 'Add to Order', row=1, col=3,
                                 command=lambda: add_to_order(items[9]))

        done_btn = MyButton(dessert_images_frame, 'Done', row=2, col=0, colspan=4, command=lambda: done(frame))
        done_btn['width'] = 6
        done_btn.grid(pady=(4, 0))

    def ask_drink():
        ask_dessert_frame.destroy()
        # ask add_drink
        global ask_drink_frame
        frame = 'Drink'
        ask_drink_frame = MyFrame(extras_window, row=0, col=0, colspan=3)
        ask_drink_frame.grid(pady=(5, 0))
        ask_drink_label = MyLabel(ask_drink_frame, 'Would you like to add a drink to your order?', row=0, col=0,
                                  font='Helvetica 14 bold')
        ask_drink_label['width'] = 60
        answer_frame = MyFrame(ask_drink_frame, row=1, col=0)
        yes_btn = MyButton(answer_frame, 'Yes', row=0, col=0, command=add_drink)
        no_btn = MyButton(answer_frame, 'No', row=0, col=2, command=ask_done)
        last_ask_btn = MyButton(answer_frame, 'Back', row=0, col=1, command=lambda: last_ask(frame))

    def add_dipping():
        ask_dipping_frame.destroy()
        extras_window.geometry('670x239')
        # add_dipping
        global add_dipping_frame
        global cheesy_jalapeno
        global garlic_butter
        global marinara
        global ranch
        # open dipping images
        cheesy_jalapeno = ImageTk.PhotoImage(Image.open('images/sauces/chee.png'))
        garlic_butter = ImageTk.PhotoImage(Image.open('images/sauces/gar.png'))
        marinara = ImageTk.PhotoImage(Image.open('images/sauces/mar.png'))
        ranch = ImageTk.PhotoImage(Image.open('images/sauces/ran.png'))

        frame = 'Dipping'
        add_dipping_frame = MyFrame(extras_window, row=0, col=0, colspan=4)
        add_dipping_label = MyLabel(add_dipping_frame, 'Add dipping sauces to your order', row=0, col=0,
                                    font='Helvetica 18 bold')
        add_dipping_label['width'] = 60
        add_dipping_label.grid(pady=(5, 10))

        dipping_images_frame = MyFrame(add_dipping_frame, row=1, col=0)

        cheesy_jalapeno_frame = MyLabelFrame(dipping_images_frame, 'Cheese', row=0, col=0,
                                             font='Helvetica 14 bold', padx=20)
        cheesy_jalapeno_image = MyLabel(cheesy_jalapeno_frame, '', row=0, col=0, img=cheesy_jalapeno)
        add_cheesy_jalapeno = MyButton(dipping_images_frame, 'Add to Order', row=1, col=0,
                                       command=lambda: add_to_order(items[2]))

        garlic_butter_frame = MyLabelFrame(dipping_images_frame, 'Garlic Butter', row=0, col=1,
                                           font='Helvetica 14 bold', padx=20)
        garlic_butter_image = MyLabel(garlic_butter_frame, '', row=0, col=0, img=garlic_butter)
        add_garlic_butter = MyButton(dipping_images_frame, 'Add to Order', row=1, col=1,
                                     command=lambda: add_to_order(items[3]))

        marinara_frame = MyLabelFrame(dipping_images_frame, 'Marinara', row=0, col=2,
                                      font='Helvetica 14 bold', padx=20)
        marinara_image = MyLabel(marinara_frame, '', row=0, col=0, img=marinara)
        add_marinara = MyButton(dipping_images_frame, 'Add to Order', row=1, col=2,
                                command=lambda: add_to_order(items[4]))

        ranch_frame = MyLabelFrame(dipping_images_frame, 'Ranch', row=0, col=3,
                                   font='Helvetica 14 bold', padx=20)
        ranch_image = MyLabel(ranch_frame, '', row=0, col=0, img=ranch)
        add_ranch = MyButton(dipping_images_frame, 'Add to Order', row=1, col=3,
                             command=lambda: add_to_order(items[5]))

        done_btn = MyButton(dipping_images_frame, 'Done', row=2, col=0, colspan=4, command=lambda: done(frame))
        done_btn['width'] = 6
        done_btn.grid(pady=(4, 0))

    def ask_dessert():
        ask_dipping_frame.destroy()
        # ask add_dessert
        global ask_dessert_frame
        frame = 'Dessert'
        ask_dessert_frame = MyFrame(extras_window, row=0, col=0, colspan=3)
        ask_dessert_frame.grid(pady=(5, 0))
        ask_dessert_label = MyLabel(ask_dessert_frame, 'Would you like to add a dessert to your order?', row=0, col=0,
                                    font='Helvetica 14 bold')
        ask_dessert_label['width'] = 60
        answer_frame = MyFrame(ask_dessert_frame, row=1, col=0)
        yes_btn = MyButton(answer_frame, 'Yes', row=0, col=0, command=add_dessert)
        no_btn = MyButton(answer_frame, 'No', row=0, col=2, command=ask_drink)
        last_ask_btn = MyButton(answer_frame, 'Back', row=0, col=1, command=lambda: last_ask(frame))

    def add_side():
        ask_side_frame.destroy()
        extras_window.geometry('670x335')
        # add_side
        global add_side_frame
        global breadsticks
        global garlic_bread
        # open side images
        breadsticks = ImageTk.PhotoImage(Image.open('images/sides/bs.png'))
        garlic_bread = ImageTk.PhotoImage(Image.open('images/sides/gb.png'))
        frame = 'Side'
        add_side_frame = MyFrame(extras_window, row=0, col=0, colspan=3)
        add_side_label = MyLabel(add_side_frame, 'Add sides to your order', row=0, col=0,
                                 font='Helvetica 18 bold')
        add_side_label['width'] = 60
        add_side_label.grid(pady=(5, 10))

        side_images_frame = MyFrame(add_side_frame, row=1, col=0)

        breadsticks_frame = MyLabelFrame(side_images_frame, 'Breadsticks', row=0, col=0,
                                         font='Helvetica 14 bold', padx=20)
        breadsticks_image = MyLabel(breadsticks_frame, '', row=0, col=0, img=breadsticks)
        add_breadsticks = MyButton(side_images_frame, 'Add to Order', row=1, col=0,
                                   command=lambda: add_to_order(items[0]))

        garlic_bread_frame = MyLabelFrame(side_images_frame, 'Garlic Bread', row=0, col=1,
                                          font='Helvetica 14 bold', padx=20)
        garlic_bread_image = MyLabel(garlic_bread_frame, '', row=0, col=0, img=garlic_bread)
        add_garlic_bread = MyButton(side_images_frame, 'Add to Order', row=1, col=1,
                                    command=lambda: add_to_order(items[1]))

        done_btn = MyButton(side_images_frame, 'Done', row=2, col=0, colspan=3, command=lambda: done(frame))
        done_btn['width'] = 6

    def ask_dipping():
        ask_side_frame.destroy()
        # ask add_dipping
        global ask_dipping_frame
        frame = 'Dipping'
        ask_dipping_frame = MyFrame(extras_window, row=0, col=0, colspan=3)
        ask_dipping_frame.grid(pady=(5, 0))
        ask_dipping_label = MyLabel(ask_dipping_frame, 'Would you like to add dipping sauces to your order?', row=0,
                                    col=0, font='Helvetica 14 bold')
        ask_dipping_label['width'] = 60
        answer_frame = MyFrame(ask_dipping_frame, row=1, col=0)
        yes_btn = MyButton(answer_frame, 'Yes', row=0, col=0, command=add_dipping)
        no_btn = MyButton(answer_frame, 'No', row=0, col=2, command=ask_dessert)
        last_ask_btn = MyButton(answer_frame, 'Back', row=0, col=1, command=lambda: last_ask(frame))

    def ask_side():
        # ask add_side
        global ask_side_frame
        frame = 'Side'
        ask_side_frame = MyFrame(extras_window, row=0, col=0, colspan=3)
        ask_side_frame.grid(pady=(5, 0))
        ask_side_label = MyLabel(ask_side_frame, 'Would you like to add sides to your order?', row=0, col=0,
                                 font='Helvetica 14 bold')
        ask_side_label['width'] = 60
        answer_frame = MyFrame(ask_side_frame, row=1, col=0)
        yes_btn = MyButton(answer_frame, 'Yes', row=0, col=0, command=add_side)
        no_btn = MyButton(answer_frame, 'No', row=0, col=2, command=ask_dipping)
        last_ask_btn = MyButton(answer_frame, 'Back', row=0, col=1, command=lambda: last_ask(frame))
        last_ask_btn['state'] = DISABLED

    # 'back' button function
    def back_extras():
        pizza.customize_pizza(pickup, p_size, p_base, your_pizza)  # opens the 'customize_pizza' window (and passes variables)
        extras_window.destroy()

    # 'exit' button function
    def exit_extras():
        p_size.set(0)  # reset 'size' variable (avoid weird behavior)
        p_base = IntVar()  # resent p_base as a tkinter variable (instead of an integer, so it can be reset below)
        p_base.set(0)  # reset 'base' variable (avoid weird behavior)
        your_pizza = None  # reset 'your_pizza' variable (avoid weird behavior)
        custom = False
        changes = None
        order = []
        extras_window.destroy()  # destroy 'extras' window

    # 'next' button function
    def next_payment():
        extras_window.destroy()  # destroy 'base_window' window
        payment.pizza_payment(pickup, p_size, p_base, your_pizza, custom, changes, order)

    ask_side()

    # program navigation
    nav_frame = MyFrame(extras_window, row=1, col=0, colspan=4, sticky=N+S)
    nav_frame.grid(pady=(40, 0))
    back_btn = MyButton(nav_frame, '<< Back', row=0, col=0, command=back_extras)
    exit_btn = MyButton(nav_frame, 'EXIT', row=0, col=1, command=exit_extras)
    next_btn = MyButton(nav_frame, 'Next >>', row=0, col=2, command=next_payment)
    next_btn['state'] = DISABLED

'''
# alt text
# documentation! follow document but line by line comments and docstrings on all functions and modules
# go thru all modules and add 1-line attributes to myGUI objects

print(pickup.get())  # delivery = 0, carry-out = 1
print(p_size.get())  # small = 0, medium = 1, large = 2, xl = 3
print(p_base)  # int = dictionary from pizza.py
print(your_pizza)  # list = based on p_base / customizations made (not reflected by p_base but here) from pizza.py
 '''