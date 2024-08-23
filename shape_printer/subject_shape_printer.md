## Shape printer

In this exercise, you will have some fun! It is about printing some nice shapes in the output.

## Instructions

This exercise is composed of five functions you will have to write. Unless explicitly stated, all the functions take three named arguments `width`, `height` and `char`. These arguments have default values:

- `width = 3` by default,
- `height = 3` by default,
- `char = *` by default.

Sometimes, the arguments `width` and `height` will be replaced by a single argument `size`, which default value is 3.

### Rectangle

The function `rectangle` prints a rectangle. For example, calling `rectangle()` (implicitly with argument `width = 3`, `height = 3`, `char = *`) prints
```
***
***
***
```
with a trailing newline.

Calling `rectangle(width = 5, height = 10, char = "i")` prints

```
*****
*****
*****
*****
*****
*****
*****
*****
*****
*****
```
with a trailing newline.

Calling `rectangle(width = 0)` prints nothing.

### Square

This time, the arguments are `size` and `char`. The `square` function prints a square.

Calling `square()` prints

```
***
***
***
```
with a trailing newline.

Calling `square(size = 7, char = "|")` prints

```
|||||||
|||||||
|||||||
|||||||
|||||||
|||||||
|||||||
```

### Pyramid

This function prints a pyramid, pointing upwards. There are spaces before the pyramid on each line, but no space after.

Calling `pyramid()` prints

```
  *
 ***
*****
```
with a trailing newline.

Calling `pyramid(size = 1, char = "%") ` prints

```
%
```
with a trailing newline.

### Empty rectangle

This function prints a special rectangle, because it is empty inside.

Calling `empty_rectangle()` prints

```
***
* *
***
```
with a trailing newline.

Calling `empty_rectangle(width = 7, height = 4)` prints

```
*******
*     *
*     *
*******
```
with a trailing newline.

Calling `empty_rectangle(width = 2, height = 2, char = "m")` prints

```
mm
mm
```
with a trailing newline

### Empty diamond

This functions prints a diamond which is empty inside.

Calling `empty_diamond()` prints

```
  *
 * *
*   *
 * *
  *
```
with a trailing newline.

Calling `empty_diamond(size = 6, char = "=")` prints

```
     =
    = =
   =   =
  =     =
 =       =
=         =
 =       =
  =     =
   =   =
    = =
     =
```
with a trailing newline.

Calling `empty_diamond(size = 1)` prints

```
*
```
with a trailing newline.
