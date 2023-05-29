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