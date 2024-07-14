# Valid Credentials

In this exercise, you will learn to manipulate strings and regular expressions.

### File tree

```
valid_credentials
├── valid_credentials.py
└── test_valid_credentials.py
```

## Help for this exercise

For this exercise, using the `re` module of Python is highly recommended. For more information about this module, [click here](https://docs.python.org/3/howto/regex.html). Not using this module is possible but very tedious.

## Instructions

### Login

You will have to write the `is_valid_login(login: str) -> bool` function. It takes a string as argument (a login) and returns `True` if the login verifies all the rules related to the login, and `False` if at least one of the rules are violated. In addition ot that, it has to print a message for a the violated rules.

The set of rules to create a valid login is :

1. the login must contain between 4 and 40 characters (bounds included).
2. it has to be of the form `{firstName}.{lastName}`, where neither the first name nor the last name contain the `.` character
3. the first name and the last name may only contain letters, be they capital or not. The first name may also contain digits from 0 to 9. The accents are forbidden.
4. the possible digits of a first name can only be at the end of the first name.

If at least one of these rules are violated, a message has to be printed to the error output, with a trailing newline. The messages are : 

1. `The login has an invalid number of characters. Expected: between 4 and 40, got: {the length of the login}.`, where `{the length of the login}` is replaced by the real number of characters in the login.

2. `The login {login} is not of the form {firstName}.{lastName}.`, where `{login}` is replaced by the whole login.

3. 
    - If the problem is in the first name, the message is: `The first name contains an illegal character: {illegal character}.`, where `{illegal character}` is the first illegal character in the first name.

    - If the problem is in the last name, the message is : `The last name contains an illegal character: {illegal character}.`, where `{illegal character}` is the first illegal character in the last name.

4. `The first name may only contain digits at the end of it. Detected an illegal digit before the end: {illegal digit}.` where `{illegal digit}` is the first illegal digit found in the first name.

### Password

You will now have to write the function `is_valid_password(password: str) -> bool` that takes the password as argument and returns `True` if the password is valid, and false if it is not. As with the previous function, when the password is invalid, the function has to print a message on the error output.

The set of rules for the password is:

1. The password has to be at least 10 characters long (so that the password cannot be brute forced easily!)

2. It may contain all letters (capital or not), digits 0-9, special characters that are in this list: `#@&"'()§!-_$*%=+/:;.,?<>`. The accents are forbidden.

3. It has to contain at least one capital letter, one small letter (i.e. not capital), one digit and one special character.

The messages related to each rule violation are:

1. `The password has an invalid number of characters. Expected: at least 10, got: {the length of the password}.`.

2. `The password contains an illegal character: {illegal character}.`, where `{illegal character}` is the first illegal character in the password.

3. `The password is invalid because a {type of character} is missing.` The `{type of character}` is either `capital letter`, `small letter`, `digit` or `special character`.

As with the login, the messages must be followed by a trailing newline.

### Examples

Here are some test cases to help you:

| type     | input                | return value | error output                                                                                                                             |
|----------|----------------------|--------------|------------------------------------------------------------------------------------------------------------------------------------------|
| login    | john.smith     | True         |                                                                                                                                          |
| login    | moi                  | False        | `The login has an invalid number of characters. Expected: between 4 and 40, got: 3.\nThe login is not of the form {firstName}.{lastName}.\n` |
| password | Aa1&skibidi          | True         |                                                                                                                                          |
| password | SuchAGreatPassword99 | False        | `The password is invalid because a special character is missing.\n`                                                                          |

Mind the two `\n` in the second test case, since two messages have to be printed.