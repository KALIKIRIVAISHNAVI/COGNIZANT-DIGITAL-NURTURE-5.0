def validate_login(user, pwd):
    if user == "" or pwd == "":
        print("Username or password cannot be blank")
        return

    if user == "admin":
        if pwd == "pass123":
            print("Login Successful")
        else:
            print("Incorrect Password")
    else:
        print("Invalid Username")

user = "admin"
pwd = "pass123"

validate_login(user, pwd)