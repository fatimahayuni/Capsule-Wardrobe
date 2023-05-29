occasions = ["WORK FORMAL", "SMART CASUAL", "FANCY GIRLY WEEKEND", "CASUAL WEEKEND"]

bottom = ['black tailored pants', 'stone tailored pants', 'taupe casual pants', 'dark blue jeans', 'black tailored skirt', 'casual skirt', 'stone shorts']
top = ['black long-sleeved top', 'white or accent color long-sleeved top', 'black tank top', 'white tank top', 'accent color blouse 1', 'accent color blouse 2']

index = 0
for x in bottom:
  for y in top:
    index += 1
    print(str(index) + ". " + x + " + " + y)