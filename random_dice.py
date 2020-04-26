import random

print("This is a rolling dice simulator")
min_dice = 1
max_dice = 6
while True:
    print(random.randint(min_dice,max_dice))
    nExt = input("Roll again? ")
    if nExt.startswith("y"):
        continue
    else:
        break
