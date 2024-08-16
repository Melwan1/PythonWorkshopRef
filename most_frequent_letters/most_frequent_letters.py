ALPHABET_LENGTH = 26

import sys

def most_frequent_letters(filename, limit = ALPHABET_LENGTH):
    if not isinstance(limit, int):
        raise TypeError("The limit argument must be an integer")
    if limit < 1 or limit > 26:
        raise ValueError(f"The limit argument is invalid. Got: {limit}. Expected: between 1 and 26")
    content = ""
    try:
        with open(filename, 'r') as file:
            content = file.read()
        occurencies = {}
        for i in range(len(content)):
            if not content[i].isalpha():
                continue
            letter = content[i].upper()
            if letter in occurencies:
                occurencies[letter] += 1
            else:
                occurencies[letter] = 1
        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if not letter in occurencies:
                occurencies[letter] = 0
        sorted_array = sorted(occurencies.items(), key = lambda x: x[1], reverse = True)[:limit]
        return sorted_array
    except IOError as e:
        print("The file could not be opened or read.", file=sys.stderr)
