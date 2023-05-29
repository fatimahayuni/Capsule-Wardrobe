user_selected_clothes = ['black long tailored pants', 'black long-sleeved top', 'black blazer', 'black shoes', 'black tote']
index = 0
for x in user_selected_clothes:
    index += 1
    print(str(index) + ". " + x)
user_selected_clothes[1] = '* item deleted *'


print()

index = 0
for x in user_selected_clothes:
    index += 1
    print(str(index) + ". " + x)

