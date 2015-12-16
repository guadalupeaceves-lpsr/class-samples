icecreamflavors = ['Chocolate', 'Vanilla', 'Strawberry', 'Salted Caramel', 'Mint Chip']
print("These are our ice cream flavors:")
print(icecreamflavors)
print("Want to add an ice cream flavor? Enter it now:")
newicecreamflavor = raw_input()
newicecreamflavor = [newicecreamflavor] 
newmenu = icecreamflavors + newicecreamflavor
print("Great! Here's our menu:")
print(newmenu)
import random
randomicecreamflavor = random.randint(0,5)
randomicecreamflavor = newmenu[randomicecreamflavor]
print("Your flavor for today has been chosen randomly. Enjoy " + randomicecreamflavor + "!")

