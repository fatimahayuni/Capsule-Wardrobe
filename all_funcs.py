occasions = ["WORK FORMAL", "SMART CASUAL", "FANCY GIRLY WEEKEND", "CASUAL WEEKEND"]

# clothing_list_variable
bottom = ['black tailored pants', 'stone tailored pants', 'taupe casual pants', 'dark blue jeans', 'black tailored skirt', 'casual skirt', 'stone shorts']
top = ['black long-sleeved top', 'white or accent color long-sleeved top', 'black tank top', 'white tank top', 'accent color blouse 1', 'accent color blouse 2']
top_layer = ['black blazer', 'stone blazer', 'black cardigan']
shoe = ['black pumps', 'strappy black heels', 'ankle-length boots', 'dressy flat sandals', 'black ballet flats', 'patent-leather tan wedges']
bag = ['black tote', 'beige tote', 'black clutch']
dress = ['little black dress', 'casual printed dress']

user_selected_clothes = []


#1st function: To select occasion.
def select_occasion():
    print("What is the occasion?")
    index = 0
    for x in occasions:
        index += 1
        print(str(index) + ". " + x)
    try:
        occasion_input_string = input("Enter the number: ")
        occasion_input_integer = int(occasion_input_string) - 1
        print("You have selected " + occasions[occasion_input_integer] + " style.")
        print()
    except:
        occasion_error_message = f"Please enter number between 1-4."
        print(occasion_error_message)
        print()
        select_occasion()

#2nd function: To add clothes.
def add_clothes(clothing_list_string, clothing_list_variable):
    print("What is the " + clothing_list_string + " that you want?")
    index = 0
    for clothing_item in clothing_list_variable:
        index += 1
        print(str(index) + ". " + clothing_item)
    try:
        clothing_name_input_string = input("Enter the number: ")
        clothing_name_input_integer = int(clothing_name_input_string) - 1
        user_selected_clothes.append(clothing_list_variable[clothing_name_input_integer])
        user_selected_clothing_items_strings = " + ".join(user_selected_clothes)
        print("You have chosen " + user_selected_clothing_items_strings + ".")
        print()
        return clothing_list_variable[clothing_name_input_integer]
    except:
        index_error_message = f"ALERT: Please enter the number within range of list. Also enter like '1' not 'one' ."
        print(index_error_message)
        print()
        add_clothes(clothing_list_string, clothing_list_variable)

#3rd function: To delete clothes
def delete_clothes():
    delete_input_string = ''
    while user_selected_clothes != ['* item deleted *', '* item deleted *', '* item deleted *', '* item deleted *', '* item deleted *']:
        delete_input_string = input("What do you want to delete? Enter the number: ")
        delete_input_integer = int(delete_input_string)
        delete_input_integer_index = delete_input_integer - 1
        print()

        user_selected_clothes[delete_input_integer_index] = '* item deleted *'
        index = 0
        for x in user_selected_clothes:
            index += 1
            print(str(index) + ". " + x)
    print("No more items to delete in the list")
    print()

#4th function: ADD / DELETE / DONE
def add_delete_done():
    change_input_string = input("* ADD / DELETE / DONE:  ")
    if change_input_string == "ADD":
        user_selected_clothes.clear()
        add_clothes("bottom", bottom)
        add_clothes("top", top)
        add_clothes("top layer", top_layer)
        add_clothes("shoes", shoe)
        add_clothes("bag", bag)
    elif change_input_string == "DELETE":
        index = 0
        for x in user_selected_clothes:
            index += 1
            print(str(index) + ". " + x)
        delete_clothes()
    elif change_input_string == "DONE":
        print("Don't forget to take a selfie!")
    print()