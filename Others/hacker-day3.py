def number_needed(a1, b1):
    x = a1.lower().replace(' ', '')
    y = b1.lower().replace(' ', '')
    a=[]
    b=[]
    for i in x:
        a.append(i)
    for i in y:
        b.append(i)
    #print(a)
    #print(b)
    s1 = set(a)
    s2 = set(b)
    if  s1.intersection(s2) == s1:
        return 0
    else:
        return len(s1.union(s2)) - len(s1.intersection(s2))


a1 = input('enter').strip()
b1 = input('enter').strip()

print(number_needed(a1, b1))
