import itertools
bottom = ['black tailored pants', 'stone tailored pants', 'taupe casual pants', 'dark blue jeans', 'black tailored skirt', 'casual skirt', 'stone shorts']
top = ['black long-sleeved top', 'white or accent color long-sleeved top', 'black tank top', 'white tank top', 'accent color blouse 1', 'accent color blouse 2']
top_layer = ['black blazer', 'stone blazer', 'black cardigan']
shoe = ['black pumps', 'strappy black heels', 'ankle-length boots', 'dressy flat sandals', 'black ballet flats', 'patent-leather tan wedges']
bag = ['black tote', 'beige tote', 'black clutch']
dress = ['little black dress', 'casual printed dress']

index = 0
for a in bottom:
  for b in top:
    for c in top_layer:
        for d in shoe:
            for e in bag:
                index += 1
                print(str(index) + ". " + a + " + " + b + " + " + c + " + " + d + " + " + e)




