age = int(input("enter your age ----> "))
is_employed = bool(input("are you currently employed? ---> "))
credit_score = float(input("credit score --> "))
annual_income = float(input("what is yout annual salary? ---> "))
has_collateral = bool(input( "do you have any collateral (true / false ) ---> "))

base_rate = 0.0


if age >=21 and is_employed == True:
        print("accepted")
        if credit_score >=750:
                print("you have a high credit score") 
                if annual_income >= 100000:
                        base_rate = 4.5
                        print(" your base rate is ", base_rate)
                else:
                        base_rate = 5.0
                        print ("your base rate is", base_rate)
    elif credit_score >= 600 and credit_score < 750:
        print("your credit score is less than 750")
        if has_collateral == True:
                print("you have a collateral")
                base_rate = 7.0
                print("your base rate is", base_rate)
        elif annual_income <= 40000:
                print("low annual income")
                base_rate = 9.0
                print("your base rate is", base_rate)
        else:
                base_rate = 8.0
                print("your base rate is", base_rate)
                elif credit_score <= 600:
print ("rejected: credict score too low")


else: 
        print("rejected")