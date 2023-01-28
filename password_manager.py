master_password = input("what is your password? ")

def view():
    with open('password.txt', 'r') as p:
        for line in p.readlines():
            print(line.rstrip())

def add():
    name = input("Account Name: ")
    password = input("password: ")
    with open('password.txt', 'a') as p:
        p.write(name + "|" + password + "/n")


while True:
    mode = input("would you like to add a new password or show exiting passwords? (view / add). Press q to quit ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid input,  mode is either  view or add ")
        continue