#init method for oop
class Coffee(object):

    attr1 = "Sweet"
    def __init__ (self, name,cost):
        self.name = name
        self.cost = cost
    def coffee_name(self):
        print("The name of the coffee is {}".format(self.name))
    def coffee_cost(self):
        print("The cost of the coffee is {}".format(self.cost))
    
    
#python inheritance. inheritance is the concept of using code from one class to another class. 
#you can use the 
class Milk(Coffee):
    def __init__(self,name,cost,coffee):
        self.name = name
        self.cost = cost
        self.coffee = coffee
        #this is where the inheritance occurs
        Coffee.__init__(self,name,cost)
    def coffee_details(self):
        print("Cost of coffee is {}".format(self.cost))

#python polymorphism. polymorphism means having many forms.  

latte = Coffee("Latte", 10)
capu = Coffee("Cappucino", 9)

print("The coffee name is {}".format(latte.name))
print("The coffee name is {}".format(capu.name))
latte.coffee_name()
capu.coffee_name()

kopio = Milk("kopi o", "10", "lattee")
kopio.coffee_details()
kopio.coffee_name()