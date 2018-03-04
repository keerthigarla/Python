import random
for i in range(1,7):
    if i == 1:
        a = input('Guess a number: ')
        x = random.randint(1, 100)
        if a.lstrip('-').isdigit()==True:
            a1=int(a)
            if a1==x:
                print('You have guessed it right!!')
            else:
                if a1>x:
                    r=a1-x
                    print('Number is high by', r, ' !!')
                else:
                    r=x-a1
                    print('Number is low by', r, ' !!')
                continue
        else:
            print('Its not a number!!')
    elif i > 1:
        b= input('Guess a number again: ')
        y = random.randint(1, 100)
        if b.lstrip('-').isdigit()==True:
            b1= int(b)
            if b1 ==y:
                print('You have guessed it right!!')
            else:
                if b1>y:
                    r=b1-y
                    print('Number is high by', r, ' !!')
                else:
                    r=y-b1
                    print('Number is low by', r, ' !!')
                #break
                continue
        else:
            print('Its not a number!!')
    else:
        print('End of program')
        break
