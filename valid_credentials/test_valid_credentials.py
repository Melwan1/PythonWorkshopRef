import sys
import pytest
from valid_credentials import is_valid_login, is_valid_password

def test_valid_login_1_return():
    login = "john.smith"
    assert is_valid_login(login)

def test_valid_login_1_error(capsys):
    login = "john.smith"
    is_valid_login(login)
    _, err = capsys.readouterr()
    assert err == "", f"Expected is_valid_login({login}) to print nothing on error output, got:\n{err}"

def test_valid_login_2_return():
    login = "averylongnamewithdigits987.othername"
    assert is_valid_login(login)

def test_valid_login_2_error(capsys):
    login = "averylongnamewithdigits987.othername"
    is_valid_login(login)
    _, err = capsys.readouterr()
    assert err == "", f"Expected is_valid_login({login}) to print nothing on error output, got:\n{err}"

def test_invalid_login_too_short_return():
    login = "a.b"
    assert not is_valid_login(login)

def test_invalid_login_too_short_error(capsys):
    login = "a.b"
    is_valid_login(login)
    _, err = capsys.readouterr()
    assert err == f"The login has an invalid number of characters. Expected: between 4 and 40, got: {len(login)}\n"

def test_invalid_login_too_long_return():
    login = "thisisaloginwaytoolong.thisisaloginwaytoolong"
    assert not is_valid_login(login)

def test_invalid_login_too_long_error(capsys):
    login = "thisisaloginwaytoolong.thisisaloginwaytoolong"
    is_valid_login(login)
    _, err = capsys.readouterr()
    assert err == f"The login has an invalid number of characters. Expected: between 4 and 40, got: {len(login)}\n"

def test_invalid_login_bad_format_return():
    login = "firstname_lastname"
    assert not is_valid_login(login)

def test_invalid_login_bad_format_error(capsys):
    login = "firstname_lastname"
    is_valid_login(login)
    _, err = capsys.readouterr()
    assert err == "The login " f"{login}" " is not of the form {firstName}.{lastName}.\n"

def test_invalid_login_multiple_dots_return():
    login = "firstname.surname.lastname"
    assert not is_valid_login(login)

def test_invalid_login_multiple_dots_error(capsys):
    login = "firstname.surname.lastname"
    is_valid_login(login)
    _, err = capsys.readouterr()
    assert err == "The login " f"{login}" " is not of the form {firstName}.{lastName}.\n"

def test_invalid_login_invalid_firstname_digits_return():
    login = "joh3n.smith"
    assert not is_valid_login(login)

def test_invalid_login_invalid_firstname_digits_error(capsys):
    login = "joh3n.smith"
    is_valid_login(login)
    _, err = capsys.readouterr()
    assert err == "The first name contains an illegal character: n.\n"
 
def test_invalid_login_invalid_lastname_digits_1_return():
    login = "john.smith2"
    assert not is_valid_login(login)

def test_invalid_login_invalid_lastname_digits_1_error(capsys):
    login = "john.smith2"
    is_valid_login(login)
    _, err = capsys.readouterr()
    assert err == "The last name contains an illegal character: 2.\n"

def test_invalid_login_invalid_firstname_digits_2_return():
    login = "john.smit\nh"
    assert not is_valid_login(login)

def test_invalid_login_invalid_firstname_digits_2_error(capsys):
    login = "john.smit$h"
    is_valid_login(login)
    _, err = capsys.readouterr()
    assert err == "The last name contains an illegal character: $.\n"
 
def test_valid_password_1_return():
    password = "Aa1&skibidi"
    assert is_valid_password(password)

def test_valid_password_1_error(capsys):
    password = "Aa1&skibidi"
    is_valid_password(password)
    _, err = capsys.readouterr()
    assert err == "", f"Expected is_valid_password({password}) to print nothing on error output, got:\n{err}"

def test_valid_password_2_return():
    password = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789#@&\"'()§!-_$*%=+/:;.,?"
    assert is_valid_password(password)

def test_valid_password_2_error(capsys):
    password = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789#@&\"'()§!-_$*%=+/:;.,?"
    is_valid_password(password)
    _, err = capsys.readouterr()
    assert err == "", f"Expected is_valid_password({password}) to print nothing on error output, got:\n{err}"

def test_invalid_password_too_short_return():
    password = "Aa1&skib"
    assert not is_valid_password(password)

