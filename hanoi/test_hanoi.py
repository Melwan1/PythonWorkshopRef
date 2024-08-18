from hanoi import hanoi

def test_hanoi_0_return():
    assert hanoi(0, 1, 2, 3) == 0

def test_hanoi_1_return():
    assert hanoi(1, 1, 2, 3) == 1

def test_hanoi_2_return():
    assert hanoi(2, 1, 2, 3) == 3

def test_hanoi_3_return():
    assert hanoi(3, 1, 2, 3) == 7

def test_hanoi_4_return():
    assert hanoi(4, 1, 2, 3) == 15

def test_hanoi_5_return():
    assert hanoi(5, 1, 2, 3) == 31

def test_hanoi_6_return():
    assert hanoi(6, 1, 2, 3) == 63

def test_hanoi_7_return():
    assert hanoi(7, 1, 2, 3) == 127

def test_hanoi_8_return():
    assert hanoi(8, 1, 2, 3) == 255

def test_hanoi_9_return():
    assert hanoi(9, 1, 2, 3) == 511

def test_hanoi_10_return():
    assert hanoi(10, 1, 2, 3) == 1023

def test_hanoi_0_output(capsys):
    hanoi(0, 1, 2, 3)
    out, _ = capsys.readouterr()
    assert out == ""

def test_hanoi_1_output(capsys):
    hanoi(1, 1, 3, 2)
    out, _ = capsys.readouterr()
    assert out == "Disk has been moved from 1 to 3\n"

def test_hanoi_2_output(capsys):
    hanoi(2, 1, 3, 2)
    out, _ = capsys.readouterr()
    assert out == "Disk has been moved from 1 to 2\nDisk has been moved from 1 to 3\nDisk has been moved from 2 to 3\n"

def test_hanoi_3_output(capsys):
    hanoi(3, 1, 3, 2)
    out, _ = capsys.readouterr()
    assert out == "Disk has been moved from 1 to 3\nDisk has been moved from 1 to 2\nDisk has been moved from 3 to 2\nDisk has been moved from 1 to 3\nDisk has been moved from 2 to 1\nDisk has been moved from 2 to 3\nDisk has been moved from 1 to 3\n"

def test_hanoi_4_output(capsys):
    hanoi(4, "A", "B", "C")
    out, _ = capsys.readouterr()
    assert out == "Disk has been moved from A to C\nDisk has been moved from A to B\nDisk has been moved from C to B\nDisk has been moved from A to C\nDisk has been moved from B to A\nDisk has been moved from B to C\nDisk has been moved from A to C\nDisk has been moved from A to B\nDisk has been moved from C to B\nDisk has been moved from C to A\nDisk has been moved from B to A\nDisk has been moved from C to B\nDisk has been moved from A to C\nDisk has been moved from A to B\nDisk has been moved from C to B\n"
