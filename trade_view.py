import model as model
import wrapper as contr

def main():
    model.create_table()
    print('Welcome to Share Market, Login/Signin in to your Account')
    # username = input('Enter Username: ' )
    # password = input('Enter Password: ' )
    #model.User_Reg(username, password)
    username = model.User_Login()
    if username =='admin':
        input("Hit any key to see the Top 10 Users.")
        model.Admin(username)
    else:
        print('Please select from below menu')
        print('a. Search for a Company'  )
        print('b. Get a quote')
        print('c. Buy Shares')
        print('d. Sell Shares')
        print('e. Earnings')
        print('f. Shares List')
        print('g. Exit')

        i=1
        while i>0:
            ch= input("Enter the menu item as a, b, c, d, e, f, g: ")
            cl = contr.Markit()
            if ch== 'a':
                symbol = input('To start the trade, please enter the name of the company. (For example AAPL for APPLE or A for All stocks that starts with A ): ')
                k, v = cl.company_search(symbol)
                model.Lookup(k,v)
            elif ch== 'b':
                #symbol = input('Enter the exact symbol of the company from above list:')
                k,v = cl.quote()
                model.Quote(k, v)
            elif ch== 'c':
                #symbol = input('Enter the exact symbol of the company from above list.')
                model.Shares_Buy(username, symbol)
            elif ch=='d':
                #symbol = input('Enter the exact symbol of the company from above list.')
                model.Shares_Sell(username, symbol)
            elif ch=='e':
                model.Earnings(username)
            elif ch=='f':
                model.SharesList(username)
            else:
                break
            i=i+1
main()
