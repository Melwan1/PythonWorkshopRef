import sys
import pytest
import override_arithmetics

def test_add_1_return():
    arg1 = 7
    arg2 = 3
    expected = arg1 + arg2
    actual = override_arithmetics.add(arg1, arg2)
    assert expected == actual, f"Expected add({arg1}, {arg2}) to be: {expected}, got: {actual}"

def test_add_1_output(capsys):
    arg1 = 7
    arg2 = 3
    expected = arg1 + arg2
    actual = override_arithmetics.add(arg1, arg2)
    out, err = capsys.readouterr()
    assert out == f"{arg1} + {arg2} = {expected}\n", f"Expected add({arg1}, {arg2}) to print:\n{arg1} + {arg2} = {expected}\ngot:\n{out}"

def test_add_1_error(capsys):
    arg1 = 7
    arg2 = 3
    expected = arg1 + arg2
    actual = override_arithmetics.add(arg1, arg2)
    out, err = capsys.readouterr()
    assert err == "", f"Expected add({arg1}, {arg2}) to print nothing on error output, got:\n{err}"

def test_add_2_return():
    arg1 = -17
    arg2 = 999
    expected = arg1 + arg2
    actual = override_arithmetics.add(arg1, arg2)
    assert expected == actual, f"Expected add({arg1}, {arg2}) to be: {expected}, got: {actual}"

def test_add_2_output(capsys):
    arg1 = -17
    arg2 = 999
    expected = arg1 + arg2
    actual = override_arithmetics.add(arg1, arg2)
    out, err = capsys.readouterr()
    assert out == f"{arg1} + {arg2} = {expected}\n", f"Expected add({arg1}, {arg2}) to print:\n{arg1} + {arg2} = {expected}\ngot:\n{out}"

def test_add_2_error(capsys):
    arg1 = -17
    arg2 = 999
    expected = arg1 + arg2
    actual = override_arithmetics.add(arg1, arg2)
    out, err = capsys.readouterr()
    assert err == "", f"Expected add({arg1}, {arg2}) to print nothing on error output, got:\n{err}"

def test_add_3_return():
    arg1 = 1
    arg2 = -1
    expected = arg1 + arg2
    actual = override_arithmetics.add(arg1, arg2)
    assert expected == actual, f"Expected add({arg1}, {arg2}) to be: {expected}, got: {actual}"

def test_add_3_output(capsys):
    arg1 = 1
    arg2 = -1
    expected = arg1 + arg2
    actual = override_arithmetics.add(arg1, arg2)
    out, err = capsys.readouterr()
    assert out == f"{arg1} + {arg2} = {expected}\n", f"Expected add({arg1}, {arg2}) to print:\n{arg1} + {arg2} = {expected}\ngot:\n{out}"

def test_add_3_error(capsys):
    arg1 = 1
    arg2 = -1
    expected = arg1 + arg2
    actual = override_arithmetics.add(arg1, arg2)
    out, err = capsys.readouterr()
    assert err == "", f"Expected add({arg1}, {arg2}) to print nothing on error output, got:\n{err}"

def test_sub_1_return():
    arg1 = 7
    arg2 = 3
    expected = arg1 - arg2
    actual = override_arithmetics.sub(arg1, arg2)
    assert expected == actual, f"Expected sub({arg1}, {arg2}) to be: {expected}, got: {actual}"

def test_sub_1_output(capsys):
    arg1 = 7
    arg2 = 3
    expected = arg1 - arg2
    actual = override_arithmetics.sub(arg1, arg2)
    out, err = capsys.readouterr()
    assert out == f"{arg1} - {arg2} = {expected}\n", f"Expected sub({arg1}, {arg2}) to print:\n{arg1} - {arg2} = {expected}\ngot:\n{out}"

