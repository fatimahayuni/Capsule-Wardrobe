occasions = ["WORK FORMAL", "SMART CASUAL", "FANCY DATE WEEKEND", "CASUAL WEEKEND"]
bottoms = ['black tailored pants', 'stone tailored pants', 'taupe casual pants', 'dark blue jeans', 'black tailored skirt', 'casual skirt', 'stone shorts']
tops = ['black long-sleeved top', 'white or accent color long-sleeved top', 'black tank top', 'white tank top', 'accent color blouse 1', 'accent color blouse 2']
top_layers = ['black blazer', 'stone blazer', 'black cardigan']
shoes = ['black pumps', 'strappy black heels', 'ankle-length boots', 'dressy flat sandals', 'black ballet flats', 'patent-leather tan wedges']
bags = ['black tote', 'beige tote', 'black clutch']
dresses = ['little black dress', 'casual printed dress']


print("What is the occasion?")
index = 0
for x in occasions:
    index += 1
    print(str(index) + ". " + x)
occasion_input = input("Enter the number: ")
occasion_input_index_integer = int(occasion_input) - 1
print("You have selected " + occasions[occasion_input_index_integer] + " style.")
print()

combination = []

def print_list(list_name, list):
    print("What is the " + list_name + " that you want?")
    index = 0
    for x in list:
        index += 1
        print(str(index) + ". " + x)
    list_name_input = input("Enter the number: ")
    list_name_index_integer = int(list_name_input) - 1
    combination.append(list_name_index_integer)
    print("So you want " + list[list_name_index_integer] + ".")
    print()
    return list[list_name_index_integer]
    

print_list("bottoms", bottoms)
print_list("tops", tops)
print_list("top layer", top_layers)
print_list("shoe", shoes)
print_list("bags", bags)


def convert_index_to_strings(list):
    for x in combination:
        combination_index_to_clothing_list_strings = list[x]
    print(combination_index_to_clothing_list_strings)



convert_index_to_strings(bottoms)
convert_index_to_strings(tops)
convert_index_to_strings(top_layers)
convert_index_to_strings(shoes)
convert_index_to_strings(bags)

exit(1)


   
'''
Output that I want:
So you want bottom.
So you want bottom + top.
So you want bottom + top + top layer.
So you want bottom + top + top layer + shoes.
So you want bottom + top + top layer + shoes + bags.

combinations = [0,0,0,0,0]
combinations = ["black bottom", "black top", "black blazer", "black pumps", "black tote"]
combinations = [
    bottoms[0],
    tops[0],
    top_layers[0],
    shoes[0],
    bags[0]
]

'''


# You have selected black tailored pants + black long-sleeved top + black blazer + black pumps + black tote. 

# #Q: What's the occasion?
# print("What's the occasion?")
# index = 0
# for x in occasions:
#     index += 1
#     print(str(index) + " " + x)
# print("Enter the number: ")
# occasion_input = input()
# print()

#-------------------------------------------------------------------
# Q: What bottom do you want to wear?
print("So you want " + occasions[int(occasion_input) - 1] + ". What bottom do you want to wear today?")
index = 0
for x in bottoms:
    index += 1
    print(str(index) + " " + x)
print("Enter the number: ")
bottom_input = input()
print()

#-------------------------------------------------------------------
# Q: What top do you want to go with that?
print("So you want " + bottoms[int(bottom_input) - 1] + ". What top do you want to go with that?")
index = 0
for x in tops:
    index += 1
    print(str(index) + " " + x)
print("Enter the number: ")
top_input = input()
print()

#-------------------------------------------------------------------
# Q: What shoes do you want to go with that?
print("So you want " + bottoms[int(bottom_input) - 1] + " + " + tops[int(top_input) - 1] + ". What shoes do you want to go with that?")
index = 0
for x in shoes:
    index += 1
    print(str(index) + " " + x)
print("Enter the number: ")
shoe_input = input()
print()

#-------------------------------------------------------------------
# Q: What bags do you want to go with that?
print("So you want " + bottoms[int(bottom_input) - 1] + " + " + tops[int(top_input) - 1] + " + " + shoes[int(shoe_input) - 1] + ". What bags do you want to go with that?")
index = 0
for x in bags:
    index += 1
    print(str(index) + " " + x)
print("Enter the number: ")
bag_input = input()
print()

print("So you want " + bottoms[int(bottom_input) - 1] + " + " + tops[int(top_input) - 1] + " + " + shoes[int(shoe_input) - 1] + " + " + bags[int(bag_input) - 1] + ". Great choice! Don't forget to take a selfie!")
