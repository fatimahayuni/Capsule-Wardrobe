
def output_question(question_dict):
    response = ""
    for index, element in enumerate(question_dict):
        response += element + ": " + question_dict[element] + "\n"
    return response


def output_combination_question(combination, question_dict):
    """for each dict element, append the combination to the end as your output"""
    response = ""
    for index, element in enumerate(question_dict):
        response += element + ": " + combination + " + " + question_dict[element] + "\n"
    return response


occasions = {
    "1": "WORK FORMAL",
    "2": "SMART CASUAL",
    "3": "FANCY DATE WEEKEND",
    "4": "CASUAL PLAY WEEKEND"
}

bottoms = {
    "1": "Black tailored pants",
    "2": "Stone tailored pants",
    "3": "Taupe casual pants",
    "4": "Dark blue jeans",
    "5": "Stone color shorts"
}

tops = {
    "1": "black long-sleeved top",
    "2": "white or accent color long-sleeved top",
    "3": "black tank top",
    "4": "white tank top",
    "5": "accent color blouse 1",
    "6": "accent color blouse 2"
}

shoes = {
    "1": "strappy black heels",
    "2": "ankle length boots",
    "3": "black ballet flats",
    "4": "patent leather tan wedges",
    "5": "nude wedges"
}

topLayer = {
    "1": "black blazer",
    "2": "stone blazer",
    "3": "black cardigan"
}

handbags = {
    "1": "black tote",
    "2": "beige tote",
    "3": "black clutch"
}

print("What's the occasion?")
print(output_question(occasions))
answer = input()
if answer not in occasions.keys():
    print("invalid choice for occasion")
    exit(1)

chosenOccasion = occasions[answer]

print("So you want " + chosenOccasion)
print("What bottom are you planning to wear today?")
print(output_question(bottoms))
answer = input()
if answer not in bottoms.keys():
    print("Invalid choice for bottoms")
    exit(1)

# list the possible combinations between the bottoms and tops
chosenBottom = bottoms[answer]
print(output_combination_question(chosenBottom, tops))
answer = input()
if answer not in tops.keys():
    print("Invalid choice for tops")
    exit(1)
chosenTop = tops[answer]

combo = chosenBottom + " + " + chosenTop
print(output_combination_question(combo, shoes))
answer = input()
if answer not in shoes.keys():
    print("Invalid choice for shoes")
    exit(1)
chosenShoes = shoes[answer]

combo = combo + " + " + chosenShoes
print("You chose " + combo + ". Nice!")
answer = input("Do you want to add top layer? Enter Y or N. ")

chosenTopLayer = ""  # just in case we need to use it later
if answer.lower() == "Y".lower():
    print(output_combination_question(combo, topLayer))
    answer = input()
    if answer not in topLayer.keys():
        print("Invalid choice for topLayer")
        exit(1)
    chosenTopLayer = topLayer[answer]
    combo = combo + " + " + chosenTopLayer

answer = input("handbag now? Y or N. ")
if answer.lower() == "Y".lower():
    print(output_combination_question(combo, handbags))
    answer = input()
    if answer not in handbags.keys():
        print("Invalid choice for handbags")
        exit(1)
    chosenHandbag = handbags[answer]
    combo = combo + " + " + chosenHandbag

print("enjoy your " + chosenOccasion + " wearing your " + combo)