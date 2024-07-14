import re
import sys

def match_first_name(first_name: str) -> bool:
    allow_digits : bool = False
    for index in range(len(first_name)):
        if not first_name[index].isalnum():
            print(f"The first name contains an illegal character: {first_name[index]}.", file=sys.stderr)
            return False
        if allow_digits and first_name[index].isalpha():
            print(f"The first name contains an illegal character: {first_name[index]}.", file=sys.stderr)
            return False
        if first_name[index].isdigit():
            allow_digits = True
    return True

def match_last_name(last_name: str) -> bool:
    for index in range(len(last_name)):
        if not last_name[index].isalpha():
            print(f"The last name contains an illegal character: {last_name[index]}.", file=sys.stderr)
            return False
    return True

def is_valid_login(login: str) -> bool:
    valid: bool = True
    if len(login) < 4 or len(login) > 40:
        print("The login has an invalid number of characters. Expected: between 4 and 40, got:", len(login), file=sys.stderr)
        valid = False
    names = re.compile("[^.]+")
    m = names.findall(login)
    if len(m) != 2:
        print("The login", login, "is not of the form {firstName}.{lastName}.", file=sys.stderr)
        valid = False
    else:
        first_name : str = m[0]
        if not match_first_name(first_name):
            valid = False
        last_name : str = m[1]
        if not match_last_name(last_name):
            valid = False
    return valid

def is_valid_password(password: str) -> bool:
    valid: bool = True
    if len(password) < 10:
        print(f"The password has an invalid number of characters. Expected: at least 10, got: {len(password)}.", file=sys.stderr)
        valid = False
    if len(re.compile("[A-Z]").findall(password)) == 0:
        print("The password is invalid because a capital letter is missing.", file=sys.stderr)
        valid = False
    if len(re.compile("[a-z]").findall(password)) == 0:
        print("The password is invalid because a small letter is missing.", file=sys.stderr)
        valid = False
    if len(re.compile("[0-9]").findall(password)) == 0:
        print("The password is invalid because a digit is missing.", file=sys.stderr)
        valid = False
    if len(re.compile("[#@&\"'()§!_$*%=+/:;.,?-]").findall(password)) == 0:
        print("The password is invalid because a special character is missing.", file=sys.stderr)
        valid = False
    for index in range(len(password)):
        if re.compile("[^A-Za-z0-9]").match(password[index]) and not password[index] in "#@&\"'()§!_$*%=+/:;.,?-":
            print(f"The password contains an illegal character: {password[index]}.", file=sys.stderr)
            valid = False
            break
    return valid