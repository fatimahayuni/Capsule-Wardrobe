from all_funcs import *

print()
select_occasion()
add_clothes("bottom", bottom)
add_clothes("top", top)
add_clothes("top layer", top_layer)
add_clothes("shoes", shoe)
add_clothes("bag", bag)
print()

add_delete_done()

"""
TODAY'S TASK:
1. Do the generator
1. Fix Github repo. 

BUGS:
1. When I enter anything other than DELETE or ADD or HAPPY, like number 1 or 'ayuni', THERE WILL BE A BUGGGGGG. 
2. Make it specifically either 'DELETE' or 'delete' ONLY. Make DELETE case-insensitive.


THOUGHTS: 
1. What if the user wants to add or delete items IN THE clothing_categories list. Ie; I want to add a new bottom to existing bottom list?

Ongoing tasks:
- When the user adds clothes back into the collection, the program ends. I want the program to continuously ask at any point if the user wants to delete or add item. 
Instead of add all collections, and then delete all collections.
- Top layer, make optional. 

"""