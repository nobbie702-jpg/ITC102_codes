anime_type = ["isekai","fantasy","yaoi","yuri"]
anime_title = []

while True:
    ans = input("you watch anime? -->    (yes / no)")
    if ans.lower() == "yes":
        print("whats the genre? --> select from the list ")
        for x in anime_type:
            print (x)


        a_type = input("type -->  ")

        title = input("what is the tittle of the anime -->  ")
        anime_title.append(title)
        continue
    else:
        print("thanks")
        print("so far you have encoded the following")
        for x in anime_title:
            print (x)
        break   



    