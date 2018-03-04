def isPrime(x):
    y=[]
    for i in range(1,x+1):
        if x%i == 0:
            y.append(i)
    print(y)
    for i in range(2,max(y)+1):
            if max(y)%i==0:
                x= False
            else:
                x= True
    yield x
print(next(isPrime(10)))
