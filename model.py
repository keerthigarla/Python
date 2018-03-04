#Manages 5 tables
# Users : Dimension table which captures Id, Username, password
# Stocks : Dimension table which sources Id, name, symbol, price, asofdate from 'Quote' and 'Lookup' tables for the companies which user has searched or traded.
# Users_Shares : Fact table which captures user transactions
# Quote: Source table for company Quote data
# Lookup: Source and Lookup table for companies

from requests import get
import json,csv
import sqlite3
from tabulate import tabulate
import datetime
import time
#create empty tables: Users, Stocks, Users_Shares
def create_table():
    conn = sqlite3.connect('sh_market1.db')
    cur = conn.cursor()
    today = datetime.date.today()
    cur.execute('''CREATE TABLE IF NOT EXISTS Users(Id INTEGER PRIMARY KEY, username TEXT NOT NULL, password TEXT NOT NULL)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS Stocks(Id INTEGER PRIMARY KEY, name TEXT NOT NULL, symbol TEXT NOT NULL, price INTEGER NOT NULL, asofdate DateTime)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS Users_Shares(Id INTEGER PRIMARY KEY, username TEXT NOT NULL, symbol , asofdate, shares, Buy_Sell, funds_avail INTEGER NOT NULL )''')
    conn.commit()

# User Registration
def User_Reg(username, password):
    input('New customer!! To register hit any key:')
    conn = sqlite3.connect('sh_market1.db')
    cur = conn.cursor()
    today = datetime.date.today()
    #username  and password checking
    cur.execute('''SELECT username, password FROM Users''')
    lstu=[]
    lstp=[]
    for row in cur.fetchall():
        lstu.append(row[0])
        lstp.append(row[1])
    if username in lstu:
        print('Username already exists, please choose a different username')
        User_Login()
    else:
        cur.execute("INSERT INTO Users (username,password) VALUES (?,?)", (username,password))
        cur.execute("INSERT INTO Users_Shares(username,asofdate, shares, funds_avail) VALUES (?,?, ?,?)", (username, today, 0, 100000 ))
        conn.commit()
        print('Registered successfully. Please login back again later')
        User_Login()
        #exit()
    conn.commit()
    conn.close()


# User Login
def User_Login():
    username = input('Enter Username: ' )
    password = input('Enter Password: ' )
    conn=sqlite3.connect('sh_market1.db')
    cur = conn.cursor()
    #username  and password checking
    cur.execute('''SELECT username, password FROM Users''')
    lstu=[]
    lstp=[]
    for row in cur.fetchall():
        lstu.append(row[0])
        lstp.append(row[1])

    if username in lstu and password in lstp:
        print('Logged in successfully')
        return username
    else:
        User_Reg(username, password)
    conn.commit()
    conn.close()