def test_sub_1_error(capsys):
    arg1 = 7
    arg2 = 3
    expected = arg1 - arg2
    actual = override_arithmetics.sub(arg1, arg2)
    out, err = capsys.readouterr()
    assert err == "", f"Expected sub({arg1}, {arg2}) to print nothing on error output, got:\n{err}"

def test_sub_2_return():
    arg1 = -17
    arg2 = 999
    expected = arg1 - arg2
    actual = override_arithmetics.sub(arg1, arg2)
    assert expected == actual, f"Expected sub({arg1}, {arg2}) to be: {expected}, got: {actual}"

def test_sub_2_output(capsys):
    arg1 = -17
    arg2 = 999
    expected = arg1 - arg2
    actual = override_arithmetics.sub(arg1, arg2)
    out, err = capsys.readouterr()
    assert out == f"{arg1} - {arg2} = {expected}\n", f"Expected sub({arg1}, {arg2}) to print:\n{arg1} - {arg2} = {expected}\ngot:\n{out}"

def test_sub_2_error(capsys):
    arg1 = -17
    arg2 = 999
    expected = arg1 - arg2
    actual = override_arithmetics.sub(arg1, arg2)
    out, err = capsys.readouterr()
    assert err == "", f"Expected sub({arg1}, {arg2}) to print nothing on error output, got:\n{err}"

def test_sub_3_return():
    arg1 = 1
    arg2 = -1
    expected = arg1 - arg2
    actual = override_arithmetics.sub(arg1, arg2)
    assert expected == actual, f"Expected sub({arg1}, {arg2}) to be: {expected}, got: {actual}"

def test_sub_3_output(capsys):
    arg1 = 1
    arg2 = -1
    expected = arg1 - arg2
    actual = override_arithmetics.sub(arg1, arg2)
    out, err = capsys.readouterr()
    assert out == f"{arg1} - {arg2} = {expected}\n", f"Expected sub({arg1}, {arg2}) to print:\n{arg1} - {arg2} = {expected}\ngot:\n{out}"

def test_sub_3_error(capsys):
    arg1 = 1
    arg2 = -1
    expected = arg1 - arg2
    actual = override_arithmetics.sub(arg1, arg2)
    out, err = capsys.readouterr()
    assert err == "", f"Expected sub({arg1}, {arg2}) to print nothing on error output, got:\n{err}"

def test_mul_1_return():
    arg1 = 7
    arg2 = 3
    expected = arg1 * arg2
    actual = override_arithmetics.mul(arg1, arg2)
    assert expected == actual, f"Expected mul({arg1}, {arg2}) to be: {expected}, got: {actual}"

def test_mul_1_output(capsys):
    arg1 = 7
    arg2 = 3
    expected = arg1 * arg2
    actual = override_arithmetics.mul(arg1, arg2)
    out, err = capsys.readouterr()
    assert out == f"{arg1} * {arg2} = {expected}\n", f"Expected mul({arg1}, {arg2}) to print:\n{arg1} * {arg2} = {expected}\ngot:\n{out}"

def test_mul_1_error(capsys):
    arg1 = 7
    arg2 = 3
    expected = arg1 * arg2
    actual = override_arithmetics.mul(arg1, arg2)
    out, err = capsys.readouterr()
    assert err == "", f"Expected mul({arg1}, {arg2}) to print nothing on error output, got:\n{err}"

def test_mul_2_return():
    arg1 = -17
    arg2 = 999
    expected = arg1 * arg2
    actual = override_arithmetics.mul(arg1, arg2)
    assert expected == actual, f"Expected mul({arg1}, {arg2}) to be: {expected}, got: {actual}"

def test_mul_2_output(capsys):
    arg1 = -17
    arg2 = 999
    expected = arg1 * arg2
    actual = override_arithmetics.mul(arg1, arg2)
    out, err = capsys.readouterr()
    assert out == f"{arg1} * {arg2} = {expected}\n", f"Expected mul({arg1}, {arg2}) to print:\n{arg1} * {arg2} = {expected}\ngot:\n{out}"

