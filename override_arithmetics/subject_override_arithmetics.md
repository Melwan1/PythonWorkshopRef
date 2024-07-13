# Override Arithmetics

In this exercise, you will learn to manipulate basic operations in Python, as well as learn basic f-strings. 

### File tree

```
override_arithmetics
├── override_arithmetics.py
└── test_override_arithmetics.py
```

## Help for this exercise

### Function definitions

For more information about function definitions, [click here](https://docs.python.org/3/tutorial/controlflow.html) and go to section 4.7.

### F-strings

For more information about f-strings in Python, [click here](https://docs.python.org/3/tutorial/inputoutput.html#tut-f-strings) and go to section 7.1.1.

## Instructions

All the functions will have to be written in the file `override_arithmetics.py`.

### Add

This function takes two arguments which must be integers (other types will not be tested). It adds them, returns the result and prints a line on standard output that shows the calculation and the result. For instance, if the arguments are 3 and 2, the functions displays:
```
3 + 2 = 5
```
with a trailing newline.

### Sub

This function takes two arguments which must be integers (other types will not be tested). It subtracts them, returns the result and prints a line on standard output that shows the calculation and the result. For instance, if the arguments are 3 and 2, the functions displays:
```
3 - 2 = 1
```
with a trailing newline.

### Mul

This function takes two arguments which must be integers (other types will not be tested). It multiplies them, returns the result and prints a line on standard output that shows the calculation and the result. For instance, if the arguments are 3 and 2, the functions displays:
```
3 * 2 = 6
```
with a trailing newline.

### Div

This function takes two arguments which must be integers (other types will not be tested). It divides them, returns the result and prints a line on standard output that shows the calculation and the result.

---
**Be careful!**
This function only keeps the integer part of the result (it is the euclidean division). When the divisor is 0, it should return nothing and print `Detected a division by zero` on the error output.

---


For instance, if the arguments are 18 and 5, the functions displays:
```
18 // 5 = 3
```
with a trailing newline.

### Mod 

This function takes two arguments which must be integers (other types will not be tested). It calculates the modulo between them, returns the result and prints a line on standard output that shows the calculation and the result.

---
**Be careful!**
This function only keeps the integer part of the result (it is the euclidean division). When the divisor is 0, it should return nothing and print `Detected a modulo by zero` on the error output.

---

For instance, if the arguments are 17 and 5, the functions displays:
```
17 % 5 = 2
```
with a trailing newline.

### Pow

This function takes two arguments which must be integers (other types will not be tested). It calculates the first argument to the power of the second one, returns the result and prints a line on standard output that shows the calculation and the result. For instance, if the arguments are 3 and 2, the functions displays:
```
3 ** 2 = 9
```
with a trailing newline.