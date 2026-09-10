#Global Freight Calculator 

sendername = input("whats your name? ")
itemtype = input("what kind of item? ") 
is_Fragile = bool(input("Is the item Frigile or not?(input true as yes, or press enter if not)? "))
if is_Fragile == true:
         print("handle it with care cuh, wrap it with some bubble wrap to protect the item")
else:
       print("handle it with care cuh, dont want the customer to get angry") 

weight = float(input("how heavy is the item (in kg)? "))
distance = float(input("how far is it to reach the item sa buyer (in km)? "))

#base cost
base_cost = weight * 2.50
base_cost2 = distance * 0.15
base_cost3 = base_cost + base_cost2

#total of international AND express 
total_int = base_cost3 * 1.40
total_int2 = total_int + 50

#total of express or international shipping
total_or = base_cost3 * 1.20
total_or2 = total_or + 25

#oversize > 30kg and > 1000km
total_os = base_cost3 + 30

#standard rate
total_sr = base_cost3

#free shipping 
free_ship = 0

is_express = bool(input("will it travel by express(input true as yes, or press enter if not)? "))
if is_express == true:
        print("got it pls proceed")

else:
      print("aight")

is_international = bool(input("will it travel by international shipping (input true as yes, or press enter if not)? "))
if is_express == true and is_international == true:
            print("the total shipping would amount to",total_int2)

elif is_express == true or is_international == true and weight > 20:
       print("the total shipping would amount to",total_or2)

elif weight > 30 or distance > 1000:
       print("the package is oversize. The total shipping would amount to",total_os)

elif weight <= 2.0 and distance <= 100 and is_express != true and is_international != true:
       print("the total shipping would amount to",free_ship)

else:
       print("the total shipping would amount to",base_cost3) #or total_sr
