import pytest
import sys
from hello_world import hello_world

def test_hello_world_output(capsys):
    hello_world()
    out,err = capsys.readouterr()
    assert out == "Hello World!\n", f"Output of hello_world() differs, expected\n Hello world!\nwith a trailing newline, got:\n {out}."

def test_hello_world_error(capsys):
    hello_world()
    out,err = capsys.readouterr()
    assert err == "", f"Expected nothing on error, got:\n {err}."
