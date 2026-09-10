#Problem: Global Freight Calculator 

name = input("input NAME -----> ")
item = int(input("input WHAT TYPE OF ITEM -----> "))
is_fragile = bool(input("is it fragile? "))

#boolen
yes= true
no= false
 
print ("Got it" ,name, "we'll deliver it with care")

if is_fragile == yes:
   print(" Got it we'll deliver it with care")

elif is_fragile == no:
  print (" Got it ")