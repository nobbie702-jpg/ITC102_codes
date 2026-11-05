from getpass import getpass

islogin = False

while islogin == False:
    username = input("input username ")
    password = input("input password ")

    if username == "user1" and password =="nobbie123":
        print ("access granted")
        islogin = True
    else:
        print("access denied")
