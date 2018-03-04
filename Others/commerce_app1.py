#Project 1: Electronic Commerce Application.

#You need to create the foundations of an e-commerce engine for a B2C (business-to-consumer) retailer.
#You need to have a class for a customer called User, a class for items in inventory called Item, and a shopping cart class called Cart. Items go in Carts,
#and Users can have multiple Carts. Also, multiple items can go into Carts, including more than one of any single item.
#from collections import defaulted

from collections import defaultdict
class Item():
    def __init__(self,itemname, price, quantity):
        self.itemname = itemname
        self.price = price
        self.quantity = quantity
    def display(self):
        print(self.itemname, self.price, self.quantity)

class Cart(Item):
    def __init__(self,items):
        self.items = items
        self.cart = defaultdict(list)


    def Add_Items(self):
        for i in range(0,len(self.items)):
           #print(self.items[i].itemname, self.items[i].price)
           key1 = self.cart[self.items[i].itemname]
           key1.append(self.items[i].price)
           key1.append(self.items[i].quantity)
        for k, v in self.cart.items():
            print(k, v)
            #print(self.cart[self.items[i].itemname][0])

    def Remove_Items(self, itemname):
        for key, value in self.cart.items():
            #print(key)
            #print(self.cart[key][1])
            if key == itemname:
                if self.cart[key][1] > 1:
                     self.cart[key][1] = self.cart[key][1]-1
                else:
                     del self.cart[key]
        print('Your cart has below items')
        for k, v in self.cart.items():
            print(k, v)

class User(Cart):
    def __init__(self,carts = None):
        self.carts = carts
        #super.__init__(carts)
        if self.carts == None:
            self.carts = []
        else:
            self.carts = carts
        self.user = defaultdict(list)

    def Add_carts(self):
        for i in range(0, len(self.carts)):
            key1 = self.user[i]
            key1.append(self.carts[i].cart)

                # key1.append(self.carts[i])
        for k, v in self.user.items():
            print(k, v)
            #print(self.cart[self.items[i].itemname][0])

    def Remove_carts(self, cart):
        for key, value in self.user.items():
            #print(key)
            #print(self.cart[key][1])
            if key == cart:
                del self.user[key]

        for k, v in self.user.items():
            print(k, v)


a1 = Item('Apple', 90, 2)
b1= Item('Orange', 80, 2)
ListItems = [a1,b1]
c1 = Cart(ListItems)
c1.Add_Items()
c1.Remove_Items('Apple')

a2 = Item('Book', 100, 2)
b2 = Item('Pencil', 50, 2)
ListItems = [a2,b2]
c2 = Cart(ListItems)
c2.Add_Items()
c2.Remove_Items('Pencil')

c= [c1]
print(c)
u1 = User(c)
u1.Add_carts()


u2 = User(c2)
u2.Add_carts()