def test_mul_2_error(capsys):
    arg1 = -17
    arg2 = 999
    expected = arg1 * arg2
    actual = override_arithmetics.mul(arg1, arg2)
    out, err = capsys.readouterr()
    assert err == "", f"Expected mul({arg1}, {arg2}) to print nothing on error output, got:\n{err}"

def test_mul_3_return():
    arg1 = 1
    arg2 = -1
    expected = arg1 * arg2
    actual = override_arithmetics.mul(arg1, arg2)
    assert expected == actual, f"Expected mul({arg1}, {arg2}) to be: {expected}, got: {actual}"

def test_mul_3_output(capsys):
    arg1 = 1
    arg2 = -1
    expected = arg1 * arg2
    actual = override_arithmetics.mul(arg1, arg2)
    out, err = capsys.readouterr()
    assert out == f"{arg1} * {arg2} = {expected}\n", f"Expected mul({arg1}, {arg2}) to print:\n{arg1} * {arg2} = {expected}\ngot:\n{out}"

def test_mul_3_error(capsys):
    arg1 = 1
    arg2 = -1
    expected = arg1 * arg2
    actual = override_arithmetics.mul(arg1, arg2)
    out, err = capsys.readouterr()
    assert err == "", f"Expected mul({arg1}, {arg2}) to print nothing on error output, got:\n{err}"

def test_div_1_return():
    arg1 = 7
    arg2 = 3
    expected = arg1 // arg2
    actual = override_arithmetics.div(arg1, arg2)
    assert expected == actual, f"Expected div({arg1}, {arg2}) to be: {expected}, got: {actual}"

def test_div_1_output(capsys):
    arg1 = 7
    arg2 = 3
    expected = arg1 // arg2
    actual = override_arithmetics.div(arg1, arg2)
    out, err = capsys.readouterr()
    assert out == f"{arg1} // {arg2} = {expected}\n", f"Expected div({arg1}, {arg2}) to print:\n{arg1} // {arg2} = {expected}\ngot:\n{out}"

def test_div_1_error(capsys):
    arg1 = 7
    arg2 = 3
    expected = arg1 // arg2
    actual = override_arithmetics.div(arg1, arg2)
    out, err = capsys.readouterr()
    assert err == "", f"Expected div({arg1}, {arg2}) to print nothing on error output, got:\n{err}"

def test_div_2_return():
    arg1 = -17
    arg2 = 999
    expected = arg1 // arg2
    actual = override_arithmetics.div(arg1, arg2)
    assert expected == actual, f"Expected div({arg1}, {arg2}) to be: {expected}, got: {actual}"

def test_div_2_output(capsys):
    arg1 = -17
    arg2 = 999
    expected = arg1 // arg2
    actual = override_arithmetics.div(arg1, arg2)
    out, err = capsys.readouterr()
    assert out == f"{arg1} // {arg2} = {expected}\n", f"Expected div({arg1}, {arg2}) to print:\n{arg1} // {arg2} = {expected}\ngot:\n{out}"

def test_div_2_error(capsys):
    arg1 = -17
    arg2 = 999
    expected = arg1 // arg2
    actual = override_arithmetics.div(arg1, arg2)
    out, err = capsys.readouterr()
    assert err == "", f"Expected div({arg1}, {arg2}) to print nothing on error output, got:\n{err}"

def test_div_3_return():
    arg1 = 1
    arg2 = -1
    expected = arg1 // arg2
    actual = override_arithmetics.div(arg1, arg2)
    assert expected == actual, f"Expected div({arg1}, {arg2}) to be: {expected}, got: {actual}"

def test_div_3_output(capsys):
    arg1 = 1
    arg2 = -1
    expected = arg1 // arg2
    actual = override_arithmetics.div(arg1, arg2)
    out, err = capsys.readouterr()
    assert out == f"{arg1} // {arg2} = {expected}\n", f"Expected div({arg1}, {arg2}) to print:\n{arg1} // {arg2} = {expected}\ngot:\n{out}"

