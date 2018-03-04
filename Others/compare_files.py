file1 = input('enter a file name1:')
file2=  input('enter a file name3:')
with open(file1,'rt')  as f1:
	l1=[]
	for line in f1:
		line.split()
		for word in line.split():
			l1.append(word)
#	print(l1)
with open(file2,'rt')  as f2:
	l2=[]
	for line in f2:
		line.split()
		for word in line.split():
			l2.append(word)
#	print(l2)
for i in range(0, len(l1)):
	if l1[i] in l2:
		x='same files'
	else:
		x='different files'
	print(x)
