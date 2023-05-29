user_selected_clothes = ["apple", "banana", "cherry", "duku"]

index = 0
for x in user_selected_clothes:
    index += 1
    print(str(index) + ". " + x)
print()

delete_input = ''
while user_selected_clothes != ['* item deleted *', '* item deleted *', '* item deleted *', '* item deleted *']:
    print("What do you want to delete? Enter the number: ")
    delete_input = int(input()) #make line 11 and 12 into one line in terminal. 
    delete_input_index = delete_input - 1
    print()

    user_selected_clothes[delete_input_index] = '* item deleted *'
    index = 0
    for x in user_selected_clothes:
        index += 1
        print(str(index) + ". " + x)
print("No more items to delete in the list. Do you want to add items back in now? Type YES or NO.")
print()
