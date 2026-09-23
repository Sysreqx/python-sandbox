import re


def check_password(password: str):
    if len(password) < 8:
        print("Password must contain at least 8 characters")
        return

    is_lowercase = False
    is_uppercase = False
    is_digit = False
    is_special = False

    if re.search(r"[a-z]", password):
        is_lowercase = True
    else:
        print('Password must contain at least one lowercase letter')

    if re.search(r"[A-Z]", password):
        is_uppercase = True
    else:
        print('Password must contain at least one uppercase letter')

    if re.search(r"[0-9]", password):
        is_digit = True
    else:
        print('Password must contain at least one number')

    if re.search(r"[!@#$%^&*]", password):
        is_special = True
    else:
        print('Password must contain at least one special character "!@#$%^&*"')

    if is_lowercase and is_uppercase and is_digit and is_special:
        print("Password is OK")
        return True
    else:
        print("Password is not OK")
        return False


user_pass = input("Enter password: ")

check_password(user_pass)