def test_invalid_password_too_short_error(capsys):
    password = "Aa1&skib"
    is_valid_password(password)
    _, err = capsys.readouterr()
    assert err == f"The password has an invalid number of characters. Expected: at least 10, got: {len(password)}.\n"

def test_invalid_password_missing_capital_letter_return():
    password = "aa1&skibidi"
    assert not is_valid_password(password)

def test_invalid_password_missing_capital_letter_error(capsys):
    password = "aa1&skibidi"
    is_valid_password(password)
    _, err = capsys.readouterr()
    assert err == f"The password is invalid because a capital letter is missing.\n"

def test_invalid_password_missing_small_letter_return():
    password = "AA1&SKIBIDI"
    assert not is_valid_password(password)

def test_invalid_password_missing_small_letter_error(capsys):
    password = "A1&SKIBIDI"
    is_valid_password(password)
    _, err = capsys.readouterr()
    assert err == f"The password is invalid because a small letter is missing.\n"

def test_invalid_password_missing_digit_return():
    password = "Aa&skibidi"
    assert not is_valid_password(password)

def test_invalid_password_missing_digit_error(capsys):
    password = "Aa&skibidi"
    is_valid_password(password)
    _, err = capsys.readouterr()
    assert err == f"The password is invalid because a digit is missing.\n"

def test_invalid_password_missing_special_character_return():
    password = "Aa1skibidi"
    assert not is_valid_password(password)

def test_invalid_password_missing_special_character_error(capsys):
    password = "Aa1skibidi"
    is_valid_password(password)
    _, err = capsys.readouterr()
    assert err == f"The password is invalid because a special character is missing.\n"

def test_invalid_password_missing_capital_letter_and_small_letter_return():
    password = "&%$*102973"
    assert not is_valid_password(password)

def test_invalid_password_missing_capital_letter_and_small_letter_error(capsys):
    password = "&%$*102973"
    is_valid_password(password)
    _, err = capsys.readouterr()
    assert err == f"The password is invalid because a capital letter is missing.\nThe password is invalid because a small letter is missing.\n"

def test_invalid_password_missing_capital_letter_and_digit_return():
    password = "&%$*aabbcc"
    assert not is_valid_password(password)

def test_invalid_password_missing_capital_letter_and_digit_error(capsys):
    password = "&%$*aabbcc"
    is_valid_password(password)
    _, err = capsys.readouterr()
    assert err == f"The password is invalid because a capital letter is missing.\nThe password is invalid because a digit is missing.\n"

def test_invalid_password_missing_small_letter_and_digit_return():
    password = "&%$*aabbcc"
    assert not is_valid_password(password)

def test_invalid_password_missing_small_letter_and_digit_error(capsys):
    password = "&%$*AABBCC"
    is_valid_password(password)
    _, err = capsys.readouterr()
    assert err == f"The password is invalid because a small letter is missing.\nThe password is invalid because a digit is missing.\n"

def test_invalid_password_missing_small_letter_and_special_character_return():
    password = "AABBCC112233"
    assert not is_valid_password(password)

def test_invalid_password_missing_small_letter_and_special_character_error(capsys):
    password = "AABBCC112233"
    is_valid_password(password)
    _, err = capsys.readouterr()
    assert err == f"The password is invalid because a small letter is missing.\nThe password is invalid because a special character is missing.\n"

def test_invalid_password_invalid_character_1_return():
    password = "Aa1&skibidi "
    assert not is_valid_password(password)

def test_invalid_password_invalid_character_1_error(capsys):
    password = "Aa1&skibidi "
    is_valid_password(password)
    _, err = capsys.readouterr()
    assert err == f"The password contains an illegal character:  .\n"

def test_invalid_password_invalid_character_2_return():
    password = "Aa1&skibidi "
    assert not is_valid_password(password)

def test_invalid_password_invalid_character_2_error(capsys):
    password = "A\na1&skibidi"
    is_valid_password(password)
    _, err = capsys.readouterr()
    assert err == f"The password contains an illegal character: \n.\n"

def test_invalid_password_invalid_character_3_return():
    password = "Aa1&skibidi "
    assert not is_valid_password(password)

def test_invalid_password_invalid_character_3_error(capsys):
    password = "Aàù1&skibidi"
    is_valid_password(password)
    _, err = capsys.readouterr()
    assert err == f"The password contains an illegal character: à.\n"