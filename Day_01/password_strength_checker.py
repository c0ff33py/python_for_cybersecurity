import re

def password_stength_checker(password):
    if len(password) < 8:
        return "Password too short (min 8 characters)"
    if not re.search(r"[A-Z]", password):
        return "Add at least one uppercase letter"
    if not re.search(r"[a-z]", password):
        return "Add at least none lowercase letter"
    if not re.search("[0-9]", password):
        return "Add at least one digit"
    if not re.search(r"[^A-Za-z0-9]", password):
        return "Add at least one symbol (e.g. !,@,#, etc.)"
    return "Strong Password!"

usr_pwd = input("Enter your password: ")
result = password_stength_checker(usr_pwd)
print(result)