def test_div_3_error(capsys):
    arg1 = 1
    arg2 = -1
    expected = arg1 // arg2
    actual = override_arithmetics.div(arg1, arg2)
    out, err = capsys.readouterr()
    assert err == "", f"Expected div({arg1}, {arg2}) to print nothing on error output, got:\n{err}"

def test_div_by_zero_output(capsys):
    arg1 = 1
    arg2 = 0
    override_arithmetics.div(arg1, arg2)
    out, err = capsys.readouterr()
    assert out == "", f"Expected div({arg1}, {arg2}) to print nothing on standard output, got:\n{out}"

def test_div_by_zero_error(capsys):
    arg1 = 1
    arg2 = 0
    override_arithmetics.div(arg1, arg2)
    out, err = capsys.readouterr()
    assert err == "Detected a division by zero\n", f"Expected div({arg1}, {arg2}) to print:\nDetected a division by zero\nfollowed by a trailing newline on error output, got:\n{err}"

def test_mod_1_return():
    arg1 = 7
    arg2 = 3
    expected = arg1 % arg2
    actual = override_arithmetics.mod(arg1, arg2)
    assert expected == actual, f"Expected mod({arg1}, {arg2}) to be: {expected}, got: {actual}"

def test_mod_1_output(capsys):
    arg1 = 7
    arg2 = 3
    expected = arg1 % arg2
    actual = override_arithmetics.mod(arg1, arg2)
    out, err = capsys.readouterr()
    assert out == f"{arg1} % {arg2} = {expected}\n", f"Expected mod({arg1}, {arg2}) to print:\n{arg1} % {arg2} = {expected}\ngot:\n{out}"

def test_mod_1_error(capsys):
    arg1 = 7
    arg2 = 3
    expected = arg1 % arg2
    actual = override_arithmetics.mod(arg1, arg2)
    out, err = capsys.readouterr()
    assert err == "", f"Expected mod({arg1}, {arg2}) to print nothing on error output, got:\n{err}"

def test_mod_2_return():
    arg1 = -17
    arg2 = 999
    expected = arg1 % arg2
    actual = override_arithmetics.mod(arg1, arg2)
    assert expected == actual, f"Expected mod({arg1}, {arg2}) to be: {expected}, got: {actual}"

def test_mod_2_output(capsys):
    arg1 = -17
    arg2 = 999
    expected = arg1 % arg2
    actual = override_arithmetics.mod(arg1, arg2)
    out, err = capsys.readouterr()
    assert out == f"{arg1} % {arg2} = {expected}\n", f"Expected mod({arg1}, {arg2}) to print:\n{arg1} % {arg2} = {expected}\ngot:\n{out}"

def test_mod_2_error(capsys):
    arg1 = -17
    arg2 = 999
    expected = arg1 % arg2
    actual = override_arithmetics.mod(arg1, arg2)
    out, err = capsys.readouterr()
    assert err == "", f"Expected mod({arg1}, {arg2}) to print nothing on error output, got:\n{err}"

def test_mod_3_return():
    arg1 = 1
    arg2 = -1
    expected = arg1 % arg2
    actual = override_arithmetics.mod(arg1, arg2)
    assert expected == actual, f"Expected mod({arg1}, {arg2}) to be: {expected}, got: {actual}"

def test_mod_3_output(capsys):
    arg1 = 1
    arg2 = -1
    expected = arg1 % arg2
    actual = override_arithmetics.mod(arg1, arg2)
    out, err = capsys.readouterr()
    assert out == f"{arg1} % {arg2} = {expected}\n", f"Expected mod({arg1}, {arg2}) to print:\n{arg1} % {arg2} = {expected}\ngot:\n{out}"

