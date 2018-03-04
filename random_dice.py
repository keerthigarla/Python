import random
for i in range(1,100):
    if i == 1:
        a=input('would you like to roll a dice. If yes then enter (yes) else (no): ')
        if a in ('yes', 'y', 'Yes', 'YES', 'Y'):
            x = random.randint(1, 6)
            print(x)
        else:
            print('End of program')
            break
    elif i > 1:
        b= input('would you like to roll a dice again. If yes then enter (yes) else (no): ')
        if b in ('yes', 'y', 'Yes', 'YES', 'Y'):
            y = random.randint(1, 6)
            print(y)
        else:
            print('End of program')
            break
    else:
        print('End of program')
        break
