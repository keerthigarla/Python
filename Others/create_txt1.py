
for i in range(1,5):
	menu = input("Choose one option:  'A for create file', 'B for display file' , 'C for save file', 'D for quit'")
	if menu == 'A':
		filename  = input("enter a file name:")
		#line = input("number of lines:")
		with open(filename,'xt')  as f:
			f.write('Hello Byte')
			f.write('\n'+'Hello Byte Cohort 6')
			print (filename, "file is created")
		continue
	elif menu == 'B':
		with open(filename,'rt')  as f1:
			print(f1.read())
		continue
	elif menu == 'C':
		print(filename, "file is saved")
		continue
	else:
		break
print('End of the Menu')
