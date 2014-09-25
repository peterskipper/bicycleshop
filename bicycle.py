#Definition of classes

class Bike(object):
    def __init__(self, model, weight, expense):
        self.model = model
        self.weight = weight
        self.expense = expense
    def stats(self):
        return (self.model,self.weight,self.expense)

class BikeShop(object):
    markup = 0.2
    def __init__(self, name):
        self.name = name
        self.inventory = {}
        self.pricelist = {}
        self.profit = 0
    def add_bike(self, bike):
        if bike.model in self.inventory:
            self.inventory[bike.model] += 1
        else:
            self.inventory[bike.model] = 1
    def add_price(self, bike):
        self.pricelist[bike.model] = bike.expense + self.markup * bike.expense
    def sell_bike(self, bike):
        if self.inventory[bike.model] < 1:
            print "You have no more in stock!"
            return
        else:
            self.inventory[bike.model] -= 1
            self.profit += self.markup * bike.expense
    def status(self):
        print self.name + " has the following inventory:\n"
        for model in self.inventory:
            print model + ": " + str(self.inventory[model])
        print "\n" + self.name + " has made $" + "{:.2f}".format(self.profit) + " today."
        print #get a new line
class Customer(object):
    def __init__(self, name, fund):
        self.name = name
        self.fund = fund
    def find_available(self, bikeshop):
        print self.name + " has $" + "{:.2f}".format(self.fund) + " and can afford the following bikes at " + bikeshop.name +":\n"
        for model, price in bikeshop.pricelist.iteritems():
            if price <= self.fund:
                print model + ": $" + "{:.2f}".format(price)
        print #get a new line
    def buy_bike(self, bikeshop, bike):
        if self.fund >= bikeshop.pricelist[bike.model]:
            self.fund -= bikeshop.pricelist[bike.model]
            bikeshop.sell_bike(bike)
            print self.name + " purchased a " + bike.model + " for $" + "{:.2f}".format(bikeshop.pricelist[bike.model])
            print self.name + " now has $" + "{:.2f}".format(self.fund) + " left."
            print #get a new line