#Quote Source table creation and data loading
def Quote(ke,va):
    conn=sqlite3.connect('sh_market1.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Quote(Id INTEGER PRIMARY KEY , {},{},{},{},{},{},{},{},{},{},{},{},{},{},{})". format(ke[0][0],ke[0][1],ke[0][2],ke[0][3],ke[0][4],ke[0][5],ke[0][6],ke[0][7],ke[0][8],ke[0][9],ke[0][10],ke[0][11],ke[0][12],ke[0][13],ke[0][14]) )
    for i in range(len(ke)):
    	if( "'" in str(va[i][1])):
    		va[i][1] = va[i][1].replace("'","")
    	cur.execute("INSERT INTO Quote ({},{},{},{},{},{},{},{},{},{},{},{},{},{},{}) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');".format(ke[i][0],ke[i][1],ke[i][2],ke[i][3],ke[i][4],ke[i][5],ke[i][6],ke[i][7],ke[i][8],ke[i][9],ke[i][10],ke[i][11],ke[i][12],ke[i][13],ke[i][14], va[i][0],va[i][1],va[i][2],va[i][3],va[i][4],va[i][5],va[i][6],va[i][7],va[i][8],va[i][9],va[i][10],va[i][11],va[i][12],va[i][13],va[i][14]))
    conn.commit()

#Company Source table creation and data loading
def Lookup(ke,va):
    conn = sqlite3.connect('sh_market1.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS Lookup(Id INTEGER PRIMARY KEY , {} , {} , {});'.format(ke[0],ke[1],ke[2]) )
    for i in range(len(va)):
    	if( "'" in str(va[i][1])):
    		va[i][1] = va[i][1].replace("'","")
        #time.sleep(3)
    	cur.execute("INSERT INTO Lookup ({},{},{}) VALUES('{}','{}','{}');".format(ke[0],ke[1],ke[2],va[i][0],va[i][1],va[i][2]))

    conn.commit()
    conn.close()

# Inserting stocks searched by user to buy in Stocks table; and stocks bought by each user in Users_Shares, and changing funds_avail baseed on stocks bought.
def Shares_Buy(username, symbol):
    shares = int(input("Enter number of shares to buy: "))
    conn=sqlite3.connect('sh_market1.db')
    cur = conn.cursor()
    symbol = symbol.upper()
    c1 = cur.execute("SELECT  l.Name, l.Symbol, q.LastPrice, q.Timestamp from Lookup as l, Quote  as q where l.Symbol = q.Symbol and  l.Symbol = ?" , (symbol,))
    #print(cur.fetchall())
    na=[]
    sym=[]
    lp=[]
    d1=[]
    for row in c1.fetchall():
        #print(row[0])
        na.append(row[0])
        sym.append(row[1])
        lp.append(row[2])
        d1.append(row[3])
    cur.execute("INSERT INTO Stocks(name , symbol , price , asofdate ) VALUES  (?,?, ?,?)", (na[len(na)-1], sym[len(sym)-1], lp[len(lp)-1], d1[len(d1)-1] ))
    conn.commit()
    #print(username)
    c2 = cur.execute("SELECT funds_avail from Users_Shares where username = ?", (username,) )
    f=[]
    for row in c2.fetchall():
        #print(row[0])
        f.append(row[0])
    print('Funds Available: ',f[len(f)-1])
    print('Price per share: ', lp[len(lp)-1])

    # try:
    #     f1 = f[len(f)-1]
    # except IndexError:
    #
    funds = int(f[len(f)-1]) - (float(lp[len(lp)-1]) * shares)
    print('Funds Remaining: ',funds)
    if funds < 0:
        print('You have exceeded your available funds. Pleease choose lesser shares')
        Shares_Buy()
    else:
        cur.execute("INSERT INTO Users_Shares(username ,symbol, asofdate, shares, Buy_Sell, funds_avail ) VALUES  (?,?,?,?,?,?)", (username, symbol, d1[len(d1)-1], shares, 'Buy', funds ))
    conn.commit()
    conn.close()

# Inserting stocks searched by user to sell in Stocks table; and stocks sold by each user in Users_Shares, and changing funds_avail baseed on stocks sold.
def Shares_Sell(username, symbol):
    shares = int(input("Enter number of shares to sell: "))
    conn=sqlite3.connect('sh_market1.db')
    cur = conn.cursor()
    symbol = symbol.upper()
    c1 = cur.execute("SELECT  l.Symbol, l.Name, q.LastPrice, q.Timestamp from Lookup as l, Quote  as q where l.Symbol = q.Symbol and  l.Symbol = ? " , (symbol,))
    na=[]
    sym=[]
    lp=[]
    d1=[]
    for row1 in c1.fetchall():
        na.append(row1[0])
        sym.append(row1[1])
        lp.append(row1[2])
        d1.append(row1[3])
    cur.execute("INSERT INTO Stocks(name , symbol , price , asofdate ) VALUES  (?,?, ?,?)", (na[len(na)-1], sym[len(sym)-1], lp[len(lp)-1], d1[len(d1)-1] ))
    conn.commit()

    c2 = cur.execute("SELECT funds_avail from Users_Shares where username = ? ", (username,) )
    f=[]
    for row2 in c2.fetchall():
        f.append(row2[0])

    c3 = cur.execute("SELECT shares from Users_Shares where username = ? and symbol = ?", (username,symbol) )
    sha =[]
    for row2 in c3.fetchall():
        sha.append(row2[0])
    if shares > sum(sha):
        print('Number of shares selected is greater than outstanding shares')
        Shares_Sell()
    else:
        funds = int(f[len(f)-1]) + (float(lp[len(lp)-1]) * shares)
        shares = -shares
        cur.execute("INSERT INTO Users_Shares(username ,symbol, asofdate, shares, Buy_Sell, funds_avail ) VALUES  (?,?,?,?,?,?)", (username, symbol, d1[len(d1)-1], shares, 'Sell', funds ))
    conn.commit()
    conn.close()

#Display outstanding Earnings.
def Earnings(username):
    conn=sqlite3.connect('sh_market1.db')
    cur = conn.cursor()
    c1 = cur.execute("SELECT funds_avail FROM Users_Shares WHERE Id = (SELECT max(Id) from Users_Shares where username =?  group by username)", (username,))
    f=[]
    for row in c1.fetchall():
        f.append(row[0])
    Earnings = f[len(f)-1] - 100000
    c3 = cur.execute("SELECT sum(shares) FROM  Users_Shares where username =? ", (username, ))
    sha=[]
    for row in c3.fetchall():
        sha.append(row[0])
    Outstanding_Shares = sha[0]
    lstf = [username, Earnings, Outstanding_Shares]
    return print('User:', username,'  Earnings:', Earnings, '  Outstanding Shares:',Outstanding_Shares )
    #return print(tabulate(lstf, headers = ['User', 'Earnings', 'Outstanding Shares']) )
    conn.close()



#Display list of shares per user.
def SharesList(username):
    conn=sqlite3.connect('sh_market1.db')
    cur = conn.cursor()
    c1 = cur.execute("SELECT u.Id, u.username, u.symbol, u.asofdate, u.shares, u.Buy_Sell, u.funds_avail, q2.price FROM Users_Shares as u LEFT OUTER JOIN (select q1.Symbol as Symbol, q1.LastPrice as price from Quote as q1, (select Symbol, max(Id) as Id from Quote group by Symbol) as b where q1.Id = b.Id and q1.Symbol = b.Symbol)as q2 on u.Symbol = q2.Symbol WHERE u.username = ? order by u.Id", (username,))
    data = c1.fetchall()
    #return print(data)
    return print(tabulate(data, headers = ['Id', 'Username', 'Symbol' , 'Asofdate', 'Shares', 'Buy_Sell', 'Funds_avail', 'SharePrice']))
    conn.close()

#Display Top 10 Users based on their earnings to Admin.
def Admin(username):
    conn=sqlite3.connect('sh_market1.db')
    cur = conn.cursor()
    admin = username
    query = '''SELECT username,Earnings,rank1  from
    (SELECT u.Id as Id, u.username as username, (funds_avail-100000) as Earnings, (select count(*) from
    (SELECT uu.funds_avail as funds_avail, uu.Id as Id from Users_Shares as uu, (SELECT username, max(Id) as Id from Users_Shares where username != ? group by username) as b1  where b1.username = uu.username and b1.username !=? and b1.Id = uu.Id) as b  where b.funds_avail >= u.funds_avail) as rank1 from Users_Shares as u ,
    (SELECT username as username , max(Id) as Id from Users_Shares where username != ? group by username) as i
    where  u.username = i.username and u.Id = i.Id
    ) where rank1 <=10 and rank1 > 0 order by rank1'''
    c1 = cur.execute(str(query), (admin, admin, admin))
    data = c1.fetchall()
    return print(tabulate(data, headers = [ 'Username',  'Earnings', 'Rank']))
    #return print(data)
    conn.close()
