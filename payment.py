"""
Program: Peter’s Pizza Palace – Priority order-Placement Program v1.0.0 (.py)
Author: Cameron Coy (ccoy2@ivytech.edu)
Description: This is the payment module for the Peter's Pizza Palace - Priority order-Placement Program. It calculates
the cost of the user's pizza, and itemizes and returns the user's receipts.
"""
# import statements
import extras  # import 'extras' module (for the 'back' nav button)
import final  # import 'final' module (for the 'next' nav button)
from myGUI import *  # import 'myGUI' module to create instances of my tkinter widgets (custom syntax)


# define 'customize_pizza' function (to create new 'pizza_payment' window)
def pizza_payment(pickup, p_size, p_base, your_pizza, custom, changes, extra):
    """Creates and returns receipts based on your choices up to this point and passes the final values on to the
    'final' module for payment processing"""

    # create new toplevel tkinter window
    global payment_window  # make 'payment_window' object global
    payment_window = NewWindow("Review Your Order", '1000x560')  # create the 'review order' window

    # define a function to process input variables ('in' prefix for 'incoming')
    def process_input(in_pickup, in_p_size, in_p_base, in_your_pizza, in_custom, in_changes, in_extra):
        """Processes input variables into our desired types and strips away any leftover information from
        previous modules"""

        # function to print incoming variables (for testing) ('inp' prefix for 'incoming / print')
        def print_input_vars(inp_pickup, inp_p_size, inp_p_base, inp_your_pizza, inp_custom, inp_changes, inp_extra):
            """Prints incoming variables for test purposes (pre-processing)"""
            print(f'INCOMING PICKUP: {inp_pickup.get()}')  # print incoming 'pickup' value
            print(f'INCOMING SIZE: {inp_p_size.get()}')  # print incoming 'size' value
            print(f'INCOMING BASE: {inp_p_base}')  # print incoming 'base' value
            print(f'INCOMING PIZZA: {inp_your_pizza}')  # print incoming 'pizza' list
            print(f'INCOMING CUSTOM: {inp_custom}')  # print incoming 'custom' boolean
            print(f'INCOMING CHANGES: {inp_changes}')  # print incoming 'changes' dictionary
            print(f'INCOMING EXTRA: {inp_extra}')  # print incoming 'extra' list

        '''# print input variables (with function defined above) (for testing, uncomment to see values)
        print_input_vars(in_pickup, in_p_size, in_p_base, in_your_pizza, in_custom, in_changes, in_extra)'''

        # define functions to process incoming variables to outgoing values
        # process incoming tkinter variables
        def process_tkinter_var(in_variable):  # in_variable = incoming tkinter variable
            """Processes incoming tkinter variable's values into integers"""
            var_value = int(in_variable.get())  # 'gets' tkinter variable's value (stores it as an integer)
            return var_value  # return the tkinter variable's value (stored as an integer)

        # process incoming 'your_pizza' list (strip away extra information [image_path])
        def process_pizza_list(in_list):  # in_list = incoming your_pizza list
            """Process incoming 'your_pizza' list and strip away any extra information, like image_path"""
            out_list = []  # initialize outgoing 'your_pizza' list
            for pizza_ingredient in in_list:  # iterate through the incoming 'your_pizza' list ingredients
                out_list.append(pizza_ingredient[0])  # append the ingredient's name to the outgoing 'your_pizza' list
            return out_list  # return the processed 'your_pizza' list

        # process incoming 'changes' variable / dictionary (ensure it isn't NoneType)
        def process_changes_dict(in_object):  # in_object = incoming 'changes' object (either dictionary or NoneType)
            """Process incoming 'changes' object, ensuring it isn't 'NoneType'"""
            if in_object is None:  # checking if incoming 'changes' object is None
                out_dict = {'meats': 0, 'toppings': 0, 'seasonings': 0}  # process 'changes' dictionary (if None)
            else:  # if incoming 'changes' object is already a dictionary
                out_dict = in_object  # store incoming 'changes' dict in outgoing dict (no processing required)
            return out_dict  # return the processed 'changes' dictionary

        # process incoming variables individually (with functions defined above) / make processed variables global
        global pickup_value  # make processed 'pickup' variable's value global
        pickup_value = process_tkinter_var(in_pickup)  # process incoming 'pickup' variable and return its value
        global size_value  # make processed 'size' variable's value global
        size_value = process_tkinter_var(in_p_size)  # process incoming 'size' variable and return its value
        global base_value  # make processed 'base' variable's value global
        base_value = int(in_p_base)  # process incoming 'base' variable (store its value as an integer)
        global your_pizza_ingredients  # make processed 'your_pizza' list global
        your_pizza_ingredients = process_pizza_list(in_your_pizza)  # process incoming 'your_pizza' list
        global custom_value  # make processed 'custom' boolean global
        custom_value = bool(in_custom)  # process incoming 'custom' boolean
        global changes_dict  # make processed 'changes' dictionary global
        changes_dict = process_changes_dict(in_changes)  # process incoming 'changes' object
        global extra_list  # make processed 'extra' list global
        extra_list = list(in_extra)  # process incoming 'extra' list

        # function to print outgoing variables (for testing) ('op' prefix for 'outgoing / print')
        def print_output_vars(op_pickup, op_p_size, op_p_base, op_your_pizza, op_custom, op_changes, op_extra):
            """Prints outgoing variables for test purposes (post-processing)"""
            print(f'OUTGOING PICKUP: {op_pickup}')  # print outgoing 'pickup' variable
            print(f'OUTGOING SIZE: {op_p_size}')  # print outgoing 'size' variable
            print(f'OUTGOING BASE: {op_p_base}')  # print outgoing 'base' variable
            print(f'OUTGOING PIZZA: {op_your_pizza}')  # print outgoing 'pizza' list
            print(f'OUTGOING CUSTOM: {op_custom}')  # print outgoing 'custom' boolean
            print(f'OUTGOING CHANGES: {op_changes}')  # print outgoing 'changes' dictionary
            print(f'OUTGOING EXTRA: {op_extra}')  # print outgoing 'extra' list

        '''# print output variables (with function defined above) (for testing, uncomment to see values)
        print_output_vars(pickup_value, size_value, base_value, your_pizza_ingredients, custom_value, changes_dict,
                          extra_list)'''

    # process input variables (with functions defined above)
    process_input(pickup, p_size, p_base, your_pizza, custom, changes, extra)

    # create section's heading
    section_heading = MyLabel(payment_window, 'Total Price of Your Order:', row=0, col=0,
                              font=('Helvetica', 20, 'underline', 'bold'))  # section heading's label
    section_heading.grid(pady=(4, 0), padx=(2, 0))  # give section heading's label padding (4px top, 2px left)

    # define function to generate your_pizza_name from custom_value and base_value
    def get_your_pizza_name(edited, base):  # edited = custom_value, base = base_value
        """Generates your_pizza_name from custom_value and base_value"""
        # define 'base_names' list
        base_names = ['Cheese', 'Pepperoni', 'Sausage', 'Supreme', 'Meat-za™', 'Chicken Alfredo', 'Hawaiian',
                      'BBQ Chicken', 'From Scratch']
        # generate 'your_pizza_name'
        if edited is True:  # check if your_pizza is edited
            if base < 8:  # check if base_value is less than 8 (your_pizza is edited from base)
                pizza_name = f'{base_names[base]} Masterpie-zza™'  # 'pizza_name' is base_name + edited suffix
            else:  # if base_value is 8 (your_pizza is edited from scratch)
                pizza_name = 'Masterpie-zza™'  # edited suffix is 'pizza_name'
        else:  # if your_pizza is not edited
            if base < 8:  # check if base_value is less than 8 (your_pizza is a base)
                pizza_name = f'{base_names[base]} Pizza'  # 'pizza_name' is base_name + unedited suffix
            else:  # if base_value is 8 (your_pizza is from scratch)
                pizza_name = 'Masterpie-zza™'  # 'pizza_name' is edited suffix (from scratch)
        return pizza_name  # return your_pizza_name

    # define function to generate and display the itemized receipt for your_pizza
    def generate_pizza_receipt():
        """Generate and display the itemized receipt for your_pizza"""

        # get 'your_pizza_name' using function defined above (for the pizza_frame title)
        your_pizza_name = get_your_pizza_name(custom_value, base_value)  # get your_pizza_name

        # create 'pizza_frame' label frame to hold pizza itemization receipt
        global pizza_frame  # make pizza_frame global
        pizza_frame = MyLabelFrame(payment_window, f'Your {your_pizza_name}', row=1, col=0, font='Helvetica 16 bold')

        # define function to itemize your_pizza_ingredients
        def itemize_your_pizza(pizzas_ingredients):  # pizzas_ingredients = processed 'your_pizza' list
            """Itemize your_pizza_ingredients and return the itemized lists"""
            # define pizza ingredient categories
            meat_names = ['Pepperoni', 'Ham', 'Chicken', 'Bacon', 'Sausage']  # 'meat_names' list
            topping_names = ['Tomatoes', 'Spinach', 'Mushrooms', 'Bell Peppers', 'Onions', 'Black Olives',
                             'Pineapples']  # 'topping_names' list
            seasoning_names = ['Minced Garlic', 'Parmesan', 'BBQ Drizzle']  # 'seasoning_names' list
            # initialize local variables
            ingredient_index = 0  # initialize 'ingredient_index' variable for iteration
            out_crust = ''  # initialize 'crust' string for output
            out_sauce = ''  # initialize 'sauce' string for output
            out_cheese = ''  # initialize 'cheese' string for output
            out_meat = []  # initialize 'meat' list for output
            out_topping = []  # initialize 'topping' list for output
            out_seasoning = []  # initialize 'seasoning' list for output
            # fix for cheese issue with two item 'pizzas_ingredients' lists
            if len(pizzas_ingredients) < 3:  # if there are only two ingredients this will fix an issue with cheese
                pizzas_ingredients.append(None)  # set the third (cheese) 'pizza_ingredients' item to None
            # itemize 'pizzas_ingredients'
            for p_ingredient in pizzas_ingredients:  # iterate through 'pizzas_ingredients' for itemization
                if ingredient_index == 0:  # the first item (crust) in 'pizzas_ingredients'
                    out_crust = p_ingredient  # pull 'crust' out of 'pizzas_ingredients'
                if ingredient_index == 1:  # the second item (sauce) in 'pizzas_ingredients'
                    out_sauce = p_ingredient  # pull 'sauce' out of 'pizzas_ingredients'
                if ingredient_index == 2:  # the third item (cheese) in 'pizzas_ingredients'
                    if p_ingredient is None:  # check if there is cheese in 'pizzas_ingredients'
                        out_cheese = None  # set the third item (cheese) in 'pizzas_ingredients' to None
                    elif p_ingredient == 'Mozzarella':  # check if the third item in 'pizzas_ingredients' is cheese
                        out_cheese = p_ingredient  # pull 'cheese' out of 'pizzas_ingredients'
                    else:  # if the third item in 'pizza_ingredients' isn't cheese
                        out_cheese = None  # set 'cheese' to None
                        pizzas_ingredients.insert(2, None)  # insert a cheese placeholder into 'pizzas_ingredients'
                if ingredient_index > 2:  # check if we're past the first three items in 'pizzas_ingredients'
                    found_p_ingredient = False  # boolean variable for 'p_ingredient' search loop condition
                    while found_p_ingredient is False:  # loop through pizza ingredient categories to find p_ingredient
                        for meat_name in meat_names:  # iterate through meat_names
                            if p_ingredient == meat_name:  # is p_ingredient a meat item?
                                out_meat.append(p_ingredient)  # add p_ingredient to the 'meat' list
                                found_p_ingredient = True  # set found_p_ingredient to True
                        for topping_name in topping_names:  # iterate through topping_names
                            if p_ingredient == topping_name:  # is p_ingredient a topping item?
                                out_topping.append(p_ingredient)  # add p_ingredient to the 'topping' list
                                found_p_ingredient = True  # set found_p_ingredient to True
                        for seasoning_name in seasoning_names:  # iterate through seasoning_names
                            if p_ingredient == seasoning_name:  # is p_ingredient a seasoning item?
                                out_seasoning.append(p_ingredient)  # add p_ingredient to the 'seasoning' list
                                found_p_ingredient = True  # set found_p_ingredient to True
                ingredient_index += 1  # increment 'ingredient_index' variable
            item_lists = [out_crust, out_sauce, out_cheese, out_meat, out_topping, out_seasoning]
            return item_lists  # return itemized lists

        # itemize your_pizza_ingredients
        itemized_lists = itemize_your_pizza(your_pizza_ingredients)

        # create 'pizza_frame' pizza itemization sections
        # crust section (labels and textareas)
        crust_frame = MyFrame(pizza_frame, row=0, col=0)  # crust frame
        crust_label = MyLabel(crust_frame, 'Crust', row=0, col=0, font='Helvetica 12 bold', sticky=W)  # crust label
        crust_cost_label = MyLabel(crust_frame, 'Price', row=0, col=1, font='Helvetica 12', sticky=W)  # price label
        crust_text = MyText(crust_frame, height=1, width=25, row=1, col=0, state=DISABLED)  # crust text
        crust_cost_text = MyText(crust_frame, height=1, width=5, row=1, col=1, state=DISABLED)  # crust price text
        # sauce section (labels and textareas)
        sauce_frame = MyFrame(pizza_frame, row=1, col=0)  # sauce frame
        sauce_label = MyLabel(sauce_frame, 'Sauce', row=0, col=0, font='Helvetica 12 bold', sticky=W)  # sauce label
        sauce_cost_label = MyLabel(sauce_frame, 'Price', row=0, col=1, font='Helvetica 12', sticky=W)  # price label
        sauce_text = MyText(sauce_frame, height=1, width=25, row=1, col=0, state=DISABLED)  # sauce text
        sauce_cost_text = MyText(sauce_frame, height=1, width=5, row=1, col=1, state=DISABLED)  # price text
        # cheese section (labels and textareas)
        cheese_frame = MyFrame(pizza_frame, row=2, col=0)  # cheese frame
        cheese_label = MyLabel(cheese_frame, 'Cheese', row=0, col=0, font='Helvetica 12 bold', sticky=W)  # cheese label
        cheese_cost_label = MyLabel(cheese_frame, 'Price', row=0, col=1, font='Helvetica 12', sticky=W)  # price label
        cheese_text = MyText(cheese_frame, height=1, width=25, row=1, col=0, state=DISABLED)  # cheese text
        cheese_cost_text = MyText(cheese_frame, height=1, width=5, row=1, col=1, state=DISABLED)  # price text
        # meat section (labels and textareas)
        meat_frame = MyFrame(pizza_frame, row=3, col=0)  # meat frame
        meat_label = MyLabel(meat_frame, 'Meats', row=0, col=0, font='Helvetica 12 bold', sticky=W)  # meat label
        meat_cost_label = MyLabel(meat_frame, 'Price', row=0, col=1, font='Helvetica 12', sticky=W)  # price label
        meat_text = MyText(meat_frame, height=len(itemized_lists[3]), width=25, row=1, col=0, state=DISABLED)
        meat_cost_text = MyText(meat_frame, height=len(itemized_lists[3]), width=5, row=1, col=1, state=DISABLED)
        # topping section (labels and textareas)
        topping_frame = MyFrame(pizza_frame, row=4, col=0)  # topping frame
        topping_label = MyLabel(topping_frame, 'Toppings', row=0, col=0, font='Helvetica 12 bold', sticky=W)  # toplabel
        topping_cost_label = MyLabel(topping_frame, 'Price', row=0, col=1, font='Helvetica 12', sticky=W)  # price label
        topping_text = MyText(topping_frame, height=len(itemized_lists[4]), width=25, row=1, col=0, state=DISABLED)
        topping_cost_text = MyText(topping_frame, height=len(itemized_lists[4]), width=5, row=1, col=1, state=DISABLED)
        # seasoning section (labels and textareas)
        seasoning_frame = MyFrame(pizza_frame, row=5, col=0)  # seasoning frame
        seasoning_label = MyLabel(seasoning_frame, 'Seasonings', row=0, col=0, font='Helvetica 12 bold', sticky=W)
        seasoning_cost_label = MyLabel(seasoning_frame, 'Price', row=0, col=1, font='Helvetica 12', sticky=W)
        seasoning_text = MyText(seasoning_frame, height=len(itemized_lists[5]), width=25, row=1, col=0, state=DISABLED)
        seasoning_cost_text = MyText(seasoning_frame, height=len(itemized_lists[5]), width=5, row=1, col=1,
                                     state=DISABLED)
        price_star = MyLabel(pizza_frame, "* Included in the Pizza's base cost", row=6, col=0, colspan=2, sticky=W,
                             font='Helvetica 10 italic')  # '*' explanation label

        # define function to populate 'pizza_frame' section's Textareas
        def populate_pizza_frame_text(pizza_item_lists):  # pizza_item_lists = itemized 'your_pizza' lists
            """Populates 'pizza_frame' section's Textareas with ingredients and prices"""
            # populate crust section
            crust_string = pizza_item_lists[0]  # pull 'crust_string' out of 'item_lists'
            # crust text
            crust_text['state'] = NORMAL  # set 'crust_text' state to normal
            crust_text.insert(0.0, crust_string)  # insert crust text
            crust_text['state'] = DISABLED  # set 'crust_text' state to disabled
            # crust cost text
            crust_cost_text['state'] = NORMAL  # set 'crust_cost_text' state to normal
            crust_cost_text.insert(0.0, '*')  # insert crust cost text (included in base price)
            crust_cost_text['state'] = DISABLED  # set 'crust_cost_text' state to disabled

            # populate sauce section
            sauce_string = pizza_item_lists[1]  # pull 'sauce_string' out of 'item_lists'
            # sauce text
            sauce_text['state'] = NORMAL  # set 'sauce_text' state to normal
            sauce_text.insert(0.0, sauce_string)  # insert sauces text
            sauce_text['state'] = DISABLED  # set 'sauce_text' state to disabled
            # sauce cost text
            sauce_cost_text['state'] = NORMAL  # set 'sauce_cost_text' state to normal
            sauce_cost_text.insert(0.0, '*')  # insert sauce cost text (included in base price)
            sauce_cost_text['state'] = DISABLED  # set 'sauce_cost_text' state to disabled

            # populate cheese section
            cheese_string = pizza_item_lists[2]  # pull 'cheese_string' out of 'item_lists'
            if cheese_string is not None:  # with cheese on the pizza
                # cheese text
                cheese_text['state'] = NORMAL  # set 'cheese_text' state to normal
                cheese_text.insert(0.0, cheese_string)  # insert cheese text
                cheese_text['state'] = DISABLED  # set 'cheese_text' state to disabled
                # cheese cost text
                cheese_cost_text['state'] = NORMAL  # set 'cheese_cost_text' state to normal
                cheese_cost_text.insert(0.0, '*')  # insert cheese cost text (included in base price)
                cheese_cost_text['state'] = DISABLED  # set 'cheese_cost_text' state to disabled
            else:  # without cheese on the pizza
                # cheese text
                cheese_text['state'] = NORMAL  # set 'cheese_text' state to normal
                cheese_text.insert(0.0, 'No Cheese')  # insert no cheese text
                cheese_text['state'] = DISABLED  # set 'cheese_text' state to disabled
                # cheese cost text
                cheese_cost_text['state'] = NORMAL  # set 'cheese_cost_text' state to normal
                cheese_cost_text.insert(0.0, '-')  # insert cheese cost text (no charge)
                cheese_cost_text['state'] = DISABLED  # set 'cheese_cost_text' state to disabled

            # define function to check pizza_base for an ingredient
            def check_pizza_base(base_key, list_ingredient):  # base_key = base_value, list_ingredient = item to check
                """Checks the pizza_base for presence of an ingredient"""
                # define base_ingredients dictionary (corresponds to base_value, doesn't include crust, sauce or cheese)
                base_ingredients = {0: 'Parmesan',
                                    1: 'Pepperoni',
                                    2: 'Sausage',
                                    3: ('Pepperoni', 'Sausage', 'Mushrooms', 'Bell Peppers', 'Onions', 'Black Olives'),
                                    4: ('Minced Garlic', 'Pepperoni', 'Ham', 'Bacon', 'Sausage', 'Parmesan'),
                                    5: ('Minced Garlic', 'Spinach', 'Tomatoes', 'Chicken', 'Parmesan'),
                                    6: ('Ham', 'Pineapples'),
                                    7: ('Onions', 'Bacon', 'Chicken', 'BBQ Drizzle')}
                # determine which base_ingredients list to check against
                if base_key < 8:  # base pizza is from a base pizza template
                    base_list = base_ingredients[base_key]  # pull 'base_list' out of the 'base_ingredients' dictionary
                else:  # base pizza is from scratch (no base)
                    base_list = []  # initialize 'base_list' as an empty list (no base)
                found_b_ingredient = False  # boolean variable for 'list_ingredient' to search base_ingredients
                if type(base_list) is str:  # only one item in the base (hotfix for iteration issue)
                    if list_ingredient == base_list:  # checked ingredient is the 'base_list' ingredient
                        found_b_ingredient = True  # checked ingredient is in 'base_list'
                    else:  # checked ingredient is not the 'base_list' ingredient
                        return found_b_ingredient  # return that checked item doesn't match the 'base_list' ingredient
                else:
                    for base_item in base_list:  # iterate through ingredients in base_list
                        if list_ingredient == base_item:  # check 'base_list' ingredients against 'list_ingredient'
                            found_b_ingredient = True  # checked ingredient is in 'base_list'
                return found_b_ingredient  # returns whether the ingredient was found in 'base_list' or not

            # populate meat section
            meat_list = pizza_item_lists[3]  # pull 'meat_list' out of 'item_lists'
            if not meat_list:  # no added meats
                # meat text
                meat_text['state'] = NORMAL  # set 'meat_text' state to normal
                meat_text.insert(0.0, 'No Meats')  # insert no meat text
                meat_text['state'] = DISABLED  # set 'meat_text' state to disabled
                # meat cost text
                meat_cost_text['state'] = NORMAL  # set 'meat_cost_text' state to normal
                meat_cost_text.insert(0.0, '-')  # insert meat cost text (no charge)
                meat_cost_text['state'] = DISABLED  # set 'meat_cost_text' state to disabled
            else:  # added meats
                meat_text['state'] = NORMAL  # set 'meat_text' state to normal
                meat_cost_text['state'] = NORMAL  # set 'meat_cost_text' state to normal
                meat_line = 0.0  # line variable for inserting meat_items into textareas
                for meat_item in meat_list:  # iterate through 'meat_list'
                    meat_text.insert(meat_line, f'{meat_item}\n')  # insert meat text
                    found_meat_item = check_pizza_base(base_value, meat_item)  # check if 'meat_item' is in 'base_pizza'
                    if found_meat_item is True:  # if meat_item is in 'base_pizza'
                        meat_cost_text.insert(meat_line, '*\n')  # insert meat cost text (included in base)
                    else:  # if meat_item is not in 'base_pizza'
                        meat_cost_text.insert(meat_line, '$0.75\n')  # insert meat cost text ($0.75)
                    meat_line += 1.0  # move the line variable to the next line
                meat_text['state'] = DISABLED  # set 'meat_text' state to disabled
                meat_cost_text['state'] = DISABLED  # set 'meat_cost_text' state to disabled

            # populate topping section
            topping_list = pizza_item_lists[4]  # pull 'topping_list' out of 'item_lists'
            if not topping_list:  # no added toppings
                # topping text
                topping_text['state'] = NORMAL  # set 'topping_text' state to normal
                topping_text.insert(0.0, 'No Toppings')  # insert no topping text
                topping_text['state'] = DISABLED  # set 'topping_text' state to disabled
                # topping cost text
                topping_cost_text['state'] = NORMAL  # set 'topping_cost_text' state to normal
                topping_cost_text.insert(0.0, '-')  # insert topping cost text (no charge)
                topping_cost_text['state'] = DISABLED  # set 'topping_cost_text' state to disabled
            else:  # added toppings
                topping_text['state'] = NORMAL  # set 'topping_text' state to normal
                topping_cost_text['state'] = NORMAL  # set 'topping_cost_text' state to normal
                topping_line = 0.0  # line variable for inserting topping_items into textareas
                for topping_item in topping_list:  # iterate through 'topping_list'
                    topping_text.insert(topping_line, f'{topping_item}\n')  # insert topping text
                    found_topping_item = check_pizza_base(base_value, topping_item)  # check if 'topping' is in 'base'
                    if found_topping_item is True:  # if topping_item is in 'base_pizza'
                        topping_cost_text.insert(topping_line, '*\n')  # insert topping cost text (included in base)
                    else:  # if topping_item is not in 'base_pizza'
                        topping_cost_text.insert(topping_line, '$0.45\n')  # insert topping cost text ($0.45)
                    topping_line += 1.0  # move the line variable to the next line
                topping_text['state'] = DISABLED  # set 'topping_text' state to disabled
                topping_cost_text['state'] = DISABLED  # set 'topping_cost_text' state to disabled

            # populate seasoning section
            seasoning_list = pizza_item_lists[5]  # pull 'seasoning_list' out of 'item_lists'
            if not seasoning_list:  # no added seasonings
                # seasoning text
                seasoning_text['state'] = NORMAL  # set 'seasoning_text' state to normal
                seasoning_text.insert(0.0, 'No Seasonings')  # insert no seasonings text
                seasoning_text['state'] = DISABLED  # set 'seasoning_text' state to disabled
                # seasoning cost text
                seasoning_cost_text['state'] = NORMAL  # set 'seasoning_cost_text' state to normal
                seasoning_cost_text.insert(0.0, '-')  # insert seasoning cost text (no charge)
                seasoning_cost_text['state'] = DISABLED  # set 'seasoning_cost_text' state to disabled
            else:  # added seasonings
                seasoning_text['state'] = NORMAL  # set 'seasoning_text' state to normal
                seasoning_cost_text['state'] = NORMAL  # set 'seasoning_cost_text' state to normal
                seasoning_line = 0.0  # line variable for inserting seasonings_items into textareas
                for seasoning_item in seasoning_list:  # iterate through 'seasoning_list'
                    seasoning_text.insert(seasoning_line, f'{seasoning_item}\n')  # insert seasoning text
                    found_seasoning_item = check_pizza_base(base_value, seasoning_item)  # check if 'seas' is in 'base'
                    if found_seasoning_item is True:  # if seasoning_item is in 'base_pizza'
                        seasoning_cost_text.insert(seasoning_line, '*\n')  # insert season cost text (included in base)
                    else:  # if seasoning_item is not in 'base_pizza'
                        seasoning_cost_text.insert(seasoning_line, '$0.15\n')  # insert seasoning cost text ($0.15)
                    seasoning_line += 1.0  # move the line variable to the next line
                seasoning_text['state'] = DISABLED  # set 'seasoning_text' state to disabled
                seasoning_cost_text['state'] = DISABLED  # set 'seasoning_cost_text' state to disabled

        # populate 'pizza_frame' textareas (with functions defined above)
        populate_pizza_frame_text(itemized_lists)

    # generate pizza receipt
    generate_pizza_receipt()

    # define function to generate and display the itemized receipt for your_pizza's price
    def generate_pizza_cost_receipt():
        """Generate and display the itemized receipt for your_pizza's price"""

        # create 'pizza_total_frame' label frame to hold pizza's itemized price receipt
        global pizza_total_frame  # make pizza_total_frame global
        pizza_total_frame = MyLabelFrame(payment_window, 'Pizza Price Breakdown', row=1, col=1, sticky=N,
                                         font='Helvetica 16 bold',)  # create 'pizza_total_frame'

        # create 'pizza_total_frame' pizza's price itemization sections
        # pizza base price (labels and textareas)
        pizza_base_label = MyLabel(pizza_total_frame, 'Pizza Base', row=0, col=0, font='Helvetica 12 bold', sticky=W)
        pizza_base_cost_label = MyLabel(pizza_total_frame, 'Price', row=0, col=1, font='Helvetica 12', sticky=W)
        pizza_base_text = MyText(pizza_total_frame, height=1, width=25, row=1, col=0, state=DISABLED)
        pizza_base_cost_text = MyText(pizza_total_frame, height=1, width=6, row=1, col=1, state=DISABLED)
        # pizza size price (labels and textareas)
        pizza_size_label = MyLabel(pizza_total_frame, 'Pizza Size', row=2, col=0, font='Helvetica 12 bold', sticky=W)
        pizza_size_cost_label = MyLabel(pizza_total_frame, '(x)', row=2, col=1, font='Helvetica 10 bold')
        pizza_size_text = MyText(pizza_total_frame, height=1, width=25, row=3, col=0, state=DISABLED)
        pizza_size_cost_text = MyText(pizza_total_frame, height=1, width=6, row=3, col=1, state=DISABLED)
        # delivery fee (labels and textareas)
        delivery_fee_label = MyLabel(pizza_total_frame, 'Fee', row=4, col=0, font='Helvetica 12 bold', sticky=W)
        delivery_fee_cost_label = MyLabel(pizza_total_frame, '(+)', row=4, col=1, font='Helvetica 10 bold')
        delivery_fee_text = MyText(pizza_total_frame, height=1, width=25, row=5, col=0, state=DISABLED)
        delivery_fee_cost_text = MyText(pizza_total_frame, height=1, width=6, row=5, col=1, state=DISABLED)
        # added ingredients price (labels and textareas)
        added_ingredients_label = MyLabel(pizza_total_frame, 'Added Ingredients', row=6, col=0,
                                          font='Helvetica 12 bold', sticky=W)
        added_ingredients_cost_label = MyLabel(pizza_total_frame, '(+)', row=6, col=1, font='Helvetica 10 bold')
        meat_total_text = MyText(pizza_total_frame, height=1, width=25, row=7, col=0, state=DISABLED)
        meat_total_cost_text = MyText(pizza_total_frame, height=1, width=6, row=7, col=1, state=DISABLED)
        topping_total_text = MyText(pizza_total_frame, height=1, width=25, row=8, col=0, state=DISABLED)
        topping_total_cost_text = MyText(pizza_total_frame, height=1, width=6, row=8, col=1, state=DISABLED)
        seasoning_total_text = MyText(pizza_total_frame, height=1, width=25, row=9, col=0, state=DISABLED)
        seasoning_total_cost_text = MyText(pizza_total_frame, height=1, width=6, row=9, col=1, state=DISABLED)
        # pizza total price (labels and textareas)
        pizza_total_label = MyLabel(pizza_total_frame, 'Total Pizza Price', row=10, col=0, font='Helvetica 12 bold',
                                    sticky=W)
        pizza_total_label.grid(pady=(10, 0))
        pizza_total_cost_label = MyLabel(pizza_total_frame, 'Price', row=10, col=1, font='Helvetica 12', sticky=W)
        pizza_total_cost_label.grid(pady=(10, 0))
        pizza_total_text = MyText(pizza_total_frame, height=1, width=25, row=11, col=0, state=DISABLED)
        pizza_total_cost_text = MyText(pizza_total_frame, height=1, width=6, row=11, col=1, state=DISABLED)

        # define function to populate 'pizza_total_frame' textareas
        def populate_pizza_total_frame_text():
            """Populates 'pizza_total_frame' section's Textareas with items and prices"""

            # create lists and dictionaries for pizza pricing and labeling
            # 'base_pizza' objects
            base_prices = {0: 10.50, 1: 11.00, 2: 11.00, 3: 13.00, 4: 13.50, 5: 12.00, 6: 11.50, 7: 12.00,
                           8: 10.00}  # 'base prices' dictionary
            # 'pickup' objects
            pickup_prices = {0: 4.95, 1: 0.00}  # 'pickup prices' dictionary
            pickup_names = ['Delivery', 'Carry-Out']  # 'pickup names' list
            # 'size' objects
            size_prices = {0: 1.00, 1: 1.20, 2: 1.40, 3: 1.60}  # 'size prices' dictionary
            size_names = ['Small (10") - 6 Slices', 'Medium (14") - 8 Slices', 'Large (16") - 10 Slices',
                          'XL (19") - 12 Slices']  # 'size names' list

            # define function to calculate the price of the pizza
            def calculate_pizza_price():
                """Calculates the price of the pizza"""
                # calculate the pizza's base price (price before additional ingredients)
                pizza_base_price = base_prices[base_value] * size_prices[size_value] + pickup_prices[pickup_value]
                # calculate the prices of additional ingredients
                meat_price = changes_dict['meats'] * 0.75  # price of additional meats
                topping_price = changes_dict['toppings'] * 0.45  # price of additional toppings
                seasoning_price = changes_dict['seasonings'] * 0.15  # price of additional seasonings
                added_cost = meat_price + topping_price + seasoning_price  # price of all additional ingredients
                # calculate the price of the pizza
                final_price = round((pizza_base_price + added_cost), 2)  # calculate and round 'final_price'
                return final_price  # return the 'final_price'

            # generate pizza name for heading
            pizza_total_name = get_your_pizza_name(False, base_value)

            # populate pizza total cost breakdown textareas
            # populate 'base' section
            # base text
            pizza_base_text['state'] = NORMAL  # set 'pizza_base_text' state to normal
            pizza_base_text.insert(0.0, pizza_total_name)  # insert pizza base text
            pizza_base_text['state'] = DISABLED  # set 'pizza_base_text' state to disabled
            # base cost text
            pizza_base_cost_text['state'] = NORMAL  # set 'pizza_base_cost_text' state to normal
            pizza_base_cost_text.insert(0.0, '$%0.2f' % base_prices[base_value])  # insert pizza base cost text
            pizza_base_cost_text['state'] = DISABLED  # set 'pizza_base_cost_text' state to disabled
            # times (x)
            # populate 'size' section
            # size text
            pizza_size_text['state'] = NORMAL  # set 'pizza_size_text' state to normal
            pizza_size_text.insert(0.0, f"{size_names[size_value]}")  # insert pizza size text
            pizza_size_text['state'] = DISABLED  # set 'pizza_size_text' state to disabled
            # size cost text
            pizza_size_cost_text['state'] = NORMAL  # set 'pizza_size_cost_text' state to normal
            pizza_size_cost_text.insert(0.0, '%0.2f' % size_prices[size_value])  # insert pizza size cost text
            pizza_size_cost_text['state'] = DISABLED  # set 'pizza_size_cost_text' state to disabled
            # plus (+)
            # populate 'delivery fee' section
            # delivery fee text
            delivery_fee_text['state'] = NORMAL  # set 'delivery_fee_text' state to normal
            delivery_fee_text.insert(0.0, f"{pickup_names[pickup_value]}")  # insert delivery fee text
            delivery_fee_text['state'] = DISABLED  # set 'delivery_fee_text' state to disabled
            # delivery fee cost text
            delivery_fee_cost_text['state'] = NORMAL  # set 'delivery_fee_cost_text' state to normal
            delivery_fee_cost_text.insert(0.0, '$%0.2f' % pickup_prices[pickup_value])  # insert delivery fee cost text
            delivery_fee_cost_text['state'] = DISABLED  # set 'delivery_fee_cost_text' state to disabled
            # plus(+)
            # populate 'added ingredients' section
            # 'added meats' section
            changes_meats = changes_dict['meats']  # pull the number of added meats from 'changes_dict'
            if changes_meats == 0:  # no added meats
                # meat text
                meat_total_text['state'] = NORMAL  # set 'meat_total_text' state to normal
                meat_total_text.insert(0.0, 'No Added Meats')  # insert no meat text
                meat_total_text['state'] = DISABLED  # set 'meat_total_text' state to disabled
                # meat cost text
                meat_total_cost_text['state'] = NORMAL  # set 'meat_total_cost_text' state to normal
                meat_total_cost_text.insert(0.0, '$0.00')  # insert meat cost text (No Charge)
                meat_total_cost_text['state'] = DISABLED  # set 'meat_total_cost_text' state to disabled
            else:  # additional meats added
                # meat text
                meat_total_text['state'] = NORMAL  # set 'meat_total_text' state to normal
                meat_total = changes_meats  # get total number of added meats
                meat_total_text.insert(0.0, f'{meat_total} Added Meats')  # insert meat text (with total number)
                meat_total_text['state'] = DISABLED  # set 'meat_total_text' state to disabled
                # meat cost text
                meat_total_cost_text['state'] = NORMAL  # set 'meat_total_cost_text' state to normal
                meat_total_cost = meat_total * 0.75  # calculate cost of added meats
                meat_total_cost_text.insert(0.0, '$%0.2f' % meat_total_cost)  # insert meat cost text
                meat_total_cost_text['state'] = DISABLED  # set 'meat_total_cost_text' state to disabled
            # 'added toppings' section
            changes_toppings = changes_dict['toppings']  # pull the number of added toppings from 'changes_dict'
            if changes_toppings == 0:  # no added toppings
                # topping text
                topping_total_text['state'] = NORMAL  # set 'topping_total_text' state to normal
                topping_total_text.insert(0.0, 'No Added Toppings')  # insert no topping text
                topping_total_text['state'] = DISABLED  # set 'topping_total_text' state to disabled
                # topping cost text
                topping_total_cost_text['state'] = NORMAL  # set 'topping_total_cost_text' state to normal
                topping_total_cost_text.insert(0.0, '$0.00')  # insert topping cost text (No Charge)
                topping_total_cost_text['state'] = DISABLED  # set 'topping_total_cost_text' state to disabled
            else:  # additional toppings added
                # topping text
                topping_total_text['state'] = NORMAL  # set 'topping_total_text' state to normal
                topping_total = changes_toppings  # get total number of added toppings
                topping_total_text.insert(0.0, f'{topping_total} Added Toppings')  # insert top text (w/ total number)
                topping_total_text['state'] = DISABLED  # set 'topping_total_text' state to disabled
                # topping cost text
                topping_total_cost_text['state'] = NORMAL  # set 'topping_total_cost_text' state to normal
                topping_total_cost = topping_total * 0.45  # calculate cost of added toppings
                topping_total_cost_text.insert(0.0, '$%0.2f' % topping_total_cost)  # insert topping cost text
                topping_total_cost_text['state'] = DISABLED  # set 'topping_total_cost_text' state to disabled
            # 'added seasonings' section
            changes_seasonings = changes_dict['seasonings']  # pull the number of added seasonings from 'changes_dict'
            if changes_seasonings == 0:  # no added seasonings
                # seasoning text
                seasoning_total_text['state'] = NORMAL  # set 'seasoning_total_text' state to normal
                seasoning_total_text.insert(0.0, 'No Added Seasonings')  # insert no seasoning text
                seasoning_total_text['state'] = DISABLED  # set 'seasoning_total_text' state to disabled
                # seasoning cost text
                seasoning_total_cost_text['state'] = NORMAL  # set 'seasoning_total_cost_text' state to normal
                seasoning_total_cost_text.insert(0.0, '$0.00')  # insert seasoning cost text (No Charge)
                seasoning_total_cost_text['state'] = DISABLED  # set 'seasoning_total_cost_text' state to disabled
            else:  # additional seasonings added
                # seasoning text
                seasoning_total_text['state'] = NORMAL  # set 'seasoning_total_text' state to normal
                seasoning_total = changes_seasonings  # get total number of added seasonings
                seasoning_total_text.insert(0.0, f'{seasoning_total} Added Seasonings')  # insert season text (w/ total)
                seasoning_total_text['state'] = DISABLED  # set 'seasoning_total_text' state to disabled
                # seasoning cost text
                seasoning_total_cost_text['state'] = NORMAL  # set 'seasoning_total_cost_text' state to normal
                seasoning_total_cost = seasoning_total * 0.15  # calculate cost of added seasonings
                seasoning_total_cost_text.insert(0.0, '$%0.2f' % seasoning_total_cost)  # insert seasoning cost text
                seasoning_total_cost_text['state'] = DISABLED  # set 'seasoning_total_cost_text' state to disabled
            # populate 'total pizza price' section
            # pizza total text
            pizza_total_text['state'] = NORMAL  # set 'pizza_total_text' state to normal
            if custom_value is True:  # pizza has been changed from base
                pizza_total_text.insert(0.0, 'Your Masterpie-zza™')  # insert pizza total text
                pizza_total_text['state'] = DISABLED  # set 'pizza_total_text' state to disabled
            else:  # pizza hasn't been changed from base
                pizza_total_text.insert(0.0, 'Your Pizza')  # insert pizza total text
                pizza_total_text['state'] = DISABLED  # set 'pizza_total_text' state to disabled
            # pizza total cost text
            pizza_total_cost_text['state'] = NORMAL  # set 'pizza_total_cost_text' state to normal
            global pizza_price  # make 'pizza_price' global
            pizza_price = calculate_pizza_price()  # calculate 'pizza_price' with function defined above
            pizza_total_cost_text.insert(0.0, '$%0.2f' % pizza_price)  # insert pizza total cost text
            pizza_total_cost_text['state'] = DISABLED  # set 'pizza_total_cost_text' state to disabled

        # populate 'pizza_total_frame' textareas (with functions defined above)
        populate_pizza_total_frame_text()

    # generate pizza cost receipt
    generate_pizza_cost_receipt()

    # define function to generate and display the itemized receipt for your extra items total
    def generate_extra_total_receipt():
        """Generate and display the itemized receipt for your extra items total (sides, desserts, etc.)"""

        # create 'extra_total_frame' label frame to hold your extras itemized receipt
        global extra_total_frame  # make extra_total_frame global
        extra_total_frame = MyLabelFrame(payment_window, 'Extra Items', row=1, col=3, font='Helvetica 16 bold',
                                         sticky=N)  # create 'extra_total_frame'
        extra_total_frame.grid(padx=(12, 0))  # add some padding to 'extra_total_frame' (12px left)

        # define function to determine information about your extra item selections
        def extra_item_info():
            """Determines information about your extra item selections"""
            # create lists for extra_item categories
            side_names = ['Breadsticks', 'Garlic Bread']  # 'side item' names
            dipping_names = ['Cheese', 'Garlic Butter', 'Marinara', 'Ranch']  # 'dipping sauce' names
            dessert_names = ['Cinnastix™', 'Brownies', 'Cookies', 'Choc Cookies']  # 'dessert item' names
            drink_names = ['Coke', 'Diet Coke', 'Sprite', 'Dr Pepper', 'Mtn Dew', 'Orange Soda',
                           'Grape Soda']  # 'drink' names
            # initialize extra_item category lists
            your_sides = []  # 'your_sides' list
            your_sauces = []  # 'your_sauces' list
            your_desserts = []  # 'your_desserts' list
            your_drinks = []  # 'your_drinks' list
            # determine information about extra item selections
            for extra_item in extra_list:  # iterate through 'extra_list' from previous module
                extra_item_found = False  # boolean variable for 'extra_item' to search extra_list
                while extra_item_found is not True:  # loop through the lists until 'extra_item' is 'found'
                    for side_name in side_names:  # check if extra_item is a side_item
                        if extra_item == side_name:  # 'extra_item' is a side_item
                            your_sides.append(extra_item)  # add 'extra_item' to your_sides
                            extra_item_found = True  # set 'extra_item_found' to True (end the loop for that item)
                    for dipping_name in dipping_names:  # check if extra_item is a dipping_sauce
                        if extra_item == dipping_name:  # 'extra_item' is a dipping_sauce
                            your_sauces.append(extra_item)  # add 'extra_item' to your_sauces
                            extra_item_found = True  # set 'extra_item_found' to True (end the loop for that item)
                    for dessert_name in dessert_names:  # check if extra_item is a dessert_item
                        if extra_item == dessert_name:  # 'extra_item' is a dessert_item
                            your_desserts.append(extra_item)  # add 'extra_item' to your_desserts
                            extra_item_found = True  # set 'extra_item_found' to True (end the loop for that item)
                    for drink_name in drink_names:  # check if extra_item is a drink_item
                        if extra_item == drink_name:  # 'extra_item' is a drink_item
                            your_drinks.append(extra_item)  # add 'extra_item' to your_drinks
                            extra_item_found = True  # set 'extra_item_found' to True (end the loop for that item)
            extra_item_lists = [your_sides, your_sauces, your_desserts, your_drinks]  # combine extra_lists into object
            return extra_item_lists  # return list of extra_item lists

        # determine info about extra_item selections
        global your_extras  # make 'your_extras' list global
        your_extras = extra_item_info()  # create 'your_extras' list (from the function above)

        # define function to determine height of extra_item textareas
        def determine_text_height(extra_selection_lists):
            """Determines the height of extra_total_frame's extra_item textareas (based on extra_item selections)"""
            # determine height for extra_total_frame's extra_item textareas
            # 'side' section's textarea height
            sides_list = extra_selection_lists[0]  # pull 'sides_list' from 'extra_selection_lists' list
            if len(sides_list) == 0:  # no side_items selected
                sides_height = 1  # set sides_height to 1
            else:  # side_items selected
                sides_height = len(sides_list)  # set sides_height to the amount of side_items selected
            # 'dipping sauce' section's textarea height
            sauces_list = extra_selection_lists[1]  # pull 'sauces_list' from 'extra_selection_lists' list
            if len(sauces_list) == 0:  # no dipping_sauces selected
                sauces_height = 1  # set sauces_height to 1
            else:  # dipping_sauces selected
                sauces_height = len(sauces_list)  # set sauces_height to the amount of dipping_sauces selected
            # 'dessert item' section's textarea height
            desserts_list = extra_selection_lists[2]  # pull 'desserts_list' from 'extra_selection_lists' list
            if len(desserts_list) == 0:  # no dessert_items selected
                desserts_height = 1  # set dessert_height to 1
            else:  # dessert_items selected
                desserts_height = len(desserts_list)  # set desserts_height to the amount of dessert_items selected
            # 'drinks' section's textarea height
            drinks_list = extra_selection_lists[3]  # pull 'drinks_list' from 'extra_selection_lists' list
            if len(drinks_list) == 0:  # no drinks selected
                drinks_height = 1  # set drinks_height to 1
            else:  # drinks selected
                drinks_height = len(drinks_list)  # set drinks_height to the number of drinks selected
            textarea_heights = [sides_height, sauces_height, desserts_height, drinks_height]  # add heights into list
            return textarea_heights  # return list of textarea heights

        # determine heights of extra_item textareas
        text_heights = determine_text_height(your_extras)

        # create 'extra_total_frame' extra_item's price itemization sections
        # side_item prices (labels and textareas)
        side_label = MyLabel(extra_total_frame, 'Side Items', row=0, col=0, font='Helvetica 12 bold', sticky=W)
        side_cost_label = MyLabel(extra_total_frame, 'Price', row=0, col=1, font='Helvetica 12', sticky=W)
        side_text = MyText(extra_total_frame, height=text_heights[0], width=25, row=1, col=0, state=DISABLED)
        side_cost_text = MyText(extra_total_frame, height=text_heights[0], width=5, row=1, col=1, state=DISABLED)
        # dipping_sauce prices (labels and textareas)
        dipping_label = MyLabel(extra_total_frame, 'Dipping Sauces', row=2, col=0, font='Helvetica 12 bold', sticky=W)
        dipping_cost_label = MyLabel(extra_total_frame, 'Price', row=2, col=1, font='Helvetica 12', sticky=W)
        dipping_text = MyText(extra_total_frame, height=text_heights[1], width=25, row=3, col=0, state=DISABLED)
        dipping_cost_text = MyText(extra_total_frame, height=text_heights[1], width=5, row=3, col=1, state=DISABLED)
        # dessert_item prices (labels and textareas)
        dessert_label = MyLabel(extra_total_frame, 'Dessert Items', row=4, col=0, font='Helvetica 12 bold', sticky=W)
        dessert_cost_label = MyLabel(extra_total_frame, 'Price', row=4, col=1, font='Helvetica 12', sticky=W)
        dessert_text = MyText(extra_total_frame, height=text_heights[2], width=25, row=5, col=0, state=DISABLED)
        dessert_cost_text = MyText(extra_total_frame, height=text_heights[2], width=5, row=5, col=1, state=DISABLED)
        # drink_item prices (labels and textareas)
        drink_label = MyLabel(extra_total_frame, '2-Liter Sodas', row=7, col=0, font='Helvetica 12 bold', sticky=W)
        drink_cost_label = MyLabel(extra_total_frame, 'Price', row=7, col=1, font='Helvetica 12', sticky=W)
        drink_text = MyText(extra_total_frame, height=text_heights[3], width=25, row=8, col=0, state=DISABLED)
        drink_cost_text = MyText(extra_total_frame, height=text_heights[3], width=5, row=8, col=1, state=DISABLED)

        # define function to populate 'extra_total_frame' textareas
        def populate_extra_total_frame_text(extra_items_lists):
            """Populates 'extra_total_frame' section's Textareas with items and prices"""
            # create lists and dictionaries for extra_item pricing and labeling
            global extra_prices  # make extra prices dictionary global
            extra_prices = {'Breadsticks': 4.95, 'Garlic Bread': 4.95,
                            'Cheese': 0.99, 'Garlic Butter': 0.99, 'Marinara': 0.99, 'Ranch': 0.99,
                            'Cinnastix™': 4.95, 'Brownies': 3.65, 'Cookies': 2.95, 'Choc Cookies': 2.95,
                            'Coke': 2.25, 'Diet Coke': 2.25, 'Sprite': 2.25, 'Dr Pepper': 2.25,
                            'Mtn Dew': 2.25, 'Orange Soda': 2.25, 'Grape Soda': 2.25}  # 'extra prices' dictionary
            # populate 'extra_total_frame' textareas
            # populate 'side' section's textareas
            your_side_items = extra_items_lists[0]  # pull 'your_side_items' list out of extra_items_lists
            if not your_side_items:  # no side_items selected
                # side text
                side_text['state'] = NORMAL  # set 'side_text' state to normal
                side_text.insert(0.0, 'No Side Items')  # insert no side item text
                side_text['state'] = DISABLED  # set 'side_text' state to disabled
                # side cost text
                side_cost_text['state'] = NORMAL  # set 'side_cost_text' state to normal
                side_cost_text.insert(0.0, '$0.00')  # insert side cost text (No Charge)
                side_cost_text['state'] = DISABLED  # set 'side_cost_text' state to disabled
            else:  # side_items selected
                side_text['state'] = NORMAL  # set 'side_text' state to normal
                side_cost_text['state'] = NORMAL  # set 'side_cost_text' state to normal
                side_line = 0.0  # line variable for inserting side_items into textareas
                for your_side_item in your_side_items:  # iterate through side_item selections
                    side_text.insert(side_line, f'{your_side_item}\n')  # insert side text
                    side_price = float(extra_prices[your_side_item])  # get side_items price from extra_prices
                    side_cost_text.insert(side_line, f'$%0.2f' % side_price + '\n')  # insert side cost text
                    side_line += 1.0  # increment side_line
                side_text['state'] = DISABLED  # set 'side_text' state to disabled
                side_cost_text['state'] = DISABLED  # set 'side_cost_text' state to disabled
            # populate 'dipping_sauce' section's textareas
            your_sauce_items = extra_items_lists[1]  # pull 'your_sauce_items' list out of extra_items_lists
            if not your_sauce_items:  # no dipping_sauces selected
                # dipping text
                dipping_text['state'] = NORMAL  # set 'dipping_text' state to normal
                dipping_text.insert(0.0, 'No Dipping Sauces')  # insert no dipping sauce text
                dipping_text['state'] = DISABLED  # set 'dipping_text' state to disabled
                # dipping cost text
                dipping_cost_text['state'] = NORMAL  # set 'dipping_cost_text' state to normal
                dipping_cost_text.insert(0.0, '$0.00')  # insert dipping sauce cost text (No Charge)
                dipping_cost_text['state'] = DISABLED  # set 'dipping_cost_text' state to disabled
            else:  # dipping_sauces selected
                dipping_text['state'] = NORMAL  # set 'dipping_text' state to normal
                dipping_cost_text['state'] = NORMAL  # set 'dipping_cost_text' state to normal
                sauce_line = 0.0  # line variable for inserting dipping_sauces into textareas
                for your_sauce_item in your_sauce_items:  # iterate through dipping_sauce selections
                    dipping_text.insert(sauce_line, f'{your_sauce_item}\n')  # insert dipping sauce text
                    dipping_price = float(extra_prices[your_sauce_item])  # get dipping_sauce price from extra_prices
                    dipping_cost_text.insert(sauce_line, f'$%0.2f' % dipping_price + '\n')  # insert dip sauce cost text
                    sauce_line += 1.0  # increment sauce_line
                dipping_text['state'] = DISABLED  # set 'dipping_text' state to disabled
                dipping_cost_text['state'] = DISABLED  # set 'dipping_cost_text' state to disabled
            # populate 'dessert' section's textareas
            your_dessert_items = extra_items_lists[2]  # pull 'your_dessert_items' list out of extra_items_lists
            if not your_dessert_items:  # no dessert_items selected
                # dessert text
                dessert_text['state'] = NORMAL  # set 'dessert_text' state to normal
                dessert_text.insert(0.0, 'No Dessert Items')  # insert no dessert item text
                dessert_text['state'] = DISABLED  # set 'dessert_text' state to disabled
                # dessert cost text
                dessert_cost_text['state'] = NORMAL  # set 'dessert_cost_text' state to normal
                dessert_cost_text.insert(0.0, '$0.00')  # insert dessert cost text (No Charge)
                dessert_cost_text['state'] = DISABLED  # set 'dessert_cost_text' state to disabled
            else:  # dessert_items selected
                dessert_text['state'] = NORMAL  # set 'dessert_text' state to normal
                dessert_cost_text['state'] = NORMAL  # set 'dessert_cost_text' state to normal
                dessert_line = 0.0  # line variable for inserting dessert_items into textareas
                for your_dessert_item in your_dessert_items:  # iterate through dessert_item selections
                    dessert_text.insert(dessert_line, f'{your_dessert_item}\n')  # insert dessert text
                    dessert_price = float(extra_prices[your_dessert_item])  # get dessert_items price from extra_prices
                    dessert_cost_text.insert(dessert_line, f'$%0.2f' % dessert_price + '\n')  # insert dessert cost text
                    dessert_line += 1.0  # increment dessert_line
                dessert_text['state'] = DISABLED  # set 'dessert_text' state to disabled
                dessert_cost_text['state'] = DISABLED  # set 'dessert_cost_text' state to disabled
            # populate 'drink' section's textareas
            your_drink_items = extra_items_lists[3]  # pull 'your_drink_items' list out of extra_items_lists
            if not your_drink_items:  # no drinks selected
                # drink text
                drink_text['state'] = NORMAL  # set 'drink_text' state to normal
                drink_text.insert(0.0, 'No 2-Liter Sodas')  # insert no drink item text
                drink_text['state'] = DISABLED  # set 'drink_text' state to disabled
                # drink cost text
                drink_cost_text['state'] = NORMAL  # set 'drink_cost_text' state to normal
                drink_cost_text.insert(0.0, '$0.00')  # insert drink cost text (No Charge)
                drink_cost_text['state'] = DISABLED  # set 'drink_cost_text' state to disabled
            else:  # drinks selected
                drink_text['state'] = NORMAL  # set 'drink_text' state to normal
                drink_cost_text['state'] = NORMAL  # set 'drink_cost_text' state to normal
                drink_line = 0.0  # line variable for inserting drinks into textareas
                for your_drink_item in your_drink_items:  # iterate through drink selections
                    drink_text.insert(drink_line, f'{your_drink_item}\n')  # insert drink text
                    drink_price = float(extra_prices[your_drink_item])  # get drink price from extra_prices
                    drink_cost_text.insert(drink_line, f'$%0.2f' % drink_price + '\n')  # insert drink cost text
                    drink_line += 1.0  # increment dessert_line
                drink_text['state'] = DISABLED  # set 'drink_text' state to disabled
                drink_cost_text['state'] = DISABLED  # set 'drink_cost_text' state to disabled

        # populate 'extra_total_frame' textareas
        populate_extra_total_frame_text(your_extras)

    # generate extra_item total receipt
    generate_extra_total_receipt()

    # define function to generate and display the receipt for your order total
    def generate_order_total_receipt():
        """Generate and display the receipt for your order total"""

        # create 'order_total_frame' label frame to hold your order total receipt
        global order_total_frame  # make order_total_frame global
        order_total_frame = MyLabelFrame(payment_window, 'Order Total', row=1, col=4, font='Helvetica 16 bold',
                                         sticky=N)  # create 'order_total_frame'
        order_total_frame.grid(padx=(12, 0))  # add some padding to 'order_total_frame' (12px left)

        # create order total receipt sections
        # 'pizza price' section
        total_pizza_label = MyLabel(order_total_frame, 'Pizza Price', row=0, col=0, font='Helvetica 12 bold', sticky=W)
        total_pizza_cost_label = MyLabel(order_total_frame, 'Price', row=0, col=1, font='Helvetica 12', sticky=W)
        total_pizza_text = MyText(order_total_frame, height=1, width=25, row=1, col=0, state=DISABLED)
        total_pizza_cost_text = MyText(order_total_frame, height=1, width=7, row=1, col=1, state=DISABLED)
        # 'extras price' section
        total_extras_label = MyLabel(order_total_frame, 'Extra Items Price', row=2, col=0, font='Helvetica 12 bold',
                                     sticky=W)
        total_extras_cost_label = MyLabel(order_total_frame, '(+)', row=2, col=1, font='Helvetica 10 bold')
        total_sides_text = MyText(order_total_frame, height=1, width=25, row=3, col=0, state=DISABLED)
        total_sides_cost_text = MyText(order_total_frame, height=1, width=7, row=3, col=1, state=DISABLED)
        total_dipping_text = MyText(order_total_frame, height=1, width=25, row=4, col=0, state=DISABLED)
        total_dipping_cost_text = MyText(order_total_frame, height=1, width=7, row=4, col=1, state=DISABLED)
        total_dessert_text = MyText(order_total_frame, height=1, width=25, row=5, col=0, state=DISABLED)
        total_dessert_cost_text = MyText(order_total_frame, height=1, width=7, row=5, col=1, state=DISABLED)
        total_drink_text = MyText(order_total_frame, height=1, width=25, row=6, col=0, state=DISABLED)
        total_drink_cost_text = MyText(order_total_frame, height=1, width=7, row=6, col=1, state=DISABLED)
        # 'total order price' section
        order_total_label = MyLabel(order_total_frame, 'Order Total', row=7, col=0, font='Helvetica 12 bold', sticky=W)
        order_total_label.grid(pady=(5, 0))
        order_total_cost_label = MyLabel(order_total_frame, 'Price', row=7, col=1, font='Helvetica 12', sticky=W)
        order_total_cost_label.grid(pady=(5, 0))
        extras_total_text = MyText(order_total_frame, height=1, width=25, row=8, col=0, state=DISABLED)
        extras_total_cost_text = MyText(order_total_frame, height=1, width=7, row=8, col=1, state=DISABLED)
        sub_total_text = MyText(order_total_frame, height=1, width=25, row=9, col=0, state=DISABLED)
        sub_total_cost_text = MyText(order_total_frame, height=1, width=7, row=9, col=1, state=DISABLED)
        taxes_text = MyText(order_total_frame, height=1, width=25, row=10, col=0, state=DISABLED)
        taxes_cost_text = MyText(order_total_frame, height=1, width=7, row=10, col=1, state=DISABLED)
        order_total_text = MyText(order_total_frame, height=1, width=25, row=11, col=0, state=DISABLED)
        order_total_cost_text = MyText(order_total_frame, height=1, width=7, row=11, col=1, state=DISABLED)

        # define a function to populate 'order total' textareas
        def populate_order_total_frame_text(extra_selections):
            """Populates 'order_total_frame' section's Textareas with items and prices"""
            # populate 'order_total_frame' section's textareas
            # 'total order price' section
            # populate 'pizza price' textareas
            # total pizza text
            total_pizza_text['state'] = NORMAL  # set 'total_pizza_text' state to normal
            if custom_value is True:  # pizza has been customized
                total_pizza_text.insert(0.0, 'Your Masterpie-zza™')  # insert total pizza text
            else:  # pizza hasn't been customized
                total_pizza_text.insert(0.0, 'Your Pizza')  # insert total pizza text
            total_pizza_text['state'] = DISABLED  # set 'total_pizza_text' state to disabled
            # total pizza cost text
            total_pizza_cost_text['state'] = NORMAL  # set 'total_pizza_cost_text' state to normal
            total_pizza_cost_text.insert(0.0, '$%0.2f' % pizza_price)  # insert total pizza cost text
            total_pizza_cost_text['state'] = DISABLED  # set 'total_pizza_cost_text' state to disabled

            # 'extras prices' section
            # populate 'sides' textareas
            # total sides section
            total_sides_text['state'] = NORMAL  # set 'total_sides_text' state to normal
            sides_selection = extra_selections[0]  # pull 'sides_selection' from extra_selections
            if not sides_selection:  # no sides selected
                total_sides_text.insert(0.0, 'No Side Items')  # insert total sides text
            else:  # sides selected
                total_sides = len(sides_selection)  # determine how many sides were selected
                total_sides_text.insert(0.0, f'{total_sides} Side Items')  # insert total sides text
            total_sides_text['state'] = DISABLED  # set 'total_sides_text' state to disabled
            # total sides cost text
            total_sides_cost_text['state'] = NORMAL  # set 'total_sides_cost_text' state to normal
            total_sides_cost = 0.00  # initialize total_sides_cost variable
            if not sides_selection:  # no sides selected
                total_sides_cost_text.insert(0.0, '$0.00')  # insert total slides cost text
            else:  # sides selected
                for side_selection in sides_selection:  # iterate through selected sides
                    side_selection_price = extra_prices[side_selection]  # get selected side's price
                    total_sides_cost += side_selection_price  # accumulate total_sides_cost with each side_price
                total_sides_cost_text.insert(0.0, '$%0.2f' % total_sides_cost)  # insert side cost text
            total_sides_cost_text['state'] = DISABLED  # set 'total_sides_cost_text' state to disabled
            # populate 'dipping' textareas
            # total dipping section
            total_dipping_text['state'] = NORMAL  # set 'total_dipping_text' state to normal
            dipping_selection = extra_selections[1]  # pull 'dipping_selection' from extra_selections
            if not dipping_selection:  # no sauces selected
                total_dipping_text.insert(0.0, 'No Dipping Sauces')  # insert total dipping text
            else:  # sauces selected
                total_dipping = len(dipping_selection)  # determine how many sauces were selected
                total_dipping_text.insert(0.0, f'{total_dipping} Dipping Sauces')  # insert total dipping text
            total_dipping_text['state'] = DISABLED  # set 'total_dipping_text' state to disabled
            # total dipping cost text
            total_dipping_cost_text['state'] = NORMAL  # set 'total_sides_cost_text' state to normal
            total_dipping_cost = 0.00  # initialize total_dipping_cost variable
            if not dipping_selection:  # no sauces selected
                total_dipping_cost_text.insert(0.0, '$0.00')  # insert total slides cost text
            else:  # sides selected
                for sauce_selection in dipping_selection:  # iterate through selected sauces
                    dipping_selection_price = extra_prices[sauce_selection]  # get selected sauces's price
                    total_dipping_cost += dipping_selection_price  # accumulate total_dipping_cost with each sauce_price
                total_dipping_cost_text.insert(0.0, '$%0.2f' % total_dipping_cost)  # insert dipping cost text
            total_dipping_cost_text['state'] = DISABLED  # set 'total_dipping_cost_text' state to disabled
            # populate 'dessert' textareas
            # total dessert section
            total_dessert_text['state'] = NORMAL  # set 'total_dessert_text' state to normal
            dessert_selection = extra_selections[2]  # pull 'dessert_selection' from extra_selections
            if not dessert_selection:  # no dessert selected
                total_dessert_text.insert(0.0, 'No Dessert Items')  # insert total dessert text
            else:  # desserts selected
                total_dessert = len(dessert_selection)  # determine how many desserts were selected
                total_dessert_text.insert(0.0, f'{total_dessert} Dessert Items')  # insert total dessert text
            total_dessert_text['state'] = DISABLED  # set 'total_dessert_text' state to disabled
            # total dessert cost text
            total_dessert_cost_text['state'] = NORMAL  # set 'total_dessert_cost_text' state to normal
            total_dessert_cost = 0.00  # initialize total_dessert_cost variable
            if not dessert_selection:  # no dessert selected
                total_dessert_cost_text.insert(0.0, '$0.00')  # insert total dessert cost text
            else:  # desserts selected
                for dessert_selected in dessert_selection:  # iterate through selected desserts
                    dessert_selection_price = extra_prices[dessert_selected]  # get selected desserts's price
                    total_dessert_cost += dessert_selection_price  # accumulate total_dessert_cost with each dess_price
                total_dessert_cost_text.insert(0.0, '$%0.2f' % total_dessert_cost)  # insert dessert cost text
            total_dessert_cost_text['state'] = DISABLED  # set 'total_dessert_cost_text' state to disabled
            # populate 'drink' textareas
            # total drinks section
            total_drink_text['state'] = NORMAL  # set 'total_drink_text' state to normal
            drink_selection = extra_selections[3]  # pull 'drink_selection' from extra_selections
            if not drink_selection:  # no drink selected
                total_drink_text.insert(0.0, 'No 2-Liter Sodas')  # insert total drink text
            else:  # drinks selected
                total_drinks = len(drink_selection)  # determine how many drinks were selected
                total_drink_text.insert(0.0, f'{total_drinks} 2-Liter Sodas')  # insert total drink text
            total_drink_text['state'] = DISABLED  # set 'total_drink_text' state to disabled
            # total drink cost text
            total_drink_cost_text['state'] = NORMAL  # set 'total_drink_cost_text' state to normal
            total_drink_cost = 0.00  # initialize total_drink_cost variable
            if not drink_selection:  # no drinks selected
                total_drink_cost_text.insert(0.0, '$0.00')  # insert total drink cost text
            else:  # drinks selected
                for drink_selected in drink_selection:  # iterate through selected drinks
                    drink_selection_price = extra_prices[drink_selected]  # get selected drinks's price
                    total_drink_cost += drink_selection_price  # accumulate total_drink_cost with each dess_price
                total_drink_cost_text.insert(0.0, '$%0.2f' % total_drink_cost)  # insert drink cost text
            total_drink_cost_text['state'] = DISABLED  # set 'total_drink_cost_text' state to disabled

            # populate the 'total order price' section's textareas
            # 'extras total' section
            # extra total text
            extras_total_text['state'] = NORMAL  # set 'extras_total_text' state to normal
            extras_total_text.insert(0.0, 'Extra Items Total')  # insert extras total text
            extras_total_text['state'] = DISABLED  # set 'extras_total_text' state to disabled
            # extra total cost text
            extras_total_cost_text['state'] = NORMAL  # set 'extras_total_cost_text' state to normal
            if not extra_list:  # no extra items selected
                extras_total_cost_text.insert(0.0, '$0.00')  # insert extra total cost text
                extras_final = 0.00  # initialize 'extras_final' accumulator variable
            else:  # extra items selected
                extras_total = total_sides_cost + total_dipping_cost + total_dessert_cost + total_drink_cost  # add ext
                extras_final = round(extras_total, 2)  # round the sum of all the extra_item categories
                extras_total_cost_text.insert(0.0, '$%0.2f' % extras_final)  # insert extra cost text
            extras_total_cost_text['state'] = DISABLED  # set 'extras_total_cost_text' state to disabled
            # 'order subtotal' section
            # sub total text
            sub_total_text['state'] = NORMAL  # set 'sub_total_text' state to normal
            sub_total_text.insert(0.0, 'Order Subtotal')  # insert sub total text
            sub_total_text['state'] = DISABLED  # set 'sub_total_text' state to disabled
            # sub total cost text
            sub_total_cost_text['state'] = NORMAL  # set 'sub_total_cost_text' state to normal
            sub_total = pizza_price + extras_final  # add the extras price to the pizza price
            sub_final = round(sub_total, 2)  # round the subtotal cost
            sub_total_cost_text.insert(0.0, '$%0.2f' % sub_final)  # insert sub total cost text
            sub_total_cost_text['state'] = DISABLED  # set 'sub_total_cost_text' state to disabled
            # 'taxes' section
            # taxes text
            taxes_text['state'] = NORMAL  # set 'taxes_text' state to normal
            taxes_text.insert(0.0, 'Sales Tax (8%)')  # insert tax text
            taxes_text['state'] = DISABLED  # set 'taxes_text' state to disabled
            # taxes cost text
            taxes_cost_text['state'] = NORMAL  # set 'taxes_cost_text' state to normal
            SALES_TAX = 0.08  # sales tax constant
            taxes = sub_final * SALES_TAX  # calculate sales tax cost
            taxes_final = round(taxes, 2)  # round sales tax cost
            taxes_cost_text.insert(0.0, '$%0.2f' % taxes_final)  # insert sales tax cost
            taxes_cost_text['state'] = DISABLED  # set 'taxes_cost_text' state to disabled
            # 'order total' section
            # order total text
            order_total_text['state'] = NORMAL  # set 'order_total_text' state to normal
            order_total_text.insert(0.0, 'Order Total')  # insert order total text
            order_total_text['state'] = DISABLED  # set 'order_total_text' state to disabled
            # order total cost text
            order_total_cost_text['state'] = NORMAL  # set 'order_total_cost_text' state to normal
            order_total = sub_final + taxes_final  # calculate the order total cost
            global order_final  # make order_final global
            order_final = round(order_total, 2)  # round the order total cost
            order_total_cost_text.insert(0.0, '$%0.2f' % order_final)  # insert order total cost text
            order_total_cost_text['state'] = DISABLED  # set 'order_total_cost_text' state to disabled

        # populate 'order_total_frame' textareas (with the function defined above)
        populate_order_total_frame_text(your_extras)

    # generate order total receipt
    generate_order_total_receipt()

    # navigation functions
    # 'back' button function
    def back_payment():
        """Loads the previous module and destroys the current window (also passes variables on to the that module)"""
        payment_window.destroy()  # destroy this window
        if custom_value is True:  # customized pizza
            extras.add_extras(pickup, p_size, p_base, your_pizza, custom, changes)  # passes variables to last module
        else:  # base pizza (not customized)
            extras.add_extras(pickup, p_size, p_base, your_pizza)  # passes variables to last module

    # 'exit' button function
    def exit_payment():
        """Exits the current window and resets variables"""
        p_size.set(0)  # reset 'size' variable (avoid weird behavior)
        p_base = IntVar()  # reset p_base as a tkinter variable (instead of an integer, so it can be reset below)
        p_base.set(0)  # reset 'base' variable (avoid weird behavior)
        your_pizza = None  # reset 'your_pizza' variable (avoid weird behavior)
        custom = False  # reset 'custom' variable (avoid weird behavior)
        changes = None  # reset 'changes' list (avoid weird behavior)
        payment_window.destroy()  # destroy this window

    # 'next' button function
    def next_final():
        """Loads the next module and destroys the current window (also passes variables on to the next module)"""
        payment_window.destroy()  # destroy this window
        final.finalize_order(pickup_value, order_final)  # load the next module

    # program navigation
    nav_frame = MyFrame(payment_window, row=3, col=0, colspan=5, sticky=N+S)  # navigation frame
    nav_frame.grid(pady=(40, 0))  # padding on navigation frame (40px top)
    back_btn = MyButton(nav_frame, '<< Back', row=0, col=0, command=back_payment)  # back button
    exit_btn = MyButton(nav_frame, 'EXIT', row=0, col=1, command=exit_payment)  # exit button
    next_btn = MyButton(nav_frame, 'Next >>', row=0, col=2, command=next_final)  # next button
