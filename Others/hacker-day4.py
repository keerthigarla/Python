class Person:
    def __init__(self,initialAge):
        if initialAge < 0:
            print('Age is not valid, setting age to 0')
            self.initialAge = 0
        else:
            self.initialAge = initialAge
    def amIOld(self):
        if self.initialAge < 13:
            print('You are young..')
        elif self.initialAge >= 13 and self.initialAge < 18:
            print('You are a teenager..')
        else:
            print('You are old..')
    def yearPasses(self):
        self.initialAge += 1


for i in range(0, 4):
    age = input('Enter the age: ')
    p = Person(int(age))
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")
