#Definition of classes

class Wheel(object):
    def __init__(self,model, weight, expense):
        self.model = model
        self.weight = weight
        self.expense = expense

class Frame(object):
    def __init__(self, material):
        if material[0].lower() in ["a","c","s"]:
            self.material = material[0].lower()
        else:
            print "A frame must be aluminum (a), carbon (c) or steel (s)"
            return
        if self.material == 'a':
            self.weight = 30
            self.expense = 75
        elif self.material == 's':
            self.weight = 20
            self.expense = 200
        else: #material is 'c', carbon
            self.weight = 10
            self.expense = 500

class BikeManufacturer(object):
    def __init__(self, name, markup):
        self.name = name
        self.markup = markup
    def add_model(self, model, wheel, frame):
        bike = Bike(model,wheel,frame,self.name)
        bike.expense += bike.expense * self.markup # add in the manuf's cut
        return bike

class Bike(object):
    def __init__(self, model, wheel, frame, manufacturer):
        self.model = manufacturer + " " + model
        self.wheel = wheel
        self.frame = frame
        self.manufacturer = manufacturer
        self.weight = 2 * wheel.weight + frame.weight
        self.expense = 2 * wheel.expense + frame.expense

class BikeShop(object):
    markup = 0.2
    def __init__(self, name):
        self.name = name
        self.inventory = {}
        self.pricelist = {}
        self.bankaccount = 0
    def add_bike(self, bike):
        self.bankaccount -= bike.expense
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
            self.bankaccount += self.pricelist[bike.model]
    def status(self):
        print self.name + " has the following inventory:\n"
        for model in self.inventory:
            print model + ": " + str(self.inventory[model])
        print "\n" + self.name + " has made $" + "{:.2f}".format(self.bankaccount) + " today."
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
