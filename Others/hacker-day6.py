n = int(input("Enter"))
for i in range(n):
    str1 = input("Enter string")

    for i in range(0, len(str1), 2):
        x=print(str1[i], end= '')
    print(' ', end='')
    for i in range(1, len(str1), 2):
        y = print(str1[i], end= '')
    print(' ')
