#Testing script for bicycle project
import bicycle as bk
from random import randint

bike1 = bk.Bike("Trek Silque", 30, 200)
bike2 = bk.Bike("Surly Long Haul Trucker", 50, 700)
bike3 = bk.Bike("Schwinn Fastback", 15, 300)
bike4 = bk.Bike("Huffy Highland", 20, 50)
bike5 = bk.Bike("Diamondback Overdrive", 30, 450)
bike6 = bk.Bike("Shimano Deore", 25, 125)
bikelist = [bike1,bike2,bike3,bike4,bike5,bike6]

#Set up Shop
shop = bk.BikeShop("Ridin' Dirty")
for bike in bikelist:
    for i in xrange(randint(1,5)): #add a random number of bikes to inventory, 1 to 5
        shop.add_bike(bike)
    shop.add_price(bike)

cust1 = bk.Customer("Daenerys", 200)
cust2 = bk.Customer("Renly", 500)
cust3 = bk.Customer("Tyrion", 1000)

#Check prices
cust1.find_available(shop)
cust2.find_available(shop)
cust3.find_available(shop)

#Initial inventory and profit
shop.status()

#Sell bikes
cust1.buy_bike(shop, bike4)
cust2.buy_bike(shop, bike3)
cust3.buy_bike(shop, bike2)

#New inventory and profit
shop.status()
