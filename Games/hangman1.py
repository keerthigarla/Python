import random
def guess_w():
    word_list = ('orange','apple', 'fig', 'guava')
    word = str(random.choice(word_list))
    print(word)

    lst = list(word)
    print(lst)

    lst1= []
    for i in range(1, 11):
        if len(lst)!=len(lst1):
            x=input('Guess a letter: ')
            print('You have ', 10-i, ' chances remaining to guess the word')
            if x in lst:
                #print('You have guessed it right')
                if lst[0] == x:
                    print('You have guessed the first letter of the word, Go on')
                    #lst1[0] = x
                    lst1.append(x)
                    continue
                elif lst[len(lst)-1] == x:
                    print('You have guessed the last letter of the word, Go on')
                    #lst1[len(lst)-1] = x
                    lst1.append(x)
                    continue
                else:
                    print('You have guessed a letter from the middle of the word, Go on')
                    lst1.append(x)
                    continue
            else:
                print('Wrong Letter!!, Please try again')
                continue
        else:
            print('You have guessed the right word')
            break

    for i in range(0, len(lst1)):
        if len(lst) == len(lst1):
            if lst1[i] in lst:
                x='You have guessed right word'
            else:
                x='You have guessed wrong word'
        else:
            x = 'You have guessed wrong word'
    return print(x, ':', ' word is ', word)
guess_w()
