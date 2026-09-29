age = int(input("age ----> "))
rev = float(input("revenue ----> "))
cc = int(input("creadit score ----> ")) 
yrs = float(input("years of business ----> "))
has_default = bool(input("file for bankruptcy ----->"))
collateral = input("collateral name ----->")
c_value = float(input("collateral value"))


max_loan = 0
base_fee = 0

if age >= 21 and has_default == False and yrs >= 2.0:
    print("baseline passed")
    if cc >= 702:
        print("credit score considered high ")
        max_loan = rev * 3
        if rev >= 50000:
            print ("above 50k revenue")
            base_fee = max_loan * 0.015
            print ("base fee is set to ", base_fee)
        else:
            print("renvenue below 50k")
            base_fee = max_loan * 0.025
            print("base fee is set to",base_fee)


elif cc <= 620 and cc < 720:
    print ("credit score within range of 620 to 720")
    max_loan = rev * 1.5
    if yrs >= 5.0:
        base_fee = max_loan * 0.02
        print ("years in business greater than 5 years base fee is ",base_fee)
    else:
        base_fee = max_loan = 0.035
        print ("years in business lower than 5 years base fee is",base_fee)


elif cc <620:
    print ("credit score too low")
else:
    print("invalid")


