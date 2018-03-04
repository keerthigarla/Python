def findDol3():
    d = input('Start moving by selecting the direction (L=Left, R=Right, B=Back, F=Forward). Please make sure you select only one direction at a time')
    s = input('Please select the number of steps. Please make sure you select only between 1 and 6')
    if d in ('F', 'f'):
        while s.lstrip('-').isdigit()==True:
            s=int(s)
            if s <=4:
                print('Right way!! You have taken ' , s , ' steps so far')
                if s==4:
                    return print('Congratulations!! You have reached Dollars filled room')
                else:
                    s1=4-s
                    print('you are short by ', s1 ,' steps')
                    s = input('Please select the number of steps again. Please make sure you select only between 1 and 6')
                    s=int(s)
                    while s<=s1:
                        if s==s1:
                            return print('Congratulations!! You have reached Dollars filled room')
                        else:
                            print('wrong number, please enter ', s1, ' steps' )
                            s = input('Please select the number of steps again. Please make sure you select only between 1 and 6')
                            s=int(s)
                            continue
            else:
                s = input('out of range, please enter the steps only between 1 and 6')
                s = input('Please select the number of steps again. Please make sure you select only between 1 and 6')
                s=int(s)
                continue
    else:
        print('Wrong Dirction')
        findDol3()
    #return print(x)

def findDol2():
    d = input('Start moving by selecting the direction (L=Left, R=Right, B=Back, F=Forward). Please make sure you select only one direction at a time')
    s = input('Please select the number of steps. Please make sure you select only between 1 and 6')
    if d in ('L', 'l'):
        while s.lstrip('-').isdigit()==True:
            s=int(s)
            if s <=6:
                print('Right way!! You have taken ' , s , ' steps so far')
                if s==6:
                    print('Choose another direction and steps')
                    return findDol3()
                else:
                    s1=6-s
                    print('you are short by ', s1 ,' steps')
                    s = input('Please select the number of steps again. Please make sure you select only between 1 and 6')
                    s=int(s)
                    while s<=s1:
                        if s==s1:
                            print('Choose another direction and steps')
                            return findDol3()
                        else:
                            print('wrong number, please enter ', s1, ' steps' )
                            s = input('Please select the number of steps again. Please make sure you select only between 1 and 6')
                            s=int(s)
                            continue
            else:
                s = input('out of range, please enter the steps only between 1 and 6')
                continue
    else:
        print('Wrong Dirction')
        findDol2()

def findDol1():
    d = input('Start moving by selecting the direction (L=Left, R=Right, B=Back, F=Forward). Please make sure you select only one direction at a time')
    s = input('Please select the number of steps. Please make sure you select only between 1 and 6')
    if d in ('F', 'f'):
        while s.lstrip('-').isdigit()==True:
            s=int(s)
            if s <=4:
                print('Right way!! You have taken ' , s , ' steps so far')
                if s==4:
                    print('Choose another direction and steps')
                    return findDol2()
                else:
                    s1=4-s
                    print('you are short by ', s1 ,' steps')
                    s = input('Please select the number of steps again. Please make sure you select only between 1 and 6')
                    s=int(s)
                    while s<=s1:
                        if s==s1:
                            print('Choose another direction and steps')
                            return findDol2()
                        else:
                            print('wrong number, please enter ', s1, ' steps' )
                            s = input('Please select the number of steps again. Please make sure you select only between 1 and 6')
                            s=int(s)
                            continue
            else:
                s = input('out of range, please enter the steps only between 1 and 6')
                continue
    else:
        print('Wrong Dirction')
        findDol1()


def findSil3():
    d = input('Start moving by selecting the direction (L=Left, R=Right, B=Back, F=Forward). Please make sure you select only one direction at a time')
    s = input('Please select the number of steps. Please make sure you select only between 1 and 6')
    if d in ('F', 'f'):
        while s.lstrip('-').isdigit()==True:
            s=int(s)
            if s <=4:
                print('Right way!! You have taken ' , s , ' steps so far')
                if s==4:
                    return print('Congratulations!! You have reached Silver filled room')
                else:
                    s1=4-s
                    print('you are short by ', s1 ,' steps')
                    s = input('Please select the number of steps again. Please make sure you select only between 1 and 6')
                    s=int(s)
                    while s<=s1:
                        if s==s1:
                            return print('Congratulations!! You have reached Dollars filled room')
                        else:
                            print('wrong number, please enter ', s1, ' steps' )
                            s = input('Please select the number of steps again. Please make sure you select only between 1 and 6')
                            s=int(s)
                            continue
            else:
                s = input('out of range, please enter the steps only between 1 and 6')
                s = input('Please select the number of steps again. Please make sure you select only between 1 and 6')
                s=int(s)
                continue
    else:
        print('Wrong Dirction')
        findSil3()
    #return print(x)

def findSil2():
    d = input('Start moving by selecting the direction (L=Left, R=Right, B=Back, F=Forward). Please make sure you select only one direction at a time')
    s = input('Please select the number of steps. Please make sure you select only between 1 and 6')
    if d in ('L', 'l'):
        while s.lstrip('-').isdigit()==True:
            s=int(s)
            if s <=6:
                print('Right way!! You have taken ' , s , ' steps so far')
                if s==6:
                    print('Choose another direction and steps')
                    return findSil3()
                else:
                    s1=6-s
                    print('you are short by ', s1 ,' steps')
                    s = input('Please select the number of steps again. Please make sure you select only between 1 and 6')
                    s=int(s)
                    while s<=s1:
                        if s==s1:
                            print('Choose another direction and steps')
                            return findSil3()
                        else:
                            print('wrong number, please enter ', s1, ' steps' )
                            s = input('Please select the number of steps again. Please make sure you select only between 1 and 6')
                            s=int(s)
                            continue
            else:
                s = input('out of range, please enter the steps only between 1 and 6')
                continue
    else:
        print('Wrong Dirction')
        findSil2()

