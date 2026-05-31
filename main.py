import random
discovered_num = {}
numbers = {random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10)}

print(numbers)


while True:

    answ = int(input('what number do you think is in the set? (there are 4)'))

    if answ in numbers:
        print("you got the answer correct!")
        if answ not in discovered_num:
            discovered_num.add(answ)

    else:
        print("incorrect, try again")

    if numbers == discovered_num:
        print('you discovered all numbers!')
        break