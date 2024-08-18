# Hanoi

In this exercise, you will learn to practice recursivity in functions.

## File tree

hanoi
├── hanoi.py
├── subject_hanoi.md
└── test_hanoi.py

## Instructions

In the file `hanoi.py`, you have to write the function `hanoi`. For more information on what the Tower of Hanoi is, follow [this link](https://en.wikipedia.org/wiki/Tower_of_Hanoi).

The function takes 4 parameters:

- the number of disks (an integer)
- a source pillar (an integer, a string, anything really)
- a destination pillar (same type as above)
- an auxiliary pillar (same type as above)

The goal is to move all the disks from the source to the destination, by moving some first to the auxiliary pillar if necessary.

For each disk moved, the function outputs:
```
Disk has been moved from {pillar1} to {pillar2}
```

with a trailing newline, where `{pillar1}` is replaced by the source pillar of the disk (one of the three pillar arguments of the function) and `{pillar2}` is replaced by the destination pillar of the disk.

Additionally, the function returns the minimal number of steps needed to move all disks from the source pillar to the destination pillar.

---
*Tip!*

The `hanoi` function should be recursive. To help you implement this function, try to follow this "naive" algorithm:

To move all disks from the source pillar to the destination pillar, we do in order:

- move all disks but the biggest one from the source pillar to the auxiliary pillar (that's a recursive part),
- move the biggest disk from the source pillar to the auxiliary pillar,
- move all disks but the biggest one from the auxiliary pillar to the destination pillar (that's another recursive part).

If you implement the recursivity well, the `hanoi` function with n disks should call itself twice with n-1 disks.

The number of steps does not need recursivity to be computed, although you can use the natural recursivity of the function to calculate it. Can you come up with a formula for the minimal number of steps?

---

## Example

`hanoi(2, "A", "C", "B")` will return 3 and output:
```
Disk has been moved from A to B
Disk has been moved from A to C
Disk has been moved from B to C
```

`hanoi(0, 1, 3, 2)` will return 0 and output nothing.
