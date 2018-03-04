#PATH=$PATH:/home/keerthi/Downloads
# always run above in terminal to instll webdriver before executing below code.
#import org.openqa.selenium.By
import requests
import os
import time
import re
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Firefox, FirefoxProfile
import csv




url = "http://www.boxofficemojo.com/studio/"
driver = webdriver.Firefox()

# Selenium driver inititalization
driver.wait = WebDriverWait(driver, 5)

def looping_pages():
	for i in range(2017,2015, -1):
		driver.get(url)
		if i== 2017:
			button = driver.find_element_by_link_text(str(i))
		else:
			button = driver.find_element_by_link_text(str(i)).click()
		#for i in range(1, 100):
		lst1=[]
		row = driver.find_elements_by_xpath("//table[@cellpadding='5']/tbody/tr")
		#rowc = len(row)
		col = driver.find_elements_by_xpath("//table[@cellpadding='5']/tbody/tr[1]/td")
		#colc = len(col)
		for i in range(1, len(row)+1):
			for j in range(1,len(col)+1):
				final_path = "//table[@cellpadding='5']/tbody/tr[" + str(i) + "]/td[" + str(j) + "]"
				link = driver.find_element_by_xpath(final_path)
				words = re.findall('\w+', link.text)
				lst1.append(link.text.replace('\n', ''))

		#print(lst1)
		lst2= [lst1[x:x+6] for x in range(0, len(lst1),6)]
		print(lst2)
		x=len(lst2)
		#print(tabulate(lst2[1: x+1], headers = lst2[0]))
		result = lst2[1: x+1]

		with open('Box_office_sel1.csv', 'a+') as csvfile:
			writer = csv.writer(csvfile)
			#delimiter= ' ')
			# for i in range
			for i in lst2:
				writer.writerow(i)
			writer.writerow(" ")
	#	print(words)
		#data = link.text
	#	list_.append(data)
		time.sleep(5)
looping_pages()
#print(list)