def findSil1():
    d = input('Start moving by selecting the direction (L=Left, R=Right, B=Back, F=Forward). Please make sure you select only one direction at a time')
    s = input('Please select the number of steps. Please make sure you select only between 1 and 6')
    if d in ('F', 'f'):
        while s.lstrip('-').isdigit()==True:
            s=int(s)
            if s <=4:
                print('Right way!! You have taken ' , s , ' steps so far')
                if s==4:
                    print('Choose another direction and steps')
                    return findSil2()
                else:
                    s1=4-s
                    print('you are short by ', s1 ,' steps')
                    s = input('Please select the number of steps again. Please make sure you select only between 1 and 6')
                    s=int(s)
                    while s<=s1:
                        if s==s1:
                            print('Choose another direction and steps')
                            return findSil2()
                        else:
                            print('wrong number, please enter ', s1, ' steps' )
                            s = input('Please select the number of steps again. Please make sure you select only between 1 and 6')
                            s=int(s)
                            continue
            else:
                s = input('out of range, please enter the steps only between 1 and 6')
                continue
    else:
        print('Wrong Dirction')
        findSil1()


def findGol3():
    d = input('Start moving by selecting the direction (L=Left, R=Right, B=Back, F=Forward). Please make sure you select only one direction at a time')
    s = input('Please select the number of steps. Please make sure you select only between 1 and 6')
    if d in ('F', 'f'):
        while s.lstrip('-').isdigit()==True:
            s=int(s)
            if s <=4:
                print('Right way!! You have taken ' , s , ' steps so far')
                if s==4:
                    return print('Congratulations!! You have reached Dollars filled room')
                else:
                    s1=4-s
                    print('you are short by ', s1 ,' steps')
                    s = input('Please select the number of steps again. Please make sure you select only between 1 and 6')
                    s=int(s)
                    while s<=s1:
                        if s==s1:
                            return print('Congratulations!! You have reached Dollars filled room')
                        else:
                            print('wrong number, please enter ', s1, ' steps' )
                            s = input('Please select the number of steps again. Please make sure you select only between 1 and 6')
                            s=int(s)
                            continue
            else:
                s = input('out of range, please enter the steps only between 1 and 6')
                s = input('Please select the number of steps again. Please make sure you select only between 1 and 6')
                s=int(s)
                continue
    else:
        print('Wrong Dirction')
        findGol3()
    #return print(x)

def findGol2():
    d = input('Start moving by selecting the direction (L=Left, R=Right, B=Back, F=Forward). Please make sure you select only one direction at a time')
    s = input('Please select the number of steps. Please make sure you select only between 1 and 6')
    if d in ('L', 'l'):
        while s.lstrip('-').isdigit()==True:
            s=int(s)
            if s <=6:
                print('Right way!! You have taken ' , s , ' steps so far')
                if s==6:
                    print('Choose another direction and steps')
                    return findGol3()
                else:
                    s1=6-s
                    print('you are short by ', s1 ,' steps')
                    s = input('Please select the number of steps again. Please make sure you select only between 1 and 6')
                    s=int(s)
                    while s<=s1:
                        if s==s1:
                            print('Choose another direction and steps')
                            return findGol3()
                        else:
                            print('wrong number, please enter ', s1, ' steps' )
                            s = input('Please select the number of steps again. Please make sure you select only between 1 and 6')
                            s=int(s)
                            continue
            else:
                s = input('out of range, please enter the steps only between 1 and 6')
                continue
    else:
        print('Wrong Dirction')
        findGol2()

def findGol1():
    d = input('Start moving by selecting the direction (L=Left, R=Right, B=Back, F=Forward). Please make sure you select only one direction at a time')
    s = input('Please select the number of steps. Please make sure you select only between 1 and 6')
    if d in ('F', 'f'):
        while s.lstrip('-').isdigit()==True:
            s=int(s)
            if s <=4:
                print('Right way!! You have taken ' , s , ' steps so far')
                if s==4:
                    print('Choose another direction and steps')
                    return findGol2()
                else:
                    s1=4-s
                    print('you are short by ', s1 ,' steps')
                    s = input('Please select the number of steps again. Please make sure you select only between 1 and 6')
                    s=int(s)
                    while s<=s1:
                        if s==s1:
                            print('Choose another direction and steps')
                            return findGol2()
                        else:
                            print('wrong number, please enter ', s1, ' steps' )
                            s = input('Please select the number of steps again. Please make sure you select only between 1 and 6')
                            s=int(s)
                            continue
            else:
                s = input('out of range, please enter the steps only between 1 and 6')
                continue
    else:
        print('Wrong Dirction')
        findGol1()


x=input ("Do you like to go to Silver filled room then enter (S) OR Dollars filled room then enter (D) OR Gold filled room then enter (G)")
if x in ('d', 'D'):
    findDol1()
elif x in ('s', 'S'):
    findSil1()
elif x in ('g', 'G'):
    findGol1()
else:
    print('End of Program')
