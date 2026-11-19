people = ["jack", "coal", "lynn", "mmo", "akoo"]

gender = {"a guy":"male", "guy likes guy":"gay", "a girl":"female", "a girl likes girl":"lesbian", "changing private part":"transgender"}

print(people[4])

print(gender["changing private part"])


for x, y in gender.items():
    print("key is ",x," -- value is ", y)