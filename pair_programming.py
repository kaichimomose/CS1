import random

def roll_dice(nds):
    nds.replace(" ", "")
    nds.split(" ")
    nds[1].lower()
    if nds[2:] is int:
        number = int(nds[0]) * int(nds[2:])
        print(random.randint(1, number))
    else:
        print("Invalid format")

 # roll_dice("2 d6")

def find_two_number(lists, target):
    qualified = []
    for i in lists:
        if i < target:
            qualified.append(i)
    j = 0
    while j < len(qualified):
        if qualified[j] + qualified[j+1] == target:
            print("%s %s" % (qualified[j], qualified[j+1]))
            return
        elif qualified[j] + qualified[j+2] == target:
            print("%s %s" % (qualified[j], qualified[j+2]))
            return
        elif qualified[j] + qualified[j+3] == target:
            print("%s %s" % (qualified[j], qualified[j+2]))
            return
        else:
            j += 1

find_two_number([1, 9, 3, 4], 13)
