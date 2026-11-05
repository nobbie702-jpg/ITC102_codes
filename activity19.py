isExpenive = True #boolen
while isExpenive == True:
    x = bool(input("is the gas price still expensive ? (True/False)"))

    if x == True:
        print("continuing loop")
        continue

    if x == False:
        print("break")
        break