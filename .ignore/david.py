def output_question(question_dict):
    response = ""
    for index, element in enumerate(question_dict):
        response += element + ": " + question_dict[element] + "\n"
    return response


#  By convention, Q will point to the question for this block,
# other entries are the actual question id and text

qStart = {
    'Q': 'What\'s the occasion?',
    '1': 'Work formal',
    '2': 'Smart casual',
    '3': 'Fancy date weekend',
    '4': 'Casual play weekend'
}

qWorkFormal = {
    'Q': 'So you want something WORK FORMAL because you will be in the office all day! What bottom are you planning to wear today?',
    '1': 'Black tailored pants',
    '2': 'Stone tailored pants',
    '3': 'Taupe casual pants',
    '4': 'Dark blue jeans',
    '5': 'Black tailored skirt',
    '6': 'Casual skirt',
    '7': 'Stone shorts'
}

qSmartCasual = {
    'Q': "So you want something SMART CASUAL. What bottom are you planning to wear?",
    '1': 'Black tailored pants',
    '2': 'Stone tailored pants',
    '3': 'Taupe casual pants',
    '4': 'Dark blue jeans',
    '5': 'Black tailored skirt',
    '6': 'Casual skirt',
    '7': 'Stone shorts'
}

qFancyDateWeekend = {
    'Q': 'So you want to go on a FANCY DATE on a weekend! What bottom are you planning to wear?',
    '1': 'Black tailored pants',
    '2': 'Stone tailored pants',
    '3': 'Taupe casual pants',
    '4': 'Dark blue jeans',
    '5': 'Black tailored skirt',
    '6': 'Casual skirt',
    '7': 'Stone shorts'
}

qCasualPlayWeekend = {
    'Q': 'So you want to go on a CASUAL PLAY on a weekend! What bottom are you planning to wear?',
    '1': 'Black tailored pants',
    '2': 'Stone tailored pants',
    '3': 'Taupe casual pants',
    '4': 'Dark blue jeans',
    '5': 'Black tailored skirt',
    '6': 'Casual skirt',
    '7': 'Stone shorts'

}


# let us get the first question and ask it
print(output_question(qStart))
answer = input("Enter answer: ")

# we use the answer to find the next question
print('Thanks for answering ' + answer)

# do we yet support this answer? exit if we do not
if answer not in "1":  # add more supported numbers as you implement them
    print('Answer not yet supported: You are not allowed to have fun, only to go out formally')
    exit(1)  # exit to system saying some kind of error

# use the answer to find the next series of questions
if answer == "1":
    print(output_question(qWorkFormal))
    answer = input("Enter answer: ")

if answer == "2":
    print(output_question(qSmartCasual))
    answer = input("Enter answer: ")

print("We now have answer " + answer + " and can go on to the next question")