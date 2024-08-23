import shape_printer

def check_output(capsys, out_ref):
    out_actual, _ = capsys.readouterr()
    assert out_actual == out_ref


def test_shape_printer_rectangle_1(capsys):
    shape_printer.rectangle()
    check_output(capsys, "***\n***\n***\n")

def test_shape_printer_rectangle_2(capsys):
    shape_printer.rectangle(width = 2)
    check_output(capsys, "**\n**\n**\n")

def test_shape_printer_rectangle_3(capsys):
    shape_printer.rectangle(width = 0)
    check_output(capsys, "\n\n\n")

def test_shape_printer_rectangle_4(capsys):
    shape_printer.rectangle(height = 2)
    check_output(capsys, "***\n***\n")

def test_shape_printer_rectangle_5(capsys):
    shape_printer.rectangle(height = 0)
    check_output(capsys, "")

def test_shape_printer_rectangle_6(capsys):
    shape_printer.rectangle(char = "p")
    check_output(capsys, "ppp\nppp\nppp\n")

def test_shape_printer_rectangle_7(capsys):
    shape_printer.rectangle(char = " ")
    check_output(capsys, "   \n   \n   \n")

def test_shape_printer_rectangle_8(capsys):
    shape_printer.rectangle(width = 5, height = 2, char = "|")
    check_output(capsys, "|||||\n|||||\n")

def test_shape_printer_rectangle_9(capsys):
    shape_printer.rectangle(width = 0, height = 0, char = "|")
    check_output(capsys, "")

def test_shape_printer_rectangle_10(capsys):
    shape_printer.rectangle(width = 10, height = 15, char = "\n")
    check_output(capsys, "\n" * 165)

def test_shape_printer_square_1(capsys):
    shape_printer.square()
    check_output(capsys, (("*" * 3) + "\n") * 3)

def test_shape_printer_square_2(capsys):
    size = 3
    char = "*"
    shape_printer.square(size = size, char = char)
    check_output(capsys, ((char * size) + "\n") * size)

def test_shape_printer_square_3(capsys):
    size = 2
    char = "*"
    shape_printer.square(size = size, char = char)
    check_output(capsys, ((char * size) + "\n") * size)

def test_shape_printer_square_4(capsys):
    size = 0
    char = "*"
    shape_printer.square(size = size, char = char)
    check_output(capsys, ((char * size) + "\n") * size)

def test_shape_printer_square_5(capsys):
    size = 3
    char = "|"
    shape_printer.square(size = size, char = char)
    check_output(capsys, ((char * size) + "\n") * size)

def test_shape_printer_square_6(capsys):
    size = 4
    char = "_"
    shape_printer.square(size = size, char = char)
    check_output(capsys, ((char * size) + "\n") * size)

def test_shape_printer_square_7(capsys):
    size = 20
    char = "x"
    shape_printer.square(size = size, char = char)
    check_output(capsys, ((char * size) + "\n") * size)

def test_shape_printer_square_8(capsys):
    size = 40
    char = "lol"
    shape_printer.square(size = size, char = char)
    check_output(capsys, ((char * size) + "\n") * size)

def test_shape_printer_square_9(capsys):
    size = 4
    char = "\n"
    shape_printer.square(size = size, char = char)
    check_output(capsys, ((char * size) + "\n") * size)

def test_shape_printer_pyramid_1(capsys):
    shape_printer.pyramid()
    check_output(capsys, "  *\n ***\n*****\n")

def test_shape_printer_pyramid_2(capsys):
    shape_printer.pyramid(size = 0)
    check_output(capsys, "")

def test_shape_printer_pyramid_2(capsys):
    shape_printer.pyramid(size = 1)
    check_output(capsys, "*\n")

def test_shape_printer_pyramid_3(capsys):
    shape_printer.pyramid(size = 2)
    check_output(capsys, " *\n***\n")

def test_shape_printer_pyramid_4(capsys):
    shape_printer.pyramid(size = 3)
    check_output(capsys, "  *\n ***\n*****\n")

def test_shape_printer_pyramid_5(capsys):
    shape_printer.pyramid(size = 6)
    check_output(capsys, "     *\n    ***\n   *****\n  *******\n *********\n***********\n")

def test_shape_printer_pyramid_6(capsys):
    shape_printer.pyramid(size = 6, char = "/")
    check_output(capsys, "     /\n    ///\n   /////\n  ///////\n /////////\n///////////\n")

def test_shape_printer_empty_rectangle_1(capsys):
    shape_printer.empty_rectangle()
    check_output(capsys, "***\n* *\n***\n")

def test_shape_printer_empty_rectangle_2(capsys):
    shape_printer.empty_rectangle(width = 3, height = 3, char = "*")
    check_output(capsys, "***\n* *\n***\n")

def test_shape_printer_empty_rectangle_3(capsys):
    shape_printer.empty_rectangle(width = 0, height = 3, char = "*")
    check_output(capsys, "\n\n\n")

def test_shape_printer_empty_rectangle_4(capsys):
    shape_printer.empty_rectangle(width = 1, height = 3, char = "-")
    check_output(capsys, "-\n-\n-\n")

def test_shape_printer_empty_rectangle_5(capsys):
    shape_printer.empty_rectangle(width = 2, height = 3, char = "-")
    check_output(capsys, "--\n--\n--\n")

def test_shape_printer_empty_rectangle_6(capsys):
    shape_printer.empty_rectangle(width = 3, height = 0, char = "-")
    check_output(capsys, "")

def test_shape_printer_empty_rectangle_7(capsys):
    shape_printer.empty_rectangle(width = 3, height = 1, char = "-")
    check_output(capsys, "---\n")

def test_shape_printer_empty_rectangle_8(capsys):
    shape_printer.empty_rectangle(width = 3, height = 2, char = "-")
    check_output(capsys, "---\n---\n")

def test_shape_printer_empty_rectangle_9(capsys):
    shape_printer.empty_rectangle(width = 10, height = 10, char = "-")
    check_output(capsys, "----------\n-        -\n-        -\n-        -\n-        -\n-        -\n-        -\n-        -\n-        -\n----------\n")

def test_shape_printer_empty_diamond_1(capsys):
    shape_printer.empty_diamond()
    check_output(capsys, "  *\n * *\n*   *\n * *\n  *\n")

def test_shape_printer_empty_diamond_2(capsys):
    shape_printer.empty_diamond(size = 0)
    check_output(capsys, "")

def test_shape_printer_empty_diamond_3(capsys):
    shape_printer.empty_diamond(size = 1)
    check_output(capsys, "*\n")

def test_shape_printer_empty_diamond_4(capsys):
    shape_printer.empty_diamond(size = 2)
    check_output(capsys, " *\n* *\n *\n")

def test_shape_printer_empty_diamond_5(capsys):
    shape_printer.empty_diamond(char = ")")
    check_output(capsys, "  )\n ) )\n)   )\n ) )\n  )\n")

def test_shape_printer_empty_diamond_6(capsys):
    shape_printer.empty_diamond(size = 7, char = "o")
    check_output(capsys, "      o\n     o o\n    o   o\n   o     o\n  o       o\n o         o\no           o\n o         o\n  o       o\n   o     o\n    o   o\n     o o\n      o\n")

