def print_full_line(size, char):
    print(char * size)

def print_empty_line(size, char):
    if (size < 3):
        print(char * size)
    else:
        print(char + " " * (size - 2) + char)

def rectangle(width = 3, height = 3, char = "*"):
    print((char * width + "\n") * height, end="")

def square(size = 3, char = "*"):
    rectangle(width = size, height = size, char = char)

def pyramid(size = 3, char = "*"):
    for i in range(1, size + 1):
        print(" " * (size - i) + char * (2 * i - 1))

def empty_rectangle(width = 3, height = 3, char = "*"):
    if height == 0:
        return
    if height == 1:
        print_full_line(width, char)
    else:
        print_full_line(width, char)
        for _ in range(height - 2):
            print_empty_line(width, char)
        print_full_line(width, char)

def empty_diamond(size = 3, char = "*"):
    for i in range(1, size + 1):
        print(" " * (size - i) + char + " " * (2 * i - 3) + char * (i > 1))
    for i in range(size - 1, 0, -1):
        print(" " * (size - i) + char + " " * (2 * i - 3) + char * (i > 1))
