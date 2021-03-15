import json
import datetime



time = list(datetime.datetime.now().strftime('%I:%M %p'))
print(time)
for i in time:
    current_time = i[0]+i[1]+i[3]+i[4]
    print(current_time)
    break

with open("data.json", "r") as file1:
    data = json.load(file1)
with open("loginfo.json", "r") as file:
    data5 = json.load(file)


liu = []
# print(data)
# print(data)


def addUser():
    """"Adds a user to the bot"""
    username = input("Set Username:\n")
    password = input("Set Password:\n")
    bal = 0
    for i in data:
        if i["username"] == username:
            return "User with username %s already exists" % username
    data.append({
        "username": username,
        "password": password,
        "bal": bal,
        "job":"none"
    })
    with open("data.json", "w") as edit:
        json.dump(data, edit)
    return "added user with name: %s, password: %s" % (username, password)


def removeUser(username, password):
    """Removes user from bot data"""

    for i,l  in data, data5:
        if i["username"] == l["username"]:
            del data[i]
            del data5[l]
            print("Removed User %s. Remaining users: %i" % (username, len(data)))



def validUser(username, password):
    """Checks if entered username and password are valid"""
    # print(data)
    for i in data:
        if i["username"] == username and i["password"] == password:
            return True
    return False



def login():
    while True:
        username = input("Enter Username:\n")
        password = input("Enter Password:\n")
        if validUser(username, password):
            # print("logged in as %s" % username)
            # return username, password
            data5.append({"username": username})
            print(data5)
            with open("loginfo.json", "w") as f:
                json.dump(data5, f)
            break
        else:
            print("User doesn't exist")
            newUSer = input("create new user? [Y/n]\n").lower()
            if newUSer == "y":
                print(addUser())

            else:
                print("Ok then. Try logging in again.")
 
def log():
        if data5 == []:
           login()
        else:
            name = data5[0]
            usr = name["username"]
            for i in data:
                if usr == i["username"]:
                    username = i["username"]
                    password = i["password"]
                    balance = i["bal"]           


def gamer():
    for i in data:
        for j in data5:
            if i["username"] == j["username"]: 
                ob = i["bal"]
                newbal = i["bal"] + 20000
                i["bal"] = newbal
                nb = i["bal"]
                print(f"you earned {nb - ob} now your balance is = {nb} ")

    with open("data.json", "w") as file1:
        json.dump(data, file1)

def programer():
    for i in data:
        for j in data5:
            if i["username"] == j["username"]: 
                ob = i["bal"]
                newbal = i["bal"] + 15000
                i["bal"] = newbal
                nb = i["bal"]
                print(f"you earned {nb - ob} now your balance is = {nb} ")

    with open("data.json", "w") as file1:
        json.dump(data, file1)

def cleaner():
    for i in data:
        for j in data5:
            if i["username"] == j["username"]: 
                ob = i["bal"]
                newbal = i["bal"] + 7000
                i["bal"] = newbal
                nb = i["bal"]
                print(f"you earned {nb - ob} now your balance is = {nb} ")

    with open("data.json", "w") as file1:
        json.dump(data, file1)
       

def painter():
    for i in data:
        for j in data5:
            if i["username"] == j["username"]: 
                ob = i["bal"]
                newbal = i["bal"] + 10000
                i["bal"] = newbal
                nb = i["bal"]
                print(f"you earned {nb - ob} now your balance is = {nb} ")

    with open("data.json", "w") as file1:
        json.dump(data, file1)

def select_job():
    print("please select a job from the options below:")
    print("-> Painter")
    print("-> programmer")
    print("-> gamer" )
    print("-> cleaner")
    useri = input()
    for i in data:
        if useri == "programmer":
            i["job"] = "programer"
            print("your new job is to program")
        elif useri == "gamer":
            i["job"] = "gamer"
            print("Your new job is to game")
        elif useri == "painter":
            i["job"] = "painter"  
            print("Your new job is to paint")
            
        elif useri == "cleaner":
            i["job"] = "cleaner"
            print("Your new job is to clean the bathroom!")

    with open("data.json", "w") as file1:
        json.dump(data, file1)


    
def work():


    for i in data:
        if i ["username"] == data5[0].get("username"):
            if i["job"] == "none":
                select_job()
            else:
                if i["job"] == "gamer":
                    gamer()
                elif i["job"] == "programer":
                    programer()
                elif i["job"] == "cleaner":
                    cleaner()
                elif i["job"] == "painter":
                    painter()
def balance():
    for i in data:
        if i["username"] == data5[0]["username"]:
            balanceofuser = i["bal"]
            print(f"your balance is {balanceofuser}")
def logout():
   
    with open("loginfo.json", "w") as file3:
        json.dump([], file3)


def shop():
    items = {"padlock":10000, "gaming laptop":20000, "rare coin":20000000000, "level up":"" }

def main():
    log()
    while True:
        command = input(">")
        if command == "work":
            work()
        elif command == "logout":
            logout()
            break
        if command == "bal": 
            balance()



main()    
