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
    pizza_window = NewWindow("Create Your Masterpie-zza™", '660x460')

    """# define 'RGBAImage' function (creates 'Alpha Layer' for images)
    def RBGAImage(path):
        return Image.open(path).convert("RGBA")"""

    # open images
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
    gp = 'images/pizza/toppings/gp.png'  # green peppers
    oni = 'images/pizza/toppings/oni.png'  # onions
    bo = 'images/pizza/toppings/bo.png'  # black olives
    pine = 'images/pizza/toppings/pine.png'  # pineapple
    # seasoning
    mg = 'images/pizza/seasoning/mg.png'  # minced garlic
    pc = 'images/pizza/seasoning/pc.png'  # parmesan cheese
    bbqd = 'images/pizza/seasoning/bbqd.png'  # bbq drizzle

    # ingredient dictionaries {key: ('label', image)}
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
                4: ('Green Peppers', gp),
                5: ('Onions', oni),
                6: ('Black Olives', bo),
                7: ('Pineapples', pine)}

    seasonings = {1: ('Minced Garlic', mg),
                  2: ('Parmesan Cheese', pc),
                  3: ('BBQ Drizzle', bbqd)}

    # base pizza template dictionaries {key | p_base: ('Pizza Name', (ingredients))}
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

    # button variables
    crust = IntVar()
    sauce = IntVar()
    cheese = IntVar()
    meat1 = IntVar()
    meat2 = IntVar()
    meat3 = IntVar()
    meat4 = IntVar()
    meat5 = IntVar()
    meat = [meat1, meat2, meat3, meat4, meat5]
    topping1 = IntVar()
    topping2 = IntVar()
    topping3 = IntVar()
    topping4 = IntVar()
    topping5 = IntVar()
    topping6 = IntVar()
    topping7 = IntVar()
    topping = [topping1, topping2, topping3, topping4, topping5, topping6, topping7]
    seasoning1 = IntVar()
    seasoning2 = IntVar()
    seasoning3 = IntVar()
    seasoning = [seasoning1, seasoning2, seasoning3]

    # your Masterpie-zza™ (custom pizza)
    if p_base < 8:
        index = p_base  # value from p_base as 'base_pizza' index
        your_base = base_pizza[index]
        # print(your_base)
        your_p_name = your_base[0]
        your_pizza = your_base[1]
    else:  # from scratch
        your_p_name = 'Your Masterpie-zza™'  # custom pizza's name
        your_pizza = ((crusts, 0), (sauces, 0))  # custom pizza's ingredients
    ingredient_list = []
    for item in your_pizza:
        dictionary = item[0]
        dict_key = item[1]
        # print(type(dict_key))
        if type(dict_key) is tuple:
            print(dict_key)
            key_index = 0
            for key in dict_key:
                ingredient_list.append(dictionary[int(dict_key[key_index])])
                key_index += 1
        else:
            ingredient_list.append(dictionary[int(dict_key)])
        # print(dictionary)
        # print(dict_key)
    #print(ingredient_list)
    # print(your_p_name)
    # print(your_pizza[0])
    # print(ingredient_list)
    # still need from scratch else: above


    # set buttons on / off based on template pizza
    for x, y in ingredient_list:
        for item in crusts.items():
            # print(x)
            # print(y)
            z = item[1]
            if str(x) == z[0]:
                #print(f'found crust {x}')
                #print(f'key: {item[0]}')
                crust.set(int(item[0]))
        for item in sauces.items():
            # print(x)
            z = item[1]
            if str(x) == z[0]:
                #print(f'found sauce {x}')
                #print(f'key: {item[0]}')
                sauce.set(int(item[0]))
        for item in cheeses.items():
            # print(x)
            z = item[1]
            if str(x) == z[0]:
                #print(f'found cheese {x}')
                #print(f'key: {item[0]}')
                cheese.set(int(item[0]))
        for item in meats.items():
            # print(x)
            z = item[1]
            if str(x) == z[0]:
                #print(f'found meat {x}')
                #print(f'key: {item[0]}')
                meat[(int(item[0]) - 1)].set(1)
        for item in toppings.items():
            # print(x)
            z = item[1]
            if str(x) == z[0]:
                #print(f'found topping {x}')
                #print(f'key: {item[0]}')
                topping[(int(item[0]) - 1)].set(1)
        for item in seasonings.items():
            # print(x)
            z = item[1]
            if str(x) == z[0]:
                #print(f'found seasoning {x}')
                #print(f'key: {item[0]}')
                seasoning[int(item[0]) - 1].set(1)
        # print(y)
        
    """for name, dict_ in dict_dict.items():
        print('the name of the dictionary is ', name)
        print('the dictionary looks like ', dict_)"""



    """else:  # transfer base template ingredients to your pizza
        index = p_base  # value from p_base
        your_base = base_pizza[index]
        your_p_name = your_base[0]
        your_pizza = your_base[1]
    print(your_p_name)
    print(your_pizza)"""

    # function to set button on/off values based on base pizza selection
    def set_buttons(options):
        print(your_pizza)
        for i in your_pizza:
            print(i)

    # radio button 'live refresh' function (as values change, refresh in realtime)
    def refresh_radio():
        return

    # check button 'live refresh' function (as values change, refresh in realtime)
    def refresh_check():
        return








    # pizza name label
    p_name_label = MyLabel(pizza_window, your_p_name, row=0, col=0,
                           font='Helvetica 18 bold')
    p_name_label.grid(sticky=W)


    # pizza's image frame
    pizza_img_frame = MyLabelFrame(pizza_window, 'Cheese Pizza', row=1, col=0)

    # set_buttons(your_pizza)

    # ingredient options
    ingredients_frame = MyFrame(pizza_window, row=2, col=0)
    # crust
    crust_frame = MyLabelFrame(ingredients_frame, "Crust", row=0, col=0, sticky=W+E)
    # crust = IntVar()
    hand_btn = MyRadio(crust_frame, 'Hand Tossed', row=0, col=0, sticky=W, var=crust, val=0)
    thin_btn = MyRadio(crust_frame, 'Thin & Crispy', row=1, col=0, sticky=W, var=crust, val=1)

    # sauce
    sauce_frame = MyLabelFrame(ingredients_frame, "Sauce", row=1, col=0, sticky=W+E)
    # sauce = IntVar()
    red_btn = MyRadio(sauce_frame, "Red Sauce", row=0, col=0, sticky=W, var=sauce, val=0)
    alfredo_btn = MyRadio(sauce_frame, "Alfredo Sauce", row=1, col=0, sticky=W, var=sauce, val=1)
    bbq_btn = MyRadio(sauce_frame, "BBQ Sauce", row=2, col=0, sticky=W, var=sauce, val=2)

    # cheese
    cheese_frame = MyLabelFrame(ingredients_frame, "Cheese", row=2, col=0, sticky=N+S+W+E)
    # cheese = IntVar()
    mozz_btn = MyCheck(cheese_frame, "Mozzarella", row=0, col=0, sticky=W, var=cheese)

    # meat
    meat_frame = MyLabelFrame(ingredients_frame, "Meats", row=0, col=1, rowspan=2, sticky=N+S+W+E)
    # meat = IntVar()
    pepp_btn = MyCheck(meat_frame, "Pepperoni", row=0, col=0, sticky=W, var=meat[0])
    ham_btn = MyCheck(meat_frame, "Ham", row=1, col=0, sticky=W, var=meat[1])
    chick_btn = MyCheck(meat_frame, "Chicken", row=2, col=0, sticky=W, var=meat[2])
    bac_btn = MyCheck(meat_frame, "Bacon", row=3, col=0, sticky=W, var=meat[3])
    saus_btn = MyCheck(meat_frame, "Sausage", row=4, col=0, sticky=W, var=meat[4])

    # topping
    topping_frame = MyLabelFrame(ingredients_frame, "Toppings", row=2, col=1, rowspan=2, sticky=N+S+W+E)
    # topping = IntVar()
    tom_btn = MyCheck(topping_frame, "Tomatoes", row=0, col=0, sticky=W, var=topping[0])
    spin_btn = MyCheck(topping_frame, "Spinach", row=1, col=0, sticky=W, var=topping[1])
    mush_btn = MyCheck(topping_frame, "Mushrooms", row=2, col=0, sticky=W, var=topping[2])
    gp_btn = MyCheck(topping_frame, "Green Peppers", row=3, col=0, sticky=W, var=topping[3])
    oni_btn = MyCheck(topping_frame, "Onions", row=4, col=0, sticky=W, var=topping[4])
    bo_btn = MyCheck(topping_frame, "Black Olives", row=5, col=0, sticky=W, var=topping[5])
    pine_btn = MyCheck(topping_frame, "Pineapples", row=6, col=0, sticky=W, var=topping[6])

    # seasoning
    seasoning_frame = MyLabelFrame(ingredients_frame, "Seasoning", row=3, col=0, sticky=N+S+W+E)
    # seasoning = IntVar()
    mg_btn = MyCheck(seasoning_frame, "Minced Garlic", row=0, col=0, sticky=W, var=seasoning[0])
    pc_btn = MyCheck(seasoning_frame, "Parmesan Cheese", row=1, col=0, sticky=W, var=seasoning[1])
    bbqd_btn = MyCheck(seasoning_frame, "BBQ Drizzle", row=2, col=0, sticky=W, var=seasoning[2])

    def refresh_za():
        return

    # make all this a funcy
    """images = []
    for img in your_pizza:
        images.append(img[1])"""

    """count = 0
    index = 0
    image0 = Image.open(str(images[index]))
    print(images[0])
    print(len(images))
    while count < len(images) - 3:
            image1 = image0
            index += 1
            image2 = Image.open(str(images[index]))
            index += 1
            inter = Image.alpha_composite(image1, image2)
            image3 = Image.open(str(images[index]))
            index += 1
            next = Image.alpha_composite(inter, image3)
            image0 = next
            count += 3
            p_final = ImageTk.PhotoImage(next)
    if count < len(images) - 2:
        image1 = Image.open(str(images[index]))
        index += 1
        image2 = Image.open(str(images[index]))
        index += 1
        inter = Image.alpha_composite(image1, image2)
        final = Image.alpha_composite(image0, inter)
        p_final = ImageTk.PhotoImage(final)
    elif count <= len(images) - 1:
        image2 = Image.open(str(images[index]))
        index += 1
        final = Image.alpha_composite(image0, image2)
        p_final = ImageTk.PhotoImage(final)
    else:
        p_final = ImageTk.PhotoImage(next)"""

    # not quite proper logic but correct bulding
    # SO FIX LOGIC, FORMATTING / READABILITY and checkbox interactions
    # img_label = MyLabel(ingredients_frame, '', row=0, col=2, img=p_final)

    """"# pizza image (from buttons)
    if crust == 0:
        crust_img = hand
    else:
        crust_img = thin
    if sauce == 0:
        sauce_img = red
    elif sauce == 1:
        sauce_img = alf
    else:
        sauce_img = bbq
    crust_img.paste(sauce_img, (0, 0), sauce_img)
    pizza_img0 = ImageTk.PhotoImage(crust_img)
    # pizza_img_label = MyLabel(ingredients_frame, '', img=pizza_img0, row=0, col=2, rowspan=4)
    #refresh_btn = MyButton(ingredients_frame, 'Refresh', row=6, col=0, colspan=4, command=refresh_za)
    if cheese == 1:
        cheese_img = mozz
    else:
        cheese_img = mozz
    if meat == 1:
        meat_img = pepp
    elif meat == 2:
        meat_img = ham
    elif meat == 3:
        meat_img = chick
    elif meat == 4:
        meat_img = bac
    else:
        meat_img = saus
    cheese_img.paste(meat_img, (0, 0), meat_img)
    pizza_img1 = ImageTk.PhotoImage(cheese_img)




    pizza_img_label = MyLabel(ingredients_frame, '', img=pizza_img0, row=0, col=2, rowspan=4)
    refresh_btn = MyButton(ingredients_frame, 'Refresh', row=6, col=0, colspan=4, command=refresh_za)

    # pizza image (from base template)
    '''index = 0
    for top in your_pizza:
        if index <= len(your_pizza) - 2:
            layer1 = your_pizza[index]
            print(layer1)
            layer2 = your_pizza[index + 1]
            print(layer2)
            iamge1 = layer1[1]
            print(image1)
            image2 = layer2[1]
            print(image2)
            iamge1.paste(image2, (0, 0), image2)
            pizza_image = ImageTk.PhotoImage(iamge1)
            index += 2
        else:
            print(index)'''

    '''your_crust = your_pizza[0]
    your_sauce = your_pizza[1]
    pizza_img0 = your_crust[1]
    pizza_img1 = your_sauce[1]
    pizza_img0.paste(pizza_img1, (0, 0), pizza_img1)
    pizza_img = ImageTk.PhotoImage(pizza_img0)
    your_cheese = your_pizza[2]
    your_meat = your_pizza[3]
    pizza_img2 = your_cheese[1]
    pizza_img3 = your_meat[1]
    pizza_img2.paste(pizza_img3, (0, 0), pizza_img3)
    pizza_img = ImageTk.PhotoImage(pizza_img2)
    pizza_img0.paste(pizza_img2, (0, 0), pizza_img2)
    pizza_img = ImageTk.PhotoImage(pizza_img0)'''

    #pizza_img_label = MyLabel(pizza_img_frame, '', img=pizza_image, row=0, col=0)
    #still neeed checkboxes
    '''tests = (thin, red, mozz, pepp, tom)
    for img in tests:
        datas = img.getdata()
        newData = []
        for item in datas:
            if item[0] == 255 and item[1] == 255 and item[2] == 255:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)

        img.putdata(newData)
        img.save("mod_img1.png", "PNG")

        background = Image.open('images/pizza/crust/thin.png')
        foreground = Image.open('images/pizza/cheese/mozz.png')

        background.paste(foreground, (0, 0), foreground)
        background.show()'''



    '''try:
        your_cheese = your_pizza[2]
        pizza_img2 = pizza_img
        pizza_img3 = your_cheese
        pizza_img2.paste(your_cheese, (0, 0), your_cheese)
        pizza_img'''

    '''for x in your_pizza:
        layer1 = pizza_img
        layer2 = x[1]
        print(x[1])'''

    '''layer1.paste(layer2, (0, 0), layer2)
        layer1pic = ImageTk.PhotoImage(layer1)
        label1 = MyLabel(pizza_window, '', img=layer1pic, row=1, col=1)'''


    #print(f'YOUR LIST {your_list}')
    #print(f'YOUR BASE 1 {your_base[1]}')
    #your_b_base = your_base[1]

    # for label, image in your_base[1]:

    # replace layers with tuples and makew your_crust etc equation to 'build' pizza in real time
    # alt text / labels and non-viusual representation
    # if p_base < 8

    # GO BACK THRU AND DOCUMENT ALL MODULES AND LINES CHECK FOR ERRORS AND TYPOS
    # extra or half options?"""



    # command for live pizza refreshing
    # documentation
    # final modules and final steps



    pizza_window.mainloop()

customize_pizza(1, 2, 0)