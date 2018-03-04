class CreditCard:
    #def setdata(self, credit_num):
    def __init__(self, creditnum):
        self.credit_num = creditnum
        #self.credit_num = "the card number"
        self.card_type = self.card_type()
        self.valid = self.valid()
        #self.check_length = self.check_length()

    #def display(self):
    #    print(self.credit_num)

    def card_type(self):
        str = self.credit_num
        if str.startswith('4'):
            return 'VISA'
        elif str[0:2] in ('51','52', '53', '54', '55'):
            return 'MASTERCARD'
        elif  str[0:2] in ('34','37'):
            return 'AMEX'
        elif str.startswith('6011'):
            return 'DISCOVER'
        else:
            return 'INVALID'
        #pass
        #return print(self.card_type)

    def check_length(self):
        if self.card_type  == 'VISA' or self.card_type == 'MASTERCARD' or self.card_type == 'DISCOVER':
            if len(self.credit_num) == 16:
                return True
            else:
                self.card_type = 'INVALID'
                return False
        elif self.card_type =='AMEX':
            if len(self.credit_num) == 15:
                return True
            else:
                #self.card_type = 'INVALID'
                return False
        else:
            return False
        #pass


    def valid(self):
        y = self.check_length()
        if y == True:
            str = self.credit_num[::-1]
            s1=0
            s2=0
            for i in range(0, len(str), 2):
                s1 = int(str[i]) + s1
                #print(s1)
            for i in range(1, len(str), 2):
                a = int(str[i])*2
                if a > 9:
                    a1 = a-9
                else:
                    a1 = a
                s2 = a1 + s2
            if (s1+s2)%10 ==0:
                return True
            else:
                #self.card_type = 'Invalid'
                return False
        else:
            #self.check_type = 'Invalid'
            return False
        #pass








#cc = CreditCard('379179199857686')
#cc.valid() == True
#cc.credit_num
#cc.setdata('379179199857686')
#cc.display()

#cc.card_type()

cc = CreditCard('339179199857685')
assert cc.valid == False, "Validates mod10, but invalid starting numbers for AMEX"
assert cc.card_type == "INVALID", "card_type is INVALID"
    # many more statements like this

    #exit(1)

cc = CreditCard('4929896355493470')
assert cc.valid == True, "Visa Card is Valid"
assert cc.card_type == "VISA", "card_type is VISA"
    # many more statements like this
