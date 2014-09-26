#Testing script for bicycle project
import bicycle as bk
from random import randint

#Create parts
wald = bk.Wheel("Wald",5,5)
avenir = bk.Wheel("Avenir", 3, 10)
sta_tru = bk.Wheel("Sta-Tru",1, 25)

alum = bk.Frame('a')
carb = bk.Frame('c')
steel = bk.Frame('s')

#Create Manufacturers
trek = bk.BikeManufacturer("Trek", 0.15)
huffy = bk.BikeManufacturer("Huffy", 0.05)

#Build Bikes

bike1 = trek.add_model("Silque",avenir,steel)
bike2 = trek.add_model("Lightning",sta_tru,carb)
bike3 = trek.add_model("Overland",wald,steel)
bike4 = huffy.add_model("Roadster",wald,alum)
bike5 = huffy.add_model("Uptown",avenir,alum)
bike6 = huffy.add_model("Moderno",sta_tru,steel)

bikelist = [bike1,bike2,bike3,bike4,bike5,bike6]

#Set up Shop
shop = bk.BikeShop("Ridin' Dirty")
for bike in bikelist:
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
cust2.buy_bike(shop, bike1)
cust3.buy_bike(shop, bike2)

#New inventory and profit
shop.status()
