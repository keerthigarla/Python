import requests
import tabulate
from bs4 import BeautifulSoup
from tabulate import tabulate
import csv
#import pandas as pd
import numpy as np


lst=[]
for i in range(2017, 1999, -1):
	source_url = 'http://www.boxofficemojo.com/studio/?view=company&view2=yearly&yr=' + str(i) + '&p=.htm'
	lst.append(source_url)

for i in range(0, len(lst)):
	print('/n')
	print( '****************BOX OFFICE YEAR', 2017-i,' **************************' )
	print('/n')
	source_url = lst[i]
	# target url =
	r = requests.get(source_url)
	content = r.content
	#	print(content)
	soup = BeautifulSoup(content, "html.parser")
	#print(soup.prettify())
	#print(soup)
	right_table = soup.find('table', cellpadding ='2')
	# for link in right_table.find_all('a'):
	# 	print(link.text)
	final_table = right_table.find('table',  cellpadding ='5')
	lst1=[]
	for fon in final_table.find_all('font'):
		lst1.append(fon.text)
		#print(fon.text)
	#print(lst1)
	year = str(2017-i)
	lst2= [lst1[x:x+6] for x in range(0, len(lst1),6)]
	#print(lst2)
	x=len(lst2)
	print(tabulate(lst2[1: x+1], headers = lst2[0]))
	result = lst2[1: x+1]

	with open('Box_office_bs4v1.csv', 'a+') as csvfile:
		writer = csv.writer(csvfile)
		#delimiter= ' ')
		# for i in range
		for i in lst2:
			writer.writerow(i)
		writer.writerow(" ")
	#writer.writerow(lst2[i][1] for i in range(0, len(lst2)) )
	#writer.writerow(lst2)




	#print(result)
	# r1 = np.array(lst2)
	# df = pd.DataFrame(r1)
	# df.to_csv('file_path.csv')
# def collect_links():
#
# 	for link in soup.findAll('a'):
#
# 		links.append((link.get('href')))
#
# 	remove_none = [x for x in links if x is not None]
#
# 	proper_links = [link for link in remove_none if "lecture" in link]
#
# 	full_links = [base_url + link for link in proper_links]
#
# 	return(full_links)
#
#
#
# def write_to_csv():
#
	# with open('Box_office_bs4.csv', 'w') as csvfile:
    #
	# 	#fieldnames = ['links']
    #
	# 	writer = csv.writer(csvfile)
    #
	# 	#writer.writerow(fieldnames)# writing "links" in column header
	# 	a=0
	# 	for i in Extract_Data():
    #
	# 		writer.writerow(2017-a, i[0], i[1], i[2], i[3], i[4], i[5] )
	# 		a=a+1
#
#
#
# write_to_csv()
# #Extract_Data()