def test_mod_3_error(capsys):
    arg1 = 1
    arg2 = -1
    expected = arg1 % arg2
    actual = override_arithmetics.mod(arg1, arg2)
    out, err = capsys.readouterr()
    assert err == "", f"Expected mod({arg1}, {arg2}) to print nothing on error output, got:\n{err}"

def test_mod_by_zero_output(capsys):
    arg1 = 1
    arg2 = 0
    override_arithmetics.mod(arg1, arg2)
    out, err = capsys.readouterr()
    assert out == "", f"Expected mod({arg1}, {arg2}) to print nothing on standard output, got:\n{out}"

def test_mod_by_zero_error(capsys):
    arg1 = 1
    arg2 = 0
    override_arithmetics.mod(arg1, arg2)
    out, err = capsys.readouterr()
    assert err == "Detected a modulo by zero\n", f"Expected mod({arg1}, {arg2}) to print:\nDetected a division by zero\nfollowed by a trailing newline on error output, got:\n{err}"

def test_pow_1_return():
    arg1 = 2
    arg2 = 2
    expected = arg1 ** arg2
    actual = override_arithmetics.pow(arg1, arg2)
    assert expected == actual, f"Expected pow({arg1}, {arg2}) to be: {expected}, got: {actual}"

def test_pow_1_output(capsys):
    arg1 = 2
    arg2 = 2
    expected = arg1 ** arg2
    actual = override_arithmetics.pow(arg1, arg2)
    out, err = capsys.readouterr()
    assert out == f"{arg1} ** {arg2} = {expected}\n", f"Expected pow({arg1}, {arg2}) to print:\n{arg1} ** {arg2} = {expected}\ngot:\n{out}"

def test_pow_1_error(capsys):
    arg1 = 2
    arg2 = 2
    expected = arg1 ** arg2
    actual = override_arithmetics.pow(arg1, arg2)
    out, err = capsys.readouterr()
    assert err == "", f"Expected pow({arg1}, {arg2}) to print nothing on error output, got:\n{err}"

def test_pow_2_return():
    arg1 = 4
    arg2 = -3
    expected = arg1 ** arg2
    actual = override_arithmetics.pow(arg1, arg2)
    assert expected == actual, f"Expected pow({arg1}, {arg2}) to be: {expected}, got: {actual}"

def test_pow_2_output(capsys):
    arg1 = 4
    arg2 = -3
    expected = arg1 ** arg2
    actual = override_arithmetics.pow(arg1, arg2)
    out, err = capsys.readouterr()
    assert out == f"{arg1} ** {arg2} = {expected}\n", f"Expected pow({arg1}, {arg2}) to print:\n{arg1} ** {arg2} = {expected}\ngot:\n{out}"

def test_pow_2_error(capsys):
    arg1 = 4
    arg2 = -3
    expected = arg1 ** arg2
    actual = override_arithmetics.pow(arg1, arg2)
    out, err = capsys.readouterr()
    assert err == "", f"Expected pow({arg1}, {arg2}) to print nothing on error output, got:\n{err}"

def test_pow_3_return():
    arg1 = 3
    arg2 = 16
    expected = arg1 ** arg2
    actual = override_arithmetics.pow(arg1, arg2)
    assert expected == actual, f"Expected pow({arg1}, {arg2}) to be: {expected}, got: {actual}"

def test_pow_3_output(capsys):
    arg1 = 3
    arg2 = 16
    expected = arg1 ** arg2
    actual = override_arithmetics.pow(arg1, arg2)
    out, err = capsys.readouterr()
    assert out == f"{arg1} ** {arg2} = {expected}\n", f"Expected pow({arg1}, {arg2}) to print:\n{arg1} ** {arg2} = {expected}\ngot:\n{out}"

def test_pow_3_error(capsys):
    arg1 = 3
    arg2 = 16
    expected = arg1 ** arg2
    actual = override_arithmetics.pow(arg1, arg2)
    out, err = capsys.readouterr()
    assert err == "", f"Expected pow({arg1}, {arg2}) to print nothing on error output, got:\n{err}"


