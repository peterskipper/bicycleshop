#Definition of classes

class Bike(object):
    def __init__(self, model, weight, expense):
        self.model = model
        self.weight = weight
        self.expense = expense
    def stats(self):
        return (bike.model,bike.weight,bike.expense)

class BikeShop(object):
    markup = 0.2
    def __init__(self, name):
        self.name = name
        self.inventory = {}
        self.profit = 0
    def add_bike(self, bike):
        self.inventory[bike.model] += 1
    def sell_bike(self, bike):
        if self.inventory[bike.model] < 1:
            print "You have no more in stock!"
            return
        else:
            self.inventory[bike.model] -= 1
            self.profit += markup * bike.expense
    def status(self):
        print self.name + " has the following inventory:\n"
        for model in self.inventory:
            print model + ": " + str(self.inventory[model])
        print "\n" + self.name + "has made $" + str(self.profit) + " today."

class Customer(object):
    def __init__(self, name, fund):
        self.name = name
        self.fund = fund
    
