# Proof Of Three

In this exercise, you will learn Object-Oriented Programming (OOP) and array manipulation in Python through the simulation of a game.

## The game

The game is about finding sets of 3 cards that match some rules.

### The cards

The symbols on a card have 3 characteristics : 
- a color,
- a number of symbols,
- a shape.

The shape can be : wave (`~~`), diamond (`<>`) or rectangle (`==`), there can be 1, 2 or 3 symbols on a card and the color is either red, green or blue.

### Match

3 cards match if their 3 characteristics are either completely the same or totally different.

For instance, a match could be composed of those three cards: 

| color | number | shape     | filling |
|-------|--------|-----------|---------|
| red   | 2      | wave      | hatched |
| blue  | 2      | rectangle | filled  |
| green | 2      | diamond   | empty   |

or: 

| color | number | shape | filling |
|-------|--------|-------|---------|
| red   | 1      | wave  | filled  |
| red   | 2      | wave  | filled  |
| red   | 3      | wave  | filled  |

but not:

| color | number | shape     | filling |
|-------|--------|-----------|---------|
| red   | 1      | wave      | empty   |
| red   | 2      | rectangle | empty   |
| red   | 3      | wave      | empty   |

## Help for this exercise

To learn more about OOP in Python, [click here](https://docs.python.org/3/tutorial/classes.html).

## Instructions

### Card class

The `__init__` method of the `Card` class must have four arguments:
- the shape (a string): either `wave`, `diamond` or `rectangle`,
- the number of symbols (an integer): either 1, 2 or 3,
- the color of the symbols: either `red`, `blue` or `green`.
- the filling of the symbols : `empty`, `hatched` or `filled`.

It must also contain a method `matches_with`, that takes two arguments of the `Card` type and returns `True` if the cards match, and `False` if not.

### Deck class

The Deck class will be responsible to handle the stacks of cards. There will be 3 different stacks: 

- the stack of hidden cards that have not been played yet (the `hidden` array of cards),
- the stack of showed cards (the `showed` array of cards)
- the stack of cards that have already been played (the `played` array of cards).

The Deck class has multiple methods.

#### `__init__`

This method fills the `hidden` array with all the cards in order. The cards must be sorted by color, then by shape, then by number, and finally by filling. In total, there should be 81 cards. The first cards in the `hidden` are therefore : 

```
Card(red, wave, 1, empty)
Card(red, wave, 1, hatched)
Card(red, wave, 1, filled)
Card(red, wave, 2, empty)
Card(red, wave, 2, hatched)
Card(red, wave, 2, filled)
Card(red, wave, 3, empty)
Card(red, wave, 3, hatched)
Card(red, wave, 3, filled)
Card(red, diamond, 1, empty)
Card(red, diamond, 1, hatched)
Card(red, diamond, 1, filled)
...
```

The `__init__` method does not take any argument.

#### `shuffle`

This method shuffles the `hidden` array. Because the shuffle is meant to be random, it takes an optional seed (an integer) as argument. The seed will be passed to `random` to generate numbers. If `None` is passed to `shuffle`, then `None` has to be passed as argument to `random.seed`.

The `shuffle` algorithm is simple. It has 81 steps. For each step $i$,
- generate a random number $j$ between 0 and 80 (0 and 80 included).
- Swap the cards at indices $i$ and $j$ in the array.

If $i = j$ in a step, the algorithm should do nothing.

---
**Be careful!**
This method should raise an `AssertionError` if the hidden array does not have 81 cards, or if the `showed` or `played` arrays are not empty.

---

#### `display_cards`

This method retrieves some cards from the `hidden` array and puts them in the `showed` array. More precisely,

- if the `hidden` array is empty, it does nothing.
- if the `showed` array has less than 12 cards, it removes cards from the `hidden` array until the `showed` array has 12 cards,
- if the `showed` array has 12 cards, it removes cards from the `hidden` array until the `showed` array has 15 cards,
- if the `showed` array has 15 cards, it removes cards from the `hidden` array until the `showed` array has 18 cards.
- if the `showed` array has more than 15 cards, it does nothing.

#### `play_step`

This method tries to match 3 cards in the `showed` array. If multiple matches exist, it preferably matches the cards that have the lowest minimum index in the array.

For example, 
- if the cards at indices `(2, 6, 11)` and `(1, 8, 12)` can be matched, this method chooses the `(2, 6, 11)` match. 
- if the cards at indices `(3, 7, 9)` and `(3, 5, 10)` can be matched, this method chooses the `(3, 5, 10)` match.

If no match has been found, it calls the `display_cards` function.

If a match has been found, this method removes the matched carfs from the `showed` array and puts them in the `played` array.

--- 
**Tip**
Don't worry, the math behind this game shows that a match is always found when the `showed` array has at least 18 cards, but most of the time 12 or 15 cards are enough.

---

At the end of a game, if the `hidden` array is empty and no match has been found, the game is over. It has to print `Game over! Matched cards: {matched_cards}` on the standard output, where `{matched_cards}` is the total number of cards that have been matched.

#### `run_game`

This method runs the game. All it does is `shuffle` the cards in the `hidden` array, call `play_step` while the game is not over.

It therefore takes an optional seed as argument and passes it to the `shuffle` method.