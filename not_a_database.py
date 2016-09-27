import csv
with open("data.csv") as open_file:
    contents = csv.reader(open_file)
    better = list(contents)

print(better)
def login_info():
    login_name = input("Please enter your username below \n >")
    login_password = input("Please enter your password below \n >")
    return [login_name, login_password]

def save_info(info):
    for line in better:
        if line[0] == info[0] and line[1] == info[1]:
            print("save")
            return line


def credential_check(info):
    for line in better:
        if line[0] == info[0] and line[1] == info[1]:
            print("LOGIN")
            return True
        else:
            continue

def use_program(info):
    print("Welcome back, {}".format(info[2]))
    choice = input("Do you want to (E)dit account, (C)reate account, or (L)og out?").upper()
    if choice == "C":
        add_user(new_user())
        use_program(info)
    elif choice == "L":
        log_out()
    elif choice == "E":
        edit_info(info)


def new_user():
    new_username = input(str("Enter a new name for a user: "))
    for line in better:
        while line[0] == new_username:
            print("Username already taken")
            new_username = input(str("Enter a new name for a user: "))
    new_password = input(str("Enter a new password for user: "))
    new_fullname = input(str("Enter the users full name: "))
    new_fact = input(str("Enter a fact about the new user: "))
    full_user = [new_username, new_password, new_fullname, new_fact]
    return ",".join(full_user)

def add_user(new_user):
    better = open("data.csv", "a")
    better.write("{}\n".format(new_user))
    better.close

def log_out():
    return program_running()

def edit_info(info):
    choice = input("Do you want a new (P)assword, or new (I)nformation?  ").upper()
    if choice == "P":
        change_password(info)

def change_password(info):
    password = "init"
    while password != info[1]:
        password = input("Enter your password here \n >")
    edit_password = input("Enter new password here \n >")
    better = open("data.csv")
    lines = list(better)

    new =[line.split(",") for line in lines]
    for line in new:
        if line[0] == info[0]:
            line[1] = edit_password
        else:
            continue
    
    better.close()



def program_running():
    attempt = False
    while not attempt:
        stuff = login_info()
        info = save_info(stuff)
        attempt = credential_check(stuff)
    if attempt:
        use_program(info)

program_running()
