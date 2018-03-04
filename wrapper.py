from requests import get
import json,csv
import sqlite3
from tabulate import tabulate
import datetime
import time


class Markit:
	def __init__(self):
		self.lookup_url = "http://dev.markitondemand.com/Api/v2/Lookup/json"
		self.quote_url = "http://dev.markitondemand.com/Api/v2/Quote/json"
	#Scraping company Lookup data
	def company_search(self,string):
		q={'input': string.upper()}
		s = self.lookup_url
		res = get(s,q) #print(res) #response
		r = res.json()
		#print(r[0])
		ke = list(r[0].keys())
		time.sleep(5)
		va=[list(r[i].values()) for i in range(len(r))]
		print(tabulate(va, headers = ke))
		#print(ke)
		#print(va)
		return (ke,va)
	pass
	#Scraping Quote data
	def quote(self):
		#,string):
		string = input('Enter the exact symbol of the company from above list:')

		conn = sqlite3.connect('sh_market1.db')
		curr = conn.cursor()
		curr.execute("SELECT Symbol FROM Lookup")
		lst=[]
		for row in curr.fetchall():
			lst.append(row[0])
		ke = []
		va = []
		if string.upper() in lst:
			q = {'symbol': string.upper() }
			s = self.quote_url
			res = get(s,q)
			rr = res.json()
			ke.append(list(rr.keys()))
			time.sleep(5)
			va.append(list(rr.values()))
			print(tabulate(va, headers = ke[0]))
		else:
			print('Symbol not valid')
			self.quote()
		return (ke,va)
