def array_left_rotation( n, k, *a):
    b = a[0]
    r= []
    #print(len(b), n, k)
    if len(b) == n:
        #print(b)
        for i in range(len(b)):
            if i+k >= len(b):
                y = b[i+k-len(b)]
            else:
                y = b[i+k]
            r.append(y)
    else:
        print('value of n does not match with lenth of the array')
    return r


n, k = map(int, input('enter n, k:' ).strip().split(' '))
print(n,k)
a = list(map(int, input('enter array:').strip().split(' ')))
#print(a)
answer = array_left_rotation( n, k, a);
for i in range(len(answer)):
    print(answer[i], end =' ')
