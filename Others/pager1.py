
file = input("Enter a file name:")
with open(file, 'rt') as f:
	n=0
	for line in f:
		n = n+1
	n=int(n)



with open(file, 'rt') as f:
	x= ''
	for i in range(1,3+round(n-3/3)):
		if i<=3:
			line = f.readline()
			print(line)
		elif x== 'End of File':
			break
		else:
			a=input('Enter any key to continue')
			for j in range(0,3):
				try:
					print(next(f))
				except StopIteration:
					print("End of File")
					x= 'End of File'
					break
