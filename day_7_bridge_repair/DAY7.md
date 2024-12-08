# Advent of Code 2024 - Day 7: Bridge Repair

## Challenge Description

### Part One

The Historians take you to a familiar rope bridge over a river in the middle of a jungle. The Chief isn't on this side of the bridge, though; maybe he's on the other side?

When you go to cross the bridge, you notice a group of engineers trying to repair it. (Apparently, it breaks pretty frequently.) You won't be able to cross until it's fixed.

You ask how long it'll take; the engineers tell you that it only needs final calibrations, but some young elephants were playing nearby and stole all the operators from their calibration equations! They could finish the calibrations if only someone could determine which test values could possibly be produced by placing any combination of operators into their calibration equations (your puzzle input).

#### Example Input:
```
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
```

Each line represents a single equation:
- The test value appears before the colon.
- The remaining numbers must be combined with operators to produce the test value.

#### Rules:
1. Operators are evaluated **left-to-right** (not by precedence).
2. Numbers cannot be rearranged.
3. The operators available are:
   - Addition (`+`)
   - Multiplication (`*`)

#### Example Solutions:
- `190: 10 19`: Choosing `*` results in `10 * 19 = 190`.
- `3267: 81 40 27`: Two configurations match:
  - `81 + 40 * 27 = 3267`
  - `81 * 40 + 27 = 3267`.
- `292: 11 6 16 20`: Solvable as `11 + 6 * 16 + 20 = 292`.

Other equations, such as `156: 15 6`, cannot be solved using only `+` and `*`.

The total calibration result is the sum of test values from solvable equations:
```
190 + 3267 + 292 = 3749
```

**Task:** Determine which equations could possibly be true using only addition and multiplication. What is their total calibration result?

**Puzzle Answer (Part One):** 1430271835320

---

### Part Two

The engineers seem concerned; the total calibration result you gave them is nowhere near safety tolerances. Just then, you spot your mistake: some well-hidden elephants are holding a **third type of operator**.

#### New Operator:
- The **concatenation operator (`||`)** combines the digits from its left and right inputs into a single number.
  - For example: `12 || 345 = 12345`.

Now, in addition to the three solvable equations from Part One, three more equations can be solved using concatenation:

#### Example Solutions with Concatenation:
- `156: 15 6`: Solvable as `15 || 6 = 156`.
- `7290: 6 8 6 15`: Solvable as `6 * 8 || 6 * 15 = 7290`.
- `192: 17 8 14`: Solvable as `17 || 8 + 14 = 192`.

Adding these results to the three from Part One gives:
```
190 + 3267 + 292 + 156 + 7290 + 192 = 11387
```

**Task:** Using all three operators (`+`, `*`, and `||`), determine which equations can possibly be true. What is their total calibration result?

**Puzzle Answer (Part Two):** 456565678667482

---

## Puzzle Answers

- **Part One:** 1430271835320  
- **Part Two:** 456565678667482  

---

## Notes

This challenge involves evaluating mathematical expressions with constraints and testing combinations of operators. Part Two introduces concatenation, expanding the solution space significantly and requiring efficient handling of permutations to determine valid equations.