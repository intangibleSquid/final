"""
Program: Peter’s Pizza Palace – Priority order-Placement Program v1.0.0 (.py)
Author: Cameron Coy (ccoy2@ivytech.edu)
Description: This is the pizza module for the Peter's Pizza Palace - Priority order-Placement Program. It allows the
user to customize their pizza order as well as selecting from a number of pre-made pizzas.
"""
# import statements
import base  # import previous module (for back button)
import extras  # import next module (for next button)
from myGUI import *  # import my custom tkinter syntax
from PIL import ImageTk, Image  # pip -install Pillow dependency (PIL)


# define 'customize_pizza' function (to create new 'customize_pizza' window)
def customize_pizza(pickup, p_size, p_base, ingredients=None):
    """function to create a new window (pizza customization window)"""
    # create toplevel window
    pizza_window = NewWindow("Create Your Masterpie-zza™", '675x482')
    pizza_window.focus_force()  # force focus on pizza_window

    # store image_paths
    # crust
    hand = 'images/pizza/crust/hand.png'  # hand tossed
    thin = 'images/pizza/crust/thin.png'  # thin & crispy
    # sauce
    red = 'images/pizza/sauce/red.png'  # red sauce
    alf = 'images/pizza/sauce/alf.png'  # alfredo
    bbq = 'images/pizza/sauce/bbq.png'  # BBQ sauce
    # cheese
    mozz = 'images/pizza/cheese/mozz.png'  # mozzarella
    # meat
    pepp = 'images/pizza/meat/pepp.png'  # pepperoni
    ham = 'images/pizza/meat/ham.png'  # ham
    chick = 'images/pizza/meat/chick.png'  # chicken
    bac = 'images/pizza/meat/bac.png'  # bacon
    saus = 'images/pizza/meat/saus.png'  # sausage
    # toppings
    tom = 'images/pizza/toppings/tom.png'  # tomatoes
    spin = 'images/pizza/toppings/spin.png'  # spinach
    mush = 'images/pizza/toppings/mush.png'  # mushrooms
    gp = 'images/pizza/toppings/gp.png'  # bell peppers
    oni = 'images/pizza/toppings/oni.png'  # onions
    bo = 'images/pizza/toppings/bo.png'  # black olives
    pine = 'images/pizza/toppings/pine.png'  # pineapple
    # seasoning
    mg = 'images/pizza/seasoning/mg.png'  # minced garlic
    pc = 'images/pizza/seasoning/pc.png'  # parmesan
    bbqd = 'images/pizza/seasoning/bbqd.png'  # bbq drizzle

    # ingredient dictionaries {key: ('label', image_path)}
    crusts = {0: ('Hand Tossed', hand),
              1: ('Thin & Crispy', thin)}

    sauces = {0: ('Red Sauce', red),
              1: ('Alfredo', alf),
              2: ('BBQ Sauce', bbq)}

    cheeses = {1: ('Mozzarella', mozz)}

    meats = {1: ('Pepperoni', pepp),
             2: ('Ham', ham),
             3: ('Chicken', chick),
             4: ('Bacon', bac),
             5: ('Sausage', saus)}

    toppings = {1: ('Tomatoes', tom),
                2: ('Spinach', spin),
                3: ('Mushrooms', mush),
                4: ('Bell Peppers', gp),
                5: ('Onions', oni),
                6: ('Black Olives', bo),
                7: ('Pineapples', pine)}

    seasonings = {1: ('Minced Garlic', mg),
                  2: ('Parmesan', pc),
                  3: ('BBQ Drizzle', bbqd)}

    # base pizza template dictionaries {key = p_base: ('Pizza Name', (ingredients = (dictionary, index)))}
    base_pizza = {0: ('Cheese Pizza', ((crusts, 0), (sauces, 0), (cheeses, 1), (seasonings, 2))),
                  1: ('Pepperoni Pizza', ((crusts, 0), (sauces, 0), (cheeses, 1), (meats, 1))),
                  2: ('Sausage Pizza', ((crusts, 0), (sauces, 0), (cheeses, 1), (meats, 5))),
                  3: ('Supreme Pizza', ((crusts, 0), (sauces, 0), (cheeses, 1), (meats, (1, 5)),
                                        (toppings, (3, 4, 5, 6)))),
                  4: ('Meat-za™ Pizza', ((crusts, 0), (sauces, 0), (cheeses, 1), (seasonings, 1),
                                         (meats, (1, 2, 4, 5)), (seasonings, 2))),
                  5: ('Chicken Alfredo Pizza', ((crusts, 0), (sauces, 1), (cheeses, 1), (seasonings, 1),
                                                (toppings, (2, 1)), (meats, 3), (seasonings, 2))),
                  6: ('Hawaiian Pizza', ((crusts, 0), (sauces, 0), (cheeses, 1), (meats, 2), (toppings, 7))),
                  7: ('BBQ Chicken Pizza', ((crusts, 0), (sauces, 2), (cheeses, 1), (toppings, 5),
                                            (meats, (4, 3)), (seasonings, 3)))}

    # initialize check / radio button control variables
    global custom  # track if pizza has been changed from p_base template
    global changes  # track changed meats, toppings, and seasonings (for payment.py)
    global crust  # global crust variable
    global sauce  # global sauce variable
    global pizza_image  # global pizza_image variable
    custom = False  # default state (pizza hasn't been changed from template)
    changes = {'meats': 0, 'toppings': 0, 'seasonings': 0}  # track count of added or removed items (for payment)
    crust = IntVar()  # crust variable (radio button)
    sauce = IntVar()  # sauce variable (radio button)
    cheese = IntVar()  # cheese variable (check button)
    meat1 = IntVar()  # meat variable (check button) (pepperoni)
    meat2 = IntVar()  # meat variable (check button) (ham)
    meat3 = IntVar()  # meat variable (check button) (chicken)
    meat4 = IntVar()  # meat variable (check button) (bacon)
    meat5 = IntVar()  # meat variable (check button) (sausage)
    meat = [meat1, meat2, meat3, meat4, meat5]  # meat variables list (check buttons) (for iteration)
    topping1 = IntVar()  # topping variable (check button) (tomatoes)
    topping2 = IntVar()  # topping variable (check button) (spinach)
    topping3 = IntVar()  # topping variable (check button) (mushrooms)
    topping4 = IntVar()  # topping variable (check button) (green peppers)
    topping5 = IntVar()  # topping variable (check button) (onions)
    topping6 = IntVar()  # topping variable (check button) (black olives)
    topping7 = IntVar()  # topping variable (check button) (pineapples)
    topping = [topping1, topping2, topping3, topping4, topping5, topping6, topping7]  # topping vars list (check btns)..
    seasoning1 = IntVar()  # seasoning variable (check button) (minced garlic)
    seasoning2 = IntVar()  # seasoning variable (check button) (parmesan cheese)
    seasoning3 = IntVar()  # seasoning variable (check button) (bbq drizzle)
    seasoning = [seasoning1, seasoning2, seasoning3]  # seasoning variables list (check buttons) (for iteration)

    def generate_ingredients(p_base):
        """Generates ingredient list from the pizza base"""
        global your_p_name  # global 'pizza name' variable (for labels outside of function)
        if ingredients is None:
            # build ingredient_list from p_base template selection
            if p_base < 8:  # customize pizza from template
                index = p_base  # value from p_base as 'base_pizza' index
                your_base = base_pizza[index]  # key-value pair from template dictionary
                your_p_name = your_base[0]  # pizza base template's name
                your_pizza = your_base[1]  # pizza base template's ingredients
            else:  # customize pizza from scratch
                your_p_name = 'No Base (From Scratch)'  # custom pizza's name (no base / from scratch)
                your_pizza = ((crusts, 0), (sauces, 0))  # custom pizza's ingredients (crust and sauce only)
            ingredient_list = []  # initialize list of ingredients for check / radio buttons & pizza_image
            for item in your_pizza:  # iterate through ingredients for formatting
                dictionary = item[0]  # dictionary name for ingredient (sauces, crusts, etc.)
                dict_key = item[1]  # dictionary index for ingredients (to pass to specific dictionary)
                if type(dict_key) is tuple:  # more than one type of ingredient? (many meats, many toppings, etc.)
                    key_index = 0  # ingredient dictionary index
                    for key in dict_key:  # iterate through ingredient dictionary keys
                        ingredient_list.append(dictionary[int(dict_key[key_index])])  # add ingredients to ingredient_list
                        key_index += 1  # increment dictionary index key
                else:  # only one ingredient of dictionary type?
                    ingredient_list.append(dictionary[int(dict_key)])  # add ingredient to ingredient_list
        else:
             ingredient_list = ingredients
        return ingredient_list

    # convert p_base from previous window to ingredient list
    ingredients = generate_ingredients(p_base)

    def set_selection(ingredient_list):
        """Sets the selected buttons based on the ingredient list"""
        # set check / radio buttons based on ingredient_list (and build image_path list from ingredient_list)
        for ingredient in ingredient_list:  # iterate through ingredient and image_path in ingredient_list
            for item in crusts.items():  # check if ingredient is in crusts
                value = item[1]  # ingredient (index: 0) and image_path (index: 1) (removes dictionary key from item)
                if str(ingredient[0]) == value[0]:  # compare ingredient's name to dictionary value's name
                    # print(f'Found Crust: {ingredient}')  # console output for testing (ingredient's dictionary)
                    # print(f'Item Key: {item[0]}')  # console output for testing (ingredient's dictionary index)
                    crust.set(int(item[0]))  # when ingredient is found, set radio / check button's value
            for item in sauces.items():  # check if ingredient is in sauces
                value = item[1]  # ingredient (index: 0) and image_path (index: 1) (removes dictionary key from item)
                if str(ingredient[0]) == value[0]:  # compare ingredient's name to dictionary value's name
                    # print(f'Found Sauce: {ingredient}')  # console output for testing (ingredient's dictionary)
                    # print(f'Item Key: {item[0]}')  # console output for testing (ingredient's dictionary index)
                    sauce.set(int(item[0]))  # when ingredient is found, set radio / check button's value
            for item in cheeses.items():  # check if ingredient is in cheeses
                value = item[1]  # ingredient (index: 0) and image_path (index: 1) (removes dictionary key from item)
                if str(ingredient[0]) == value[0]:  # compare ingredient's name to dictionary value's name
                    # print(f'Found Cheese: {ingredient}')  # console output for testing (ingredient's dictionary)
                    # print(f'Item Key: {item[0]}')  # console output for testing (ingredient's dictionary index)
                    cheese.set(int(item[0]))  # when ingredient is found, set radio / check button's value
            for item in meats.items():  # check if ingredient is in meats
                value = item[1]  # ingredient (index: 0) and image_path (index: 1) (removes dictionary key from item)
                if str(ingredient[0]) == value[0]:  # compare ingredient's name to dictionary value's name
                    # print(f'Found Meat: {ingredient}')  # console output for testing (ingredient's dictionary)
                    # print(f'Item Key: {item[0]}')  # console output for testing (ingredient's dictionary index)
                    meat[(int(item[0]) - 1)].set(1)  # when ingredient is found, set radio / check button's value
            for item in toppings.items():  # check if ingredient is in toppings
                value = item[1]  # ingredient (index: 0) and image_path (index: 1) (removes dictionary key from item)
                if str(ingredient[0]) == value[0]:  # compare ingredient's name to dictionary value's name
                    # print(f'Found Topping: {ingredient}')  # console output for testing (ingredient's dictionary)
                    # print(f'Item Key: {item[0]}')  # console output for testing (ingredient's dictionary index)
                    topping[(int(item[0]) - 1)].set(1)  # when ingredient is found, set radio / check button's value
            for item in seasonings.items():  # check if ingredient is in seasonings
                value = item[1]  # ingredient (index: 0) and image_path (index: 1) (removes dictionary key from item)
                if str(ingredient[0]) == value[0]:  # compare ingredient's name to dictionary value's name
                    # print(f'Found Seasoning: {ingredient}')  # console output for testing (ingredient's dictionary)
                    # print(f'Item Key: {item[0]}')  # console output for testing (ingredient's dictionary index)
                    seasoning[int(item[0]) - 1].set(1)  # when ingredient is found, set radio / check button's value

    def get_image_list(ingredient_list):
        """Creates the image_path list to build the pizza image"""
        images = []  # initialize image_path list to build pizza_image
        for image_path in ingredient_list:
            images.append(image_path[1])  # add ingredient's image_path to images list
        return images

    # set selection (from p_base)
    set_selection(ingredients)

    # generate image_list from selection
    image_list = get_image_list(ingredients)

    def create_image(images):
        """Builds pizza image from the image_path list"""
        # create pizza_image from images (image_path list)
        index = 0  # sentinel value (loop control variable and images list index)
        intermediate = Image.open(images[index])  # open the first image in the images list
        while index < len(images) - 1:  # loop until we reach the end of the images list
            image1 = intermediate  # initialize intermediate image from outside loop or end of previous iteration
            index += 1  # increment images list index / sentinel control variable
            image2 = Image.open(images[index])  # open the next image (to layer on the first or intermediate image)
            intermediate = Image.alpha_composite(image1, image2)  # intermediate image: image1 (bottom) + image2 (top)
        final = ImageTk.PhotoImage(intermediate)  # post-composite image combination, save resulting image as tkinter image
        return final

    # create pizza_image from image_list
    pizza_image = create_image(image_list)

    # 'pizza_image' section
    pizza_img_frame = MyLabelFrame(pizza_window, your_p_name, row=0, col=1, rowspan=3, bd=6, font='Helvetica 18 bold')
    pizza_img_frame['relief'] = GROOVE  # pizza_image frame (above) and 'groove' relief style
    pizza_img_label = MyLabel(pizza_img_frame, '', row=0, col=0,
                              img=pizza_image)  # pizza_image (displayed with a label)

    def update_seasoning(value):  # seasoning only
        """Updates a seasoning from a check box toggle"""
        global pizza_image  # make pizza_image global
        global custom  # make custom global
        # update ingredients_list
        item = seasonings[value]
        # check if topping already exists (logic is reversed because value updates when clicked)
        if seasoning[value - 1].get() == 0:
            item = seasonings[value]
            ingredients.remove(item)  # remove meat from ingredients
            changes['seasonings'] -= 1
        else:
            changes['seasonings'] += 1
            if value < 2:
                ingredients.insert(3, item)  # add new meat to ingredients
            else:
                ingredients.insert(16, item)  # puts larger toppings under smaller toppings
        # generate new image_list
        image_list = get_image_list(ingredients)
        # create new pizza_image from update image_list
        pizza_image = create_image(image_list)
        pizza_img_label = MyLabel(pizza_img_frame, '', row=0, col=0, img=pizza_image)  # updated pizza_image
        custom = True

    def update_topping(value):  # toppings only
        """Updates a topping from a check box toggle"""
        global pizza_image
        global custom
        # update ingredients_list
        item = toppings[value]
        # check if topping already exists (logic is reversed because value updates when clicked)
        if topping[value - 1].get() == 0:
            item = toppings[value]
            ingredients.remove(item)  # remove meat from ingredients
            changes['toppings'] -= 1
        else:
            changes['toppings'] += 1
            if value > 2:
                ingredients.append(item)  # add new meat to ingredients
            else:
                ingredients.insert(4, item)  # puts larger toppings under smaller toppings
        # generate new image_list
        image_list = get_image_list(ingredients)
        # create new pizza_image from update image_list
        pizza_image = create_image(image_list)
        pizza_img_label = MyLabel(pizza_img_frame, '', row=0, col=0, img=pizza_image)  # updated pizza_image
        custom = True

    def update_meat(value):  # meats only
        """Updates a meat from a check box toggle"""
        global pizza_image
        global custom
        # update ingredients_list
        item = meats[value]
        # check if meat already exists (logic is reversed because value updates when clicked)
        if meat[value - 1].get() == 0:
            item = meats[value]
            ingredients.remove(item)  # remove meat from ingredients
            changes['meats'] -= 1
        else:
            changes['meats'] += 1
            if value > 1:
                ingredients.append(item)  # add new meat to ingredients
            else:
                ingredients.insert(3, item)  # puts larger toppings under smaller toppings
        # generate new image_list
        image_list = get_image_list(ingredients)
        # create new pizza_image from update image_list
        pizza_image = create_image(image_list)
        pizza_img_label = MyLabel(pizza_img_frame, '', row=0, col=0, img=pizza_image)  # updated pizza_image
        custom = True

    def update_cheese(value):  # cheese only
        """Updates cheese from a check box toggle"""
        global pizza_image
        # update ingredients_list
        item = cheeses[value]
        # check if cheese already exists (logic is reversed because value updates when clicked)
        if cheese.get() == 0:
            item = cheeses[value]
            ingredients.remove(item)  # remove cheese from ingredients
        else:
            ingredients.insert(2, item)  # add cheese to ingredients
        # generate new image_list
        image_list = get_image_list(ingredients)
        # create new pizza_image from update image_list
        pizza_image = create_image(image_list)
        pizza_img_label = MyLabel(pizza_img_frame, '', row=0, col=0, img=pizza_image)  # updated pizza_image

    def update_sauce(value):  # sauces only
        """Updates sauce from a radio button press"""
        global pizza_image
        # update ingredients_list
        ingredients[1] = sauces[value]  # replace crust with updated selection
        # generate new image_list
        image_list = get_image_list(ingredients)
        # create new pizza_image from update image_list
        pizza_image = create_image(image_list)
        pizza_img_label = MyLabel(pizza_img_frame, '', row=0, col=0, img=pizza_image)  # updated pizza_image

    # crust
    def update_crust(value):  # crusts only
        """Updates crust from a radio button press"""
        global pizza_image
        # update ingredients_list
        ingredients[0] = crusts[value]  # replace crust with updated selection
        # generate new image_list
        image_list = get_image_list(ingredients)
        # create new pizza_image from update image_list
        pizza_image = create_image(image_list)
        pizza_img_label = MyLabel(pizza_img_frame, '', row=0, col=0, img=pizza_image)  # updated pizza_image

    # 'customize pizza' section headings
    heading_frame = MyFrame(pizza_window, row=0, col=0, sticky=N+S+W+E)  # headings frame
    heading_frame['padx'] = 2  # give the heading's frame 5px padding (x-axis)
    heading_label = MyLabel(heading_frame, 'Create Your Masterpie-zza™', row=0, col=0, sticky=W,
                            font=('Helvetica', 18, 'bold', 'underline'))  # 'customize pizza' section heading
    p_name_label = MyLabel(heading_frame, f'Base: {your_p_name}', row=1, col=0, sticky=W,
                           font=('Helvetica', 16, 'bold', 'italic'))  # base pizza template name's heading

    # 'select ingredients' section
    ingredients_frame = MyFrame(pizza_window, row=1, col=0)  # 'select ingredients' section frame
    ingredients_label = MyLabel(ingredients_frame, 'Select Your Ingredients:', row=0, col=0, colspan=2,
                                font=('Helvetica', 16, 'bold', 'underline'), sticky=W)  # 'select ingredients' heading
    ingredients_label.grid(padx=(2, 0))  # give 'select ingredients' heading 2px padding (left side)

    # 'crust selection' section
    crust_frame = MyLabelFrame(ingredients_frame, "Crust", row=1, col=0, sticky=W+E, bd=3, font='Helvetica 14 bold',
                               padx=4, pady=(0, 5))  # crust selection frame
    hand_btn = MyRadio(crust_frame, 'Hand Tossed', row=0, col=0, sticky=W, var=crust, val=0,
                       command=lambda: update_crust(0))  # hand tossed button
    thin_btn = MyRadio(crust_frame, 'Thin & Crispy', row=1, col=0, sticky=W, var=crust, val=1,
                       command=lambda: update_crust(1))  # thin & crispy button

    # 'sauce selection' section
    sauce_frame = MyLabelFrame(ingredients_frame, "Sauce", row=2, col=0, sticky=W+E, bd=3, font='Helvetica 14 bold',
                               padx=4, pady=(0, 5))  # sauce selection frame
    red_btn = MyRadio(sauce_frame, "Red Sauce", row=0, col=0, sticky=W, var=sauce, val=0,
                      command=lambda: update_sauce(0))  # red sauce button
    alfredo_btn = MyRadio(sauce_frame, "Alfredo Sauce", row=1, col=0, sticky=W, var=sauce, val=1,
                          command=lambda: update_sauce(1))  # alfredo button
    bbq_btn = MyRadio(sauce_frame, "BBQ Sauce", row=2, col=0, sticky=W, var=sauce, val=2,
                      command=lambda: update_sauce(2))  # bbq sauce button

    # 'cheese selection' section
    cheese_frame = MyLabelFrame(ingredients_frame, "Cheese", row=3, col=0, sticky=N+S+W+E, bd=3,
                                font='Helvetica 14 bold', padx=4, pady=(0, 5))  # cheese selection frame
    mozz_btn = MyCheck(cheese_frame, "Mozzarella", row=0, col=0, sticky=W, var=cheese,
                       command=lambda: update_cheese(1))  # mozzarella button

    # 'meat selection' section
    meat_frame = MyLabelFrame(ingredients_frame, "Meats", row=4, col=0, sticky=N+S+W+E, bd=3, font='Helvetica 14 bold',
                              padx=4, pady=(0, 5))  # meat selection frame
    pepp_btn = MyCheck(meat_frame, "Pepperoni", row=0, col=0, sticky=W, var=meat[0],
                       command=lambda: update_meat(1))  # pepperoni button
    ham_btn = MyCheck(meat_frame, "Ham", row=1, col=0, sticky=W, var=meat[1],
                      command=lambda: update_meat(2))  # ham button
    chick_btn = MyCheck(meat_frame, "Chicken", row=2, col=0, sticky=W, var=meat[2],
                        command=lambda: update_meat(3))  # chicken button
    bac_btn = MyCheck(meat_frame, "Bacon", row=3, col=0, sticky=W, var=meat[3],
                      command=lambda: update_meat(4))  # bacon button
    saus_btn = MyCheck(meat_frame, "Sausage", row=4, col=0, sticky=W, var=meat[4],
                       command=lambda: update_meat(5))  # sausage button

    # 'topping selection' section
    topping_frame = MyLabelFrame(ingredients_frame, "Toppings", row=1, col=1, rowspan=3, sticky=N+S+W+E, bd=3,
                                 font='Helvetica 14 bold', padx=4, pady=(0, 5))  # topping selection frame
    tom_btn = MyCheck(topping_frame, "Tomatoes", row=0, col=0, sticky=W, var=topping[0],
                      command=lambda: update_topping(1))  # tomatoes button
    spin_btn = MyCheck(topping_frame, "Spinach", row=1, col=0, sticky=W, var=topping[1],
                       command=lambda: update_topping(2))  # spinach button
    mush_btn = MyCheck(topping_frame, "Mushrooms", row=2, col=0, sticky=W, var=topping[2],
                       command=lambda: update_topping(3))  # mushrooms button
    gp_btn = MyCheck(topping_frame, "Bell Peppers", row=3, col=0, sticky=W, var=topping[3],
                     command=lambda: update_topping(4))  # bell peppers button
    oni_btn = MyCheck(topping_frame, "Onions", row=4, col=0, sticky=W, var=topping[4],
                      command=lambda: update_topping(5))  # onions button
    bo_btn = MyCheck(topping_frame, "Black Olives", row=5, col=0, sticky=W, var=topping[5],
                     command=lambda: update_topping(6))  # black olives button
    pine_btn = MyCheck(topping_frame, "Pineapples", row=6, col=0, sticky=W, var=topping[6],
                       command=lambda: update_topping(7))  # pineapples button

    # 'seasoning selection' section
    seasoning_frame = MyLabelFrame(ingredients_frame, "Seasoning", row=4, col=1, sticky=N+S+W+E, bd=3,
                                   font='Helvetica 14 bold', padx=4, pady=(0, 5))  # seasoning selection frame
    mg_btn = MyCheck(seasoning_frame, "Minced Garlic", row=0, col=0, sticky=W, var=seasoning[0],
                     command=lambda: update_seasoning(1))  # minced garlic button
    pc_btn = MyCheck(seasoning_frame, "Parmesan", row=1, col=0, sticky=W, var=seasoning[1],
                     command=lambda: update_seasoning(2))  # parmesan button
    bbqd_btn = MyCheck(seasoning_frame, "BBQ Drizzle", row=2, col=0, sticky=W, var=seasoning[2],
                       command=lambda: update_seasoning(3))  # bbq drizzle button

    # 'back' button function
    def back_pizza():
        """Loads the previous module and destroys the current window (also passes variables on to the that module)"""
        base.pizza_base(pickup, p_size)  # go back to previous module
        pizza_window.destroy()  # destroy this window

    # 'exit' button function
    def exit_pizza():
        """Exits the current window and resets variables"""
        p_size.set(0)  # reset 'size' variable (avoid weird behavior)
        p_base = IntVar()  # resent p_base as a tkinter variable (instead of an integer, so it can be reset below)
        p_base.set(0)  # reset 'base' variable (avoid weird behavior)
        pizza_window.destroy()  # destroy 'base_window' window

    # 'next' button function
    def next_extras():
        """Loads the next module and destroys the current window (also passes variables on to the next module)"""
        pizza_window.destroy()  # destroy 'base_window' window
        if custom is True:
            extras.add_extras(pickup, p_size, p_base, ingredients, custom, changes)  # passes variables to the next module (to add extras)
        else:
            extras.add_extras(pickup, p_size, p_base, ingredients)  # passes variables to the next module (to add extras)

    # program navigation
    nav_frame = MyFrame(pizza_window, row=5, col=0, colspan=4, sticky=N+S)  # navigation frame
    back_btn = MyButton(nav_frame, '<< Back', row=0, col=0, command=back_pizza)  # back button
    exit_btn = MyButton(nav_frame, 'EXIT', row=0, col=1, command=exit_pizza)  # exit button
    next_btn = MyButton(nav_frame, 'Next >>', row=0, col=2, command=next_extras)  # next button
