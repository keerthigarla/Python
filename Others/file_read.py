a = input("Enter a number:")
num = int(a)
file = input("Enter a file name:")
with open(file, 'rt') as f:
	for i in range(0,num):
		line = f.readline()
		print(line)


