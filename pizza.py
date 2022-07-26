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
    pizza_window = NewWindow("Create Your Masterpie-zza™", '675x460')

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

    # set check / radio buttons based on ingredient_list (and build image_path list from ingredient_list)
    images = []  # initialize image_path list to build pizza_image
    for ingredient, image_path in ingredient_list:  # iterate through ingredient and image_path in ingredient_list
        for item in crusts.items():  # check if ingredient is in crusts
            value = item[1]  # ingredient (index: 0) and image_path (index: 1) (removes dictionary key from item)
            if str(ingredient) == value[0]:  # compare ingredient's name to dictionary value's name
                # print(f'Found Crust: {ingredient}')  # console output for testing (ingredient's dictionary)
                # print(f'Item Key: {item[0]}')  # console output for testing (ingredient's dictionary index)
                crust.set(int(item[0]))  # when ingredient is found, set radio / check button's value
        for item in sauces.items():  # check if ingredient is in sauces
            value = item[1]  # ingredient (index: 0) and image_path (index: 1) (removes dictionary key from item)
            if str(ingredient) == value[0]:  # compare ingredient's name to dictionary value's name
                # print(f'Found Sauce: {ingredient}')  # console output for testing (ingredient's dictionary)
                # print(f'Item Key: {item[0]}')  # console output for testing (ingredient's dictionary index)
                sauce.set(int(item[0]))  # when ingredient is found, set radio / check button's value
        for item in cheeses.items():  # check if ingredient is in cheeses
            value = item[1]  # ingredient (index: 0) and image_path (index: 1) (removes dictionary key from item)
            if str(ingredient) == value[0]:  # compare ingredient's name to dictionary value's name
                # print(f'Found Cheese: {ingredient}')  # console output for testing (ingredient's dictionary)
                # print(f'Item Key: {item[0]}')  # console output for testing (ingredient's dictionary index)
                cheese.set(int(item[0]))  # when ingredient is found, set radio / check button's value
        for item in meats.items():  # check if ingredient is in meats
            value = item[1]  # ingredient (index: 0) and image_path (index: 1) (removes dictionary key from item)
            if str(ingredient) == value[0]:  # compare ingredient's name to dictionary value's name
                # print(f'Found Meat: {ingredient}')  # console output for testing (ingredient's dictionary)
                # print(f'Item Key: {item[0]}')  # console output for testing (ingredient's dictionary index)
                meat[(int(item[0]) - 1)].set(1)  # when ingredient is found, set radio / check button's value
        for item in toppings.items():  # check if ingredient is in toppings
            value = item[1]  # ingredient (index: 0) and image_path (index: 1) (removes dictionary key from item)
            if str(ingredient) == value[0]:  # compare ingredient's name to dictionary value's name
                # print(f'Found Topping: {ingredient}')  # console output for testing (ingredient's dictionary)
                # print(f'Item Key: {item[0]}')  # console output for testing (ingredient's dictionary index)
                topping[(int(item[0]) - 1)].set(1)  # when ingredient is found, set radio / check button's value
        for item in seasonings.items():  # check if ingredient is in seasonings
            value = item[1]  # ingredient (index: 0) and image_path (index: 1) (removes dictionary key from item)
            if str(ingredient) == value[0]:  # compare ingredient's name to dictionary value's name
                # print(f'Found Seasoning: {ingredient}')  # console output for testing (ingredient's dictionary)
                # print(f'Item Key: {item[0]}')  # console output for testing (ingredient's dictionary index)
                seasoning[int(item[0]) - 1].set(1)  # when ingredient is found, set radio / check button's value
        images.append(image_path)  # add ingredient's image_path to images list

    # build pizza_image from images (image_path list)
    index = 0  # sentinel value (loop control variable and images list index)
    intermediate = Image.open(images[index])  # open the first image in the images list
    while index < len(images) - 1:  # loop until we reach the end of the images list
        image1 = intermediate  # initialize intermediate image from outside loop or end of previous iteration
        index += 1  # increment images list index / sentinel control variable
        image2 = Image.open(images[index])  # open the next image (to layer on the first or intermediate image)
        intermediate = Image.alpha_composite(image1, image2)  # intermediate image: image1 (bottom) + image2 (top)
    final = ImageTk.PhotoImage(intermediate)  # post-composite image combination, save resulting image as tkinter image

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
    hand_btn = MyRadio(crust_frame, 'Hand Tossed', row=0, col=0, sticky=W, var=crust, val=0)  # hand tossed button
    thin_btn = MyRadio(crust_frame, 'Thin & Crispy', row=1, col=0, sticky=W, var=crust, val=1)  # thin & crispy button

    # 'sauce selection' section
    sauce_frame = MyLabelFrame(ingredients_frame, "Sauce", row=2, col=0, sticky=W+E, bd=3, font='Helvetica 14 bold',
                               padx=4, pady=(0, 5))  # sauce selection frame
    red_btn = MyRadio(sauce_frame, "Red Sauce", row=0, col=0, sticky=W, var=sauce, val=0)  # red sauce button
    alfredo_btn = MyRadio(sauce_frame, "Alfredo Sauce", row=1, col=0, sticky=W, var=sauce, val=1)  # alfredo button
    bbq_btn = MyRadio(sauce_frame, "BBQ Sauce", row=2, col=0, sticky=W, var=sauce, val=2)  # bbq sauce button

    # 'cheese selection' section
    cheese_frame = MyLabelFrame(ingredients_frame, "Cheese", row=3, col=0, sticky=N+S+W+E, bd=3,
                                font='Helvetica 14 bold', padx=4, pady=(0, 5))  # cheese selection frame
    mozz_btn = MyCheck(cheese_frame, "Mozzarella", row=0, col=0, sticky=W, var=cheese)  # mozzarella button

    # 'meat selection' section
    meat_frame = MyLabelFrame(ingredients_frame, "Meats", row=4, col=0, sticky=N+S+W+E, bd=3, font='Helvetica 14 bold',
                              padx=4, pady=(0, 5))  # meat selection frame
    pepp_btn = MyCheck(meat_frame, "Pepperoni", row=0, col=0, sticky=W, var=meat[0])  # pepperoni button
    ham_btn = MyCheck(meat_frame, "Ham", row=1, col=0, sticky=W, var=meat[1])  # ham button
    chick_btn = MyCheck(meat_frame, "Chicken", row=2, col=0, sticky=W, var=meat[2])  # chicken button
    bac_btn = MyCheck(meat_frame, "Bacon", row=3, col=0, sticky=W, var=meat[3])  # bacon button
    saus_btn = MyCheck(meat_frame, "Sausage", row=4, col=0, sticky=W, var=meat[4])  # sausage button

    # 'topping selection' section
    topping_frame = MyLabelFrame(ingredients_frame, "Toppings", row=1, col=1, rowspan=3, sticky=N+S+W+E, bd=3,
                                 font='Helvetica 14 bold', padx=4, pady=(0, 5))  # topping selection frame
    tom_btn = MyCheck(topping_frame, "Tomatoes", row=0, col=0, sticky=W, var=topping[0])  # tomatoes button
    spin_btn = MyCheck(topping_frame, "Spinach", row=1, col=0, sticky=W, var=topping[1])  # spinach button
    mush_btn = MyCheck(topping_frame, "Mushrooms", row=2, col=0, sticky=W, var=topping[2])  # mushrooms button
    gp_btn = MyCheck(topping_frame, "Bell Peppers", row=3, col=0, sticky=W, var=topping[3])  # bell peppers button
    oni_btn = MyCheck(topping_frame, "Onions", row=4, col=0, sticky=W, var=topping[4])  # onions button
    bo_btn = MyCheck(topping_frame, "Black Olives", row=5, col=0, sticky=W, var=topping[5])  # black olives button
    pine_btn = MyCheck(topping_frame, "Pineapples", row=6, col=0, sticky=W, var=topping[6])  # pineapples button

    # 'seasoning selection' section
    seasoning_frame = MyLabelFrame(ingredients_frame, "Seasoning", row=4, col=1, sticky=N+S+W+E, bd=3,
                                   font='Helvetica 14 bold', padx=4, pady=(0, 5))  # seasoning selection frame
    mg_btn = MyCheck(seasoning_frame, "Minced Garlic", row=0, col=0, sticky=W, var=seasoning[0])  # minced garlic button
    pc_btn = MyCheck(seasoning_frame, "Parmesan", row=1, col=0, sticky=W, var=seasoning[1])  # parmesan button
    bbqd_btn = MyCheck(seasoning_frame, "BBQ Drizzle", row=2, col=0, sticky=W, var=seasoning[2])  # bbq drizzle button

    # 'pizza_image' section
    pizza_img_frame = MyLabelFrame(pizza_window, your_p_name, row=0, col=1, rowspan=3, bd=6, font='Helvetica 18 bold')
    pizza_img_frame['relief'] = GROOVE  # pizza_image frame (above) and 'groove' relief style
    pizza_img_label = MyLabel(pizza_img_frame, '', row=0, col=0, img=final)  # pizza_image (displayed with a label)

    # navigation buttons (add)

    '''
    TO DO:
    # + custom if edited ingred
    # line up GUI and fix interfaces
    # define functions and buttons to fix interfaces
    
    # not quite proper logic but correct bulding
    # SO FIX LOGIC, FORMATTING / READABILITY and checkbox interactions
    # img_label = MyLabel(ingredients_frame, '', row=0, col=2, img=p_final)

    # set_buttons(your_pizza)
    # command for live pizza refreshing
    # documentation
    # final modules and final steps
    # custom label when you click a button (+ custom)
    # pass other variables through to next function
    # ingredients list and image generator as functions?
    # create functions and call them in proper places
    # add label above (window title = label) (above pizza name header: create your custom pizza or something tool)

    # GO BACK THRU AND DOCUMENT ALL MODULES AND LINES CHECK FOR ERRORS AND TYPOS
    # extra or half options?
    # alt text / labels and non-viusual representation
    # text area or label with ingredients list?
    # refresh_btn = MyButton(ingredients_frame, 'Refresh', row=6, col=0, colspan=4, command=refresh_za)
    # buttons and navigation?
    '''

    '''
    Examples / TODO:
    
        def refresh_za():
        return
    
    # need function to set button on/off values based on base pizza selection
    def set_buttons(options):


    # radio button 'live refresh' function (as values change, refresh in realtime)
    def refresh_radio():
        return

    # check button 'live refresh' function (as values change, refresh in realtime)
    def refresh_check():
        return
    '''

    pizza_window.mainloop()

customize_pizza(1, 2, 3)